const fs = require('fs');
const path = require('path');

const {getGuardMostAsleep} = require('./repose-record');

const input = fs.readFileSync(path.resolve(__dirname, `./input.txt`), 'utf8');

const {guard, minutes} = getGuardMostAsleep(input);
console.log('Solution: ', guard, minutes);
