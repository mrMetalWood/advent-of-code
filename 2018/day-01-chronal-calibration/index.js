const fs = require('fs');
const path = require('path');

const {
  getFrequency,
  findFirstDuplicateFrequency
} = require('./chronal-calibration');

const changes = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

const frequency = getFrequency(changes);
console.log('Frequency: ', frequency);

const firstDuplicateFrequency = findFirstDuplicateFrequency(changes);
console.log('First duplicate: ', firstDuplicateFrequency);
