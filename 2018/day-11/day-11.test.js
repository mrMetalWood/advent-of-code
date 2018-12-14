const fs = require('fs');
const path = require('path');

const {day11} = require('./day-11');

test('day11 example 1', () => {
  const {finalCoords} = day11(18, 3);

  expect(finalCoords).toBe('33,45');
});

test('day11 example 1', () => {
  const {finalCoords} = day11(42, 3);

  expect(finalCoords).toBe('21,61');
});

test('day11 example 3', () => {
  const {finalCoords, finalSquareSize} = day11(18);

  expect(`${finalCoords},${finalSquareSize}`).toBe('90,269,16');
});
