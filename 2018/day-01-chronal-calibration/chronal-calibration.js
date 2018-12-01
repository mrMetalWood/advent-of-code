function getFrequency(changes) {
  return changes
    .split('\n')
    .reduce((frequency, change) => (frequency += Number(change)), 0);
}

function findFirstDuplicateFrequency(input) {
  const changes = input.split('\n');
  let index = -1;

  let frequency = 0;
  const allFrequencies = [frequency];
  let foundDuplicate = false;

  while (!foundDuplicate) {
    frequency += Number(changes[++index % changes.length]);

    if (allFrequencies.includes(frequency)) {
      foundDuplicate = true;
    }

    allFrequencies.push(frequency);
  }

  return frequency;
}

module.exports = {getFrequency, findFirstDuplicateFrequency};
