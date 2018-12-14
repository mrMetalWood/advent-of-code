const fs = require('fs');
const path = require('path');

const {day11} = require('./day-11');

const input = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

const output1 = day11(7672, 3);
console.log('Output 1: ', output1);

const output2 = day11(7672);
console.log('Output 2: ', output2);
