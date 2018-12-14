const {raw} = window;

let cars = [];
let crashedCars = [];
const crashedLocations = [];
let pause = false;
let tickCount = 0;

const intersectionDirections = ['left', 'straight', 'right'];

const getNewDirection = car => {
  const action = intersectionDirections[car.directionCycle % 3];

  if (car.placeholder === '+') {
    car.directionCycle++;
    switch (car.direction) {
      case '^':
        return action === 'left'
          ? '<'
          : action === 'right'
          ? '>'
          : car.direction;
      case '>':
        return action === 'left'
          ? '^'
          : action === 'right'
          ? 'v'
          : car.direction;
      case 'v':
        return action === 'left'
          ? '>'
          : action === 'right'
          ? '<'
          : car.direction;
      case '<':
        return action === 'left'
          ? 'v'
          : action === 'right'
          ? '^'
          : car.direction;
      default:
        return car.direction;
    }
  } else if (car.placeholder === '\\') {
    switch (car.direction) {
      case '^':
        return '<';
      case '>':
        return 'v';
      case 'v':
        return '>';
      case '<':
        return '^';
      default:
        return car.direction;
    }
  } else if (car.placeholder === '/') {
    switch (car.direction) {
      case '^':
        return '>';
      case '>':
        return '^';
      case 'v':
        return '<';
      case '<':
        return 'v';
      default:
        return car.direction;
    }
  }

  return car.direction;
};

const state = raw.split('\n').map((line, yIndex) => {
  const splitLine = line.split('');

  splitLine.forEach((cell, xIndex) => {
    let car = null;
    let placeholder = null;
    switch (cell) {
      case '^':
        car = '^';
        placeholder = '|';
        break;
      case '>':
        car = '>';
        placeholder = '-';
        break;
      case 'v':
        car = 'v';
        placeholder = '|';
        break;
      case '<':
        car = '<';
        placeholder = '-';
        break;

      default:
        break;
    }
    if (car) {
      cars.push({
        x: xIndex,
        y: yIndex,
        direction: car,
        directionCycle: 0,
        placeholder,
        id: `${xIndex}-${yIndex}`
      });
    }
  });

  return splitLine;
});

const tick = () => {
  tickCount++;
  cars = cars.sort((a, b) => {
    if (a.y === b.y) {
      return a.x - b.x;
    }

    return a.y - b.y;
  });

  cars.forEach(car => {
    state[car.y][car.x] = car.placeholder;

    switch (car.direction) {
      case '^':
        car.y -= 1;
        car.placeholder = state[car.y][car.x];
        break;
      case '>':
        car.x = car.x + 1;
        car.placeholder = state[car.y][car.x];
        break;
      case 'v':
        car.y += 1;
        car.placeholder = state[car.y][car.x];
        break;
      case '<':
        car.x -= 1;
        car.placeholder = state[car.y][car.x];
        break;
    }

    cars
      .filter(c => c.id !== car.id)
      .forEach(c => {
        if (c.x === car.x && c.y === car.y) {
          console.log('Bammm, crashed', car, c);
          crashedCars.push(c.id, car.id);
          crashedLocations.push({x: car.x, y: car.y});
          state[car.y][car.x] = c.placeholder;
        }
      });

    if (!crashedCars.includes(car.id)) {
      car.direction = getNewDirection(car);
      state[car.y][car.x] = car.direction;
    }
  });

  cars = cars.filter(c => !crashedCars.includes(c.id));

  if (cars.length === 1) {
    console.log('Location of last car: ', `${cars[0].x},${cars[0].y}`);
  }

  const stateToRender = JSON.parse(JSON.stringify(state));
  cars.forEach(car => {
    const {x, y} = car;
    stateToRender[y][x] = `<span class="car">${stateToRender[y][x]}</span>`;
  });

  crashedLocations.forEach(car => {
    const {x, y} = car;
    stateToRender[y][x] = `<span class="crashed">${stateToRender[y][x]}</span>`;
  });

  document.body.innerHTML = stateToRender.map(line => line.join('')).join('\n');

  if (tickCount % 500 === 0) {
    console.log('tick', tickCount);
  }

  if (!pause && cars.length > 1) {
    setTimeout(tick, 1);
  }
};

// tick();

document.addEventListener('keyup', event => {
  if (event.keyCode === 13) {
    tick();
  }
  if (event.keyCode === 18) {
    pause = !pause;
  }
});
