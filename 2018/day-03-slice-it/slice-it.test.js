const {getOverlappingArea, getNonOverlappingId} = require('./slice-it');

test('getOverlappingArea example', () => {
  const input = '#1 @ 1,3: 4x4\n #2 @ 3,1: 4x4\n #3 @ 5,5: 2x2';
  expect(getOverlappingArea(input)).toBe(4);
});

test('getNonOverlappingId example', () => {
  const input = '#1 @ 1,3: 4x4\n #2 @ 3,1: 4x4\n #3 @ 4,3: 2x2';
  expect(getOverlappingArea(input)).toBe(6);
});

test('getOverlappingArea example', () => {
  const input = '#1 @ 1,3: 4x4\n#3 @ 5,5: 2x2\n #2 @ 3,1: 4x4';
  expect(getNonOverlappingId(input)).toBe('#3');
});
