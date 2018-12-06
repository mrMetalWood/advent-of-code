const fs = require('fs');
const path = require('path');

const {day61, day62} = require('./day-6');

const input = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

const output1 = day61(input);
console.log('Output 1: ', output1);

const output2 = day62(input, 10000);
console.log('Output 2: ', output2);
