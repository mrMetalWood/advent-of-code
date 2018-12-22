const fs = require('fs');
const path = require('path');

const {day161} = require('./day-16');

test('day161 example 1', () => {
  const input = [
    {
      before: [3, 2, 1, 1],
      instruction: [9, 2, 1, 2],
      after: [3, 2, 2, 1]
    }
  ];

  expect(day161(input)).toBe(1);
});
