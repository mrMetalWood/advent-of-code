const fs = require('fs');
const path = require('path');

const {day91, day92} = require('./day-9');

test('day91 example', () => {
  expect(day91(9, 25)).toBe(32);
});

test('day91 example', () => {
  expect(day91(10, 1618)).toBe(8317);
});

test('day91 example2', () => {
  expect(day91(13, 7999)).toBe(146373);
});

test('day91 example2', () => {
  expect(day91(17, 1104)).toBe(2764);
});

test('day91 example2', () => {
  expect(day91(21, 6111)).toBe(54718);
});

test('day91 example2', () => {
  expect(day91(30, 5807)).toBe(37305);
});
