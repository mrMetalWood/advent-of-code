const caps = [...Array(26)].map((val, i) => String.fromCharCode(i + 65));
const lower = caps.map(letter => letter.toLowerCase());

const letterCombinations = [];
for (let i = 0; i < caps.length; i++) {
  letterCombinations.push(`${caps[i]}${lower[i]}`);
  letterCombinations.push(`${lower[i]}${caps[i]}`);
}

const regexAll = new RegExp(letterCombinations.join('|'), 'g');

function getReducedLength(input) {
  while (regexAll.test(input)) {
    input = input.replace(regexAll, '');
  }

  return input.length;
}

function getReducedLength2(input) {
  const allLength = [];

  caps.forEach((letter, index) => {
    const regexSingle = new RegExp(`${letter}|${lower[index]}`, 'g');
    let inputTemp = input.replace(regexSingle, '');

    while (regexAll.test(inputTemp)) {
      inputTemp = inputTemp.replace(regexAll, '');
    }

    allLength.push(inputTemp.length);
  });

  return allLength.sort((a, b) => a - b)[0];
}
module.exports = {getReducedLength, getReducedLength2};
