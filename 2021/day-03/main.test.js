const { powerConsumption, lifeSupportRating } = require('./solution');

const input = [
  '00100',
  '11110',
  '10110',
  '10111',
  '10101',
  '01111',
  '00111',
  '11100',
  '10000',
  '11001',
  '00010',
  '01010',
];

describe('part one', () => {
  test('should report correct power comsumption', () => {
    expect(powerConsumption(input)).toBe(198);
  });
});

describe('part two', () => {
  test('should report correct life support rating', () => {
    expect(lifeSupportRating(input)).toBe(230);
  });
});
