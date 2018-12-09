const fs = require('fs');
const path = require('path');

const {day81, day82} = require('./day-8');

const input = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

const output1 = day81(input);
console.log('Output 1: ', output1);

const output2 = day82(input);
console.log('Output 2: ', output2);
