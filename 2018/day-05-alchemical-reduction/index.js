const fs = require('fs');
const path = require('path');

const {getReducedLength, getReducedLength2} = require('./alchemical-reduction');

const input = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

const length = getReducedLength(input);
console.log('Reduced length: ', length);

const length2 = getReducedLength2(input);
console.log('Reduced length 2: ', length2);
