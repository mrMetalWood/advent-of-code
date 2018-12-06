function getCoordinates(input) {
  const lines = input.split('\n');
  let gridWidth = 0;
  let gridHeight = 0;

  const coordinates = lines.map((line, index) => {
    const splitLine = line.split(',');

    const x = Number(splitLine[0].trim());
    const y = Number(splitLine[1].trim());

    if (x > gridWidth) {
      gridWidth = x;
    }

    if (y > gridHeight) {
      gridHeight = y;
    }

    return {x, y, id: index};
  });

  return {coordinates, gridWidth, gridHeight};
}

function day61(input) {
  const {coordinates, gridWidth, gridHeight} = getCoordinates(input);

  const all = {};
  const infiniteCoordinates = [];

  for (let i = 0; i <= gridWidth; i++) {
    for (let j = 0; j <= gridHeight; j++) {
      const point = {x: i, y: j};

      const distancesToCoordinates = {};
      coordinates.forEach(coordinate => {
        distancesToCoordinates[coordinate.id] =
          Math.abs(coordinate.x - point.x) + Math.abs(coordinate.y - point.y);
      });

      const nearestToPoint = Object.entries(distancesToCoordinates).sort(
        (a, b) => a[1] - b[1]
      );

      if (i === 0 || i === gridWidth || j === 0 || j === gridHeight) {
        if (!infiniteCoordinates.includes(nearestToPoint[0][0])) {
          infiniteCoordinates.push(nearestToPoint[0][0]);
        }
      }

      if (nearestToPoint[0][1] < nearestToPoint[1][1]) {
        all[nearestToPoint[0][0]] = all[nearestToPoint[0][0]]
          ? all[nearestToPoint[0][0]] + 1
          : 1;
      }
    }
  }

  const [, largestArea] = Object.entries(all)
    .filter(([coordinateId]) => !infiniteCoordinates.includes(coordinateId))
    .sort(([, area1], [, area2]) => area2 - area1)[0];

  return largestArea;
}

function day62(input, size) {
  const {coordinates, gridWidth, gridHeight} = getCoordinates(input);

  let area = 0;

  for (let i = 0; i <= gridWidth; i++) {
    for (let j = 0; j <= gridHeight; j++) {
      const point = {x: i, y: j};

      const distanceToAll = coordinates.reduce((sum, coordinate) => {
        let stuff =
          Math.abs(coordinate.x - point.x) + Math.abs(coordinate.y - point.y);
        return sum + stuff;
      }, 0);

      if (distanceToAll < size) {
        area++;
      }
    }
  }

  return area;
}

module.exports = {day61, day62};
