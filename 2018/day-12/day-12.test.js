const fs = require('fs');
const path = require('path');

const {day121} = require('./day-12');

test('day121 example', () => {
  const spread = {
    '...##': '#',
    '..#..': '#',
    '.#...': '#',
    '.#.#.': '#',
    '.#.##': '#',
    '.##..': '#',
    '.####': '#',
    '#.#.#': '#',
    '#.###': '#',
    '##.#.': '#',
    '##.##': '#',
    '###..': '#',
    '###.#': '#',
    '####.': '#'
  };

  const initialState = '#..#.#..##......###...###';

  expect(day121(initialState, spread, 20)).toBe(325);
});
