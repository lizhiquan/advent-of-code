function powerConsumption(arr) {
  const oneFreq = [];
  for (const item of arr) {
    for (let i = 0; i < item.length; i++) {
      if (item.charAt(i) === '1') {
        oneFreq[i] = (oneFreq[i] || 0) + 1;
      }
    }
  }
  const gammaRate = oneFreq
    .map((val) => (val > arr.length / 2 ? '1' : '0'))
    .join('');
  const epsilonRate = [...gammaRate]
    .map((val) => (val === '1' ? '0' : '1'))
    .join('');

  return parseInt(gammaRate, 2) * parseInt(epsilonRate, 2);
}

function lifeSupportRating(arr) {
  var data = [...arr];
  for (let i = 0; data.length > 1; i++) {
    const bits = data.map((val) => val.charAt(i));
    const oneCount = bits.reduce(
      (acc, val) => (val === '1' ? acc + 1 : acc),
      0
    );
    const selectedBit = oneCount >= bits.length / 2 ? '1' : '0';
    data = data.filter((val) => val.charAt(i) === selectedBit);
  }
  const oxygenGeneratorRating = parseInt(data[0], 2);

  data = [...arr];
  for (let i = 0; data.length > 1; i++) {
    const bits = data.map((val) => val.charAt(i));
    const zeroCount = bits.reduce(
      (acc, val) => (val === '0' ? acc + 1 : acc),
      0
    );
    const selectedBit = zeroCount <= bits.length / 2 ? '0' : '1';
    data = data.filter((val) => val.charAt(i) === selectedBit);
  }
  const co2ScrubberRating = parseInt(data[0], 2);

  return oxygenGeneratorRating * co2ScrubberRating;
}

exports.powerConsumption = powerConsumption;
exports.lifeSupportRating = lifeSupportRating;
