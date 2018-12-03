function getChecksum(input) {
  const charCount = input.split('\n').map(id =>
    id.split('').reduce((count, char) => {
      count[char] = count[char] ? count[char] + 1 : 1;
      return count;
    }, {})
  );

  const hasExactAmount = (id, amount) =>
    Object.values(id).some(char => char === amount);

  const exactlyTwo = charCount.filter(id => hasExactAmount(id, 2)).length;
  const exactlyThree = charCount.filter(id => hasExactAmount(id, 3)).length;

  return exactlyTwo * exactlyThree;
}

function getCommonCharacters(input) {
  const ids = input.split('\n').map(id => id.split(''));
  let commonChars = '';

  while (ids.length > 0) {
    const nextId = ids.pop();

    ids.forEach(id => {
      const temp = [];

      id.forEach((char, index) => {
        if (nextId[index] === char) {
          temp.push(char);
        }
      });

      if (temp.length === id.length - 1) {
        commonChars = temp.join('');
      }
    });

    if (commonChars) {
      break;
    }
  }

  return commonChars;
}

module.exports = {getChecksum, getCommonCharacters};
