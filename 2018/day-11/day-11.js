function day11(gridSerialNumber, square = false) {
  const gridSize = 300;

  let max = 0;
  let finalCoords = '';
  let finalSquareSize = 0;

  let summedAreaTable = [...Array.from({length: gridSize})].map(e =>
    Array.from({length: gridSize})
  );

  let grid = [...Array.from({length: gridSize})]
    .map(e => Array.from({length: gridSize}))
    .map((row, y) => {
      let sum = 0;

      return row.map((_, x) => {
        const rackId = x + 1 + 10;
        let power = rackId * (y + 1);
        power = power + gridSerialNumber;
        power = power * rackId;
        power = Number(`000${power}`.slice(-3).split('')[0]);
        power = power - 5;

        sum = sum + power;

        if (y === 0) {
          summedAreaTable[y][x] = sum;
        } else {
          summedAreaTable[y][x] = summedAreaTable[y - 1][x] + sum;
        }

        return power;
      });
    });

  const squareLoopEnd = square || gridSize;

  for (let squareSize = 1; squareSize <= squareLoopEnd; squareSize++) {
    for (let y = 0; y < gridSize + 1 - squareSize; y++) {
      for (let x = 0; x < gridSize + 1 - squareSize; x++) {
        let square = 0;

        if (y > 0 && x > 0) {
          square =
            summedAreaTable[y + squareSize - 1][x + squareSize - 1] +
            summedAreaTable[y - 1][x - 1] -
            summedAreaTable[y - 1][x + squareSize - 1] -
            summedAreaTable[y + squareSize - 1][x - 1];
        }

        if (square > max) {
          max = square;
          finalCoords = `${x + 1},${y + 1}`;
          finalSquareSize = squareSize;
        }
      }
    }
  }

  return {finalCoords, finalSquareSize, max};
}

module.exports = {day11};
