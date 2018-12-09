const fs = require('fs');
const path = require('path');

const {day81, day82} = require('./day-8');

test('day81 example', () => {
  const input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2';

  expect(day81(input)).toBe(138);
});

test('day81 real', () => {
  const input = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

  expect(day81(input)).toBe(40701);
});

test('day82 example', () => {
  const input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2';

  expect(day82(input)).toBe(66);
});

test('day82 real', () => {
  const input = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

  expect(day82(input)).toBe(21399);
});
