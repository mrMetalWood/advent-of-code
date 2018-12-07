const fs = require('fs');
const path = require('path');

const {day71, day72} = require('./day-7');

const input = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

const output1 = day71(input);
console.log('Output 1: ', output1);

const output2 = day72(input, 5, 60);
console.log('Output 2: ', output2);
