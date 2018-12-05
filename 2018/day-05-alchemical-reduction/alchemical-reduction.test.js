const {getReducedLength, getReducedLength2} = require('./alchemical-reduction');

test('getReducedLength example', () => {
  const input = 'dabAcCaCBAcCcaDA';

  expect(getReducedLength(input)).toBe(10);
});

test('getReducedLength2 example', () => {
  const input = 'dabAcCaCBAcCcaDA';

  expect(getReducedLength2(input)).toBe(4);
});
