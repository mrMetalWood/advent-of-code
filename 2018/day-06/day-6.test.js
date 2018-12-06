const {day61, day62} = require('./day-6');

test('day61 example', () => {
  const input = '1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9';

  expect(day61(input)).toBe(17);
});

test('day62 example', () => {
  const input = '1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9';

  expect(day62(input, 32)).toBe(16);
});
