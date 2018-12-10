function day91(players, lastMarblePoints) {
  const ledger = [0];
  let currentIndex = 0;
  let currentElf = 0;
  const elfScores = {};

  for (let marble = 1; marble <= lastMarblePoints; marble++) {
    const elf = currentElf % players;

    if (marble % 23 === 0) {
      elfScores[elf] = elfScores[elf] ? elfScores[elf] + marble : marble;

      currentIndex -= 7;

      if (currentIndex < 0) {
        currentIndex = ledger.length + currentIndex;
      }

      const extraPoints = ledger.splice(currentIndex, 1)[0];
      elfScores[elf] = elfScores[elf] + extraPoints;
    } else {
      currentIndex += 2;

      if (!ledger[currentIndex] && !ledger[currentIndex - 1]) {
        currentIndex = 1;
      }

      ledger.splice(currentIndex, 0, marble);
    }

    currentElf++;
  }

  const biggestScore = Object.entries(elfScores)
    .map(([, score]) => score)
    .sort((a, b) => b - a)[0];

  return biggestScore;
}

function day92(input) {
  return 9999;
}

module.exports = {day91, day92};
