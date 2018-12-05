const fs = require('fs');
const path = require('path');

const {getOverlappingArea, getNonOverlappingId} = require('./slice-it');

const input = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

const area = getOverlappingArea(input);
console.log('Overlapping area:  ', area);

const stuff = getNonOverlappingId(input);
console.log('Non overlapping id: ', stuff);
