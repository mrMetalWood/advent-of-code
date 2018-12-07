const fs = require('fs');
const path = require('path');

const {day71, day72} = require('./day-7');

test('day71 example', () => {
  const input =
    'Step C must be finished before step A can begin.\nStep C must be finished before step F can begin.\nStep A must be finished before step B can begin.\nStep A must be finished before step D can begin.\nStep B must be finished before step E can begin.\nStep D must be finished before step E can begin.\nStep F must be finished before step E can begin.';

  expect(day71(input)).toBe('CABDFE');
});

test('day72 example', () => {
  const input =
    'Step C must be finished before step A can begin.\nStep C must be finished before step F can begin.\nStep A must be finished before step B can begin.\nStep A must be finished before step D can begin.\nStep B must be finished before step E can begin.\nStep D must be finished before step E can begin.\nStep F must be finished before step E can begin.';

  expect(day72(input, 2, 0)).toBe(15);
});

test('day72 real', () => {
  const input = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

  expect(day72(input, 10, 60)).toBe(1265);
});
