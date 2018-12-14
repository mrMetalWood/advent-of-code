const fs = require('fs');
const path = require('path');

const {day14, day142} = require('./day-14');

test('day14 example 1', () => {
  expect(day14(9)).toBe('5158916779');
});

test('day14 example 2', () => {
  expect(day14(5)).toBe('0124515891');
});

test('day14 example 3', () => {
  expect(day14(18)).toBe('9251071085');
});

test('day14 example 4', () => {
  expect(day14(2018)).toBe('5941429882');
});

test('day142 example 1', () => {
  expect(day142('51589')).toBe(9);
});

test('day142 example 2', () => {
  expect(day142('01245')).toBe(5);
});

test('day142 example 3', () => {
  expect(day142('92510')).toBe(18);
});

test('day142 example 4', () => {
  expect(day142('59414')).toBe(2018);
});
