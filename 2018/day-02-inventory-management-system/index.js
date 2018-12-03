const fs = require('fs');
const path = require('path');

const {
  getChecksum,
  getCommonCharacters
} = require('./inventory-management-system');

const ids = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

const checksum = getChecksum(ids);
console.log('Checksum: ', checksum);

const commonLetters = getCommonCharacters(ids);
console.log('Common letters: ', commonLetters);
