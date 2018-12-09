function getSum(array) {
  return array.reduce((sum, item) => sum + item, 0);
}

function prepareData(input) {
  const licenceFileNumbers = input.split(' ').map(Number);
  const tree = {};

  const buildTree = node => {
    const [childrenCount, metaCount] = licenceFileNumbers.splice(0, 2);

    node.children = [];

    for (let i = 0; i < childrenCount; i++) {
      node.children[i] = {};
      buildTree(node.children[i]);
    }

    node.meta = licenceFileNumbers.splice(0, metaCount);
    node.value = node.children.length
      ? node.meta.reduce((value, m) => {
          return (value += node.children[m - 1]
            ? node.children[m - 1].value
            : 0);
        }, 0)
      : getSum(node.meta);
  };

  buildTree(tree);

  return {tree};
}

function day81(input) {
  const {tree} = prepareData(input);

  const parse = node => {
    let sum = 0;

    node.children.forEach(child => {
      sum += parse(child);
    });

    return (sum += getSum(node.meta));
  };

  return parse(tree);
}

function day82(input, workerCount, additionalTime) {
  const {tree} = prepareData(input);
  return tree.value;
}

module.exports = {day81, day82};
