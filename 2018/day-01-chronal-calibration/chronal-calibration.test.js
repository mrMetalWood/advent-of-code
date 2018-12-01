const {
  getFrequency,
  findFirstDuplicateFrequency
} = require('./chronal-calibration');

test('getFrequency (+1, -2, +3, +1)', () => {
  const changes = '+1\n-2\n+3\n+1';
  expect(getFrequency(changes)).toBe(3);
});

test('getFrequency (+1, +1, +1)', () => {
  const changes = '+1\n+1\n+1';
  expect(getFrequency(changes)).toBe(3);
});

test('getFrequency (+1, +1, -2)', () => {
  const changes = '+1\n+1\n-2';
  expect(getFrequency(changes)).toBe(0);
});

test('getFrequency (-1, -2, -3)', () => {
  const changes = '-1\n-2\n-3';
  expect(getFrequency(changes)).toBe(-6);
});

test('findFirstDuplicateFrequency (+1, -1)', () => {
  const changes = '+1\n-1';
  expect(findFirstDuplicateFrequency(changes)).toBe(0);
});

test('findFirstDuplicateFrequency (+3, +3, +4, -2, -4)', () => {
  const changes = '+3\n+3\n+4\n-2\n-4';
  expect(findFirstDuplicateFrequency(changes)).toBe(10);
});

test('findFirstDuplicateFrequency (-6, +3, +8, +5, -6)', () => {
  const changes = '-6\n+3\n+8\n+5\n-6';
  expect(findFirstDuplicateFrequency(changes)).toBe(5);
});

test('findFirstDuplicateFrequency (+7, +7, -2, -7, -4)', () => {
  const changes = '+7\n+7\n-2\n-7\n-4';
  expect(findFirstDuplicateFrequency(changes)).toBe(14);
});
