const {
  getChecksum,
  getCommonCharacters
} = require('./inventory-management-system');

test('getChecksum example', () => {
  const boxIds = 'abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab';

  expect(getChecksum(boxIds)).toBe(12);
});

test('getCommonCharacters example', () => {
  const boxIds = 'abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz';

  expect(getCommonCharacters(boxIds)).toBe('fgij');
});
