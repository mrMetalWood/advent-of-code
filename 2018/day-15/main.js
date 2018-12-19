const {raw} = window;

const grid = document.querySelector('.grid');
const overlay = document.querySelector('.overlay');
let debug = false;
let pause = false;
let battleEnd = false;
let roundCount = 1;

const elfAttack = 34;

let units = [];
const deadUnits = [];

// directions - north, eaast, south, west
const dx = [0, 1, 0, -1];
const dy = [-1, 0, 1, 0];

const state = raw.split('\n').map(line => line.split(''));

state.forEach((row, y) => {
  row.forEach((cell, x) => {
    if (cell === 'E') {
      units.push({
        type: 'E',
        x,
        y,
        hp: 200,
        id: `${x}-${y}`
      });
    }
    if (cell === 'G') {
      units.push({
        type: 'G',
        x,
        y,
        hp: 200,
        id: `${x}-${y}`
      });
    }
  });
});

const initialElfCount = units.filter(unit => unit.type === 'E').length;

grid.innerHTML = state.map(line => line.join('')).join('\n');
console.log('initial', {state, units});

const sortByReadingOrder = (a, b) => {
  if (a.y === b.y) {
    return a.x - b.x;
  }

  return a.y - b.y;
};

const shortestPath = (start, finish) => {
  const stack = [{x: start.x, y: start.y}];
  let stepCount = 0;
  let reachedEnd = false;
  let nodesLeftInlayer = 1;
  let nodesInNextLayer = 0;
  const visited = state.map(row => row.map(cell => false));

  while (stack.length) {
    const next = stack.shift();
    visited[next.y][next.x] = true;

    if (next.x === finish.x && next.y === finish.y) {
      reachedEnd = true;
      break;
    }

    for (let i = 0; i < 4; i++) {
      const x = next.x + dx[i];
      const y = next.y + dy[i];
      const position = state[y][x];

      if (position === '.' && !visited[y][x]) {
        stack.push({x, y});
        visited[y][x] = true;
        nodesInNextLayer++;
      }
    }

    nodesLeftInlayer--;

    if (nodesLeftInlayer === 0) {
      nodesLeftInlayer = nodesInNextLayer;
      nodesInNextLayer = 0;
      stepCount++;
    }
  }

  if (reachedEnd) {
    return stepCount;
  }

  return -1;
};

const move = unit => {
  state[unit.y][unit.x] = '.';

  const enemies = units.filter(
    u => u.type !== unit.type && !deadUnits.includes(u.id)
  );

  const inRange = [];

  enemies.forEach(enemy => {
    for (let i = 0; i < 4; i++) {
      const x = enemy.x + dx[i];
      const y = enemy.y + dy[i];
      const position = state[y][x];

      if (position === '.') {
        inRange.push({x, y});
      }
    }
  });

  const nearest = inRange
    .map(cell => {
      return {
        x: cell.x,
        y: cell.y,
        pathLength: shortestPath({x: unit.x, y: unit.y}, cell)
      };
    })
    .filter(cell => cell.pathLength !== -1)
    .sort((a, b) => {
      if (a.pathLength === b.pathLength) {
        return sortByReadingOrder(a, b);
      }

      return a.pathLength - b.pathLength;
    });

  if (nearest.length) {
    let startPoints = [];
    for (let i = 0; i < 4; i++) {
      const x = unit.x + dx[i];
      const y = unit.y + dy[i];
      const position = state[y][x];

      if (position === '.') {
        startPoints.push({x, y, pathLength: shortestPath({x, y}, nearest[0])});
      }
    }

    const startPoint = startPoints
      .filter(path => path.pathLength !== -1)
      .sort((a, b) => {
        if (a.pathLength === b.pathLength) {
          return sortByReadingOrder(a, b);
        }

        return a.pathLength - b.pathLength;
      })[0];

    // Debug
    if (debug) {
      overlay.innerHTML = '';
      const ov = JSON.parse(JSON.stringify(state)).map(line =>
        line.map(c => ' ')
      );
      ov[unit.y][unit.x] = `<span class="unit"> </span>`;
      inRange.forEach(cell => {
        ov[cell.y][cell.x] = '<span class="inrange"> </span>';
      });
      ov[nearest[0].y][nearest[0].x] = '<span class="nearest"> </span>';
      ov[startPoint.y][startPoint.x] = '<span class="selected"> </span>';

      overlay.innerHTML = ov.map(line => line.join('')).join('\n');
      grid.innerHTML = state.map(line => line.join('')).join('\n');
      // debugger;
    }
    // Debug end

    unit.x = startPoint.x;
    unit.y = startPoint.y;
  }

  state[unit.y][unit.x] = unit.type;
};

const getPossibleTargets = unit => {
  const enemies = units.filter(
    u => u.type !== unit.type && !deadUnits.includes(u.id)
  );

  let possibleTargets = [];
  for (let i = 0; i < 4; i++) {
    const x = unit.x + dx[i];
    const y = unit.y + dy[i];
    const position = state[y][x];

    const enemy = enemies.find(enemy => enemy.x === x && enemy.y === y);

    if (enemy) {
      possibleTargets.push(enemy);
    }
  }

  if (possibleTargets.length) {
    possibleTargets = possibleTargets.sort((a, b) => {
      if (a.hp === b.hp) {
        return sortByReadingOrder(a, b);
      }

      return a.hp - b.hp;
    });
  }

  return possibleTargets;
};

const attack = (unit, target, unitIndex) => {
  if (unit.type === 'E') {
    target.hp -= elfAttack;
  } else {
    target.hp -= 3;
  }

  if (target.hp <= 0) {
    state[target.y][target.x] = '.';
    deadUnits.push(target.id);
    if (unitIndex === units.length - 1) {
      roundComplete = true;
    }
  }
};

const timeout = ms => {
  return new Promise(resolve => setTimeout(resolve, ms));
};

const round = () => {
  units = units.sort(sortByReadingOrder);

  let roundComplete = false;

  (async function() {
    let index = 0;
    for await (unit of units) {
      // Debug
      if (debug) {
        await timeout(300);
      }
      // Debug end
      if (!deadUnits.includes(unit.id)) {
        const possibleTargets = getPossibleTargets(unit);

        if (possibleTargets.length) {
          attack(unit, possibleTargets[0], index);
        } else {
          move(unit);

          const newPossibleTargets = getPossibleTargets(unit);
          if (newPossibleTargets.length) {
            attack(unit, newPossibleTargets[0], index);
          }
        }
      }

      index++;
      grid.innerHTML = state.map(line => line.join('')).join('\n');
    }

    units = units.filter(unit => !deadUnits.includes(unit.id));

    // grid.innerHTML = state.map(line => line.join('')).join('\n');

    if (
      units.every(unit => unit.type === 'E') ||
      units.every(unit => unit.type === 'G')
    ) {
      battleEnd = true;
    }

    const unitsHP = units.reduce((sum, unit) => (sum += unit.hp), 0);
    const rounds = roundComplete ? roundCount : roundCount - 1;

    console.log(
      `Round: ${rounds} -  UnitsHP: ${unitsHP} - Score: ${rounds *
        unitsHP} - Elves: ${units.filter(unit => unit.type === 'E').length}`
    );

    roundCount++;

    if (!pause && !battleEnd) {
      setTimeout(round, 100);
    }
  })();

  // units.forEach((unit, index) => {
  //   if (!deadUnits.includes(unit.id)) {
  //     const possibleTargets = getPossibleTargets(unit);

  //     if (possibleTargets.length) {
  //       attack(unit, possibleTargets[0], index);
  //     } else {
  //       move(unit);

  //       const newPossibleTargets = getPossibleTargets(unit);
  //       if (newPossibleTargets.length) {
  //         attack(unit, newPossibleTargets[0], index);
  //       }
  //     }
  //   }
  // });

  // units = units.filter(unit => !deadUnits.includes(unit.id));

  // grid.innerHTML = state.map(line => line.join('')).join('\n');

  // if (
  //   units.every(unit => unit.type === 'E') ||
  //   units.every(unit => unit.type === 'G')
  // ) {
  //   battleEnd = true;
  // }

  // const unitsHP = units.reduce((sum, unit) => (sum += unit.hp), 0);
  // const rounds = roundComplete ? roundCount : roundCount - 1;

  // console.log(
  //   `Round: ${rounds} -  UnitsHP: ${unitsHP} - Score: ${rounds *
  //     unitsHP} - Elves: ${units.filter(unit => unit.type === 'E').length}`
  // );

  // roundCount++;

  // if (!pause && !battleEnd) {
  //   setTimeout(round, 200);
  // }
};

if (!pause) {
  round();
}

document.addEventListener('keyup', event => {
  if (event.keyCode === 13) {
    round();
  }
  if (event.keyCode === 18) {
    pause = !pause;
  }
});

// correct part 1: 226688
// correct part 2: 62958
