const fs = require('fs');
const { powerConsumption, lifeSupportRating } = require('./solution');

const input = fs.readFileSync('input.txt', 'utf8').split('\n');
console.log('Part 1: ', powerConsumption(input));
console.log('Part 2: ', lifeSupportRating(input));
