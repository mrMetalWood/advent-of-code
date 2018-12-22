function addr(registers, [a, b, c]) {
  registers[c] = registers[a] + registers[b];
  return registers;
}
function addi(registers, [a, b, c]) {
  registers[c] = registers[a] + b;
  return registers;
}
function mulr(registers, [a, b, c]) {
  registers[c] = registers[a] * registers[b];
  return registers;
}
function muli(registers, [a, b, c]) {
  registers[c] = registers[a] * b;
  return registers;
}
function banr(registers, [a, b, c]) {
  registers[c] = registers[a] & registers[b];
  return registers;
}
function bani(registers, [a, b, c]) {
  registers[c] = registers[a] & b;
  return registers;
}
function borr(registers, [a, b, c]) {
  registers[c] = registers[a] | registers[b];
  return registers;
}
function bori(registers, [a, b, c]) {
  registers[c] = registers[a] | b;
  return registers;
}
function setr(registers, [a, b, c]) {
  registers[c] = registers[a];
  return registers;
}
function seti(registers, [a, b, c]) {
  registers[c] = a;
  return registers;
}
function gtir(registers, [a, b, c]) {
  registers[c] = a > registers[b] ? 1 : 0;
  return registers;
}
function gtri(registers, [a, b, c]) {
  registers[c] = registers[a] > b ? 1 : 0;
  return registers;
}
function gttr(registers, [a, b, c]) {
  registers[c] = registers[a] > registers[b] ? 1 : 0;
  return registers;
}
function eqir(registers, [a, b, c]) {
  registers[c] = a === registers[b] ? 1 : 0;
  return registers;
}
function eqri(registers, [a, b, c]) {
  registers[c] = registers[a] === b ? 1 : 0;
  return registers;
}
function eqrr(registers, [a, b, c]) {
  registers[c] = registers[a] === registers[b] ? 1 : 0;
  return registers;
}

function pbcopy(data) {
  var proc = require('child_process').spawn('pbcopy');
  proc.stdin.write(data);
  proc.stdin.end();
}

const operations = {
  addr,
  addi,
  mulr,
  muli,
  banr,
  bani,
  borr,
  bori,
  setr,
  seti,
  gtir,
  gtri,
  gttr,
  eqir,
  eqri,
  eqrr
};

let possibleOperationMapping = new Map();

function day161(input) {
  return input.reduce(
    (count, {before, instruction: [opCode, a, b, c], after}) => {
      return Object.entries(operations).reduce((amount, [name, operation]) => {
        // slice.... don't forget that...
        const result = operation(before.slice(), [a, b, c]).join('');

        if (after.join('') === result) {
          if (!possibleOperationMapping.has(opCode)) {
            possibleOperationMapping.set(opCode, new Set());
          }

          let possibleNames = possibleOperationMapping.get(opCode).add(name);
          possibleOperationMapping.set(opCode, possibleNames);
        }

        return after.join('') === result ? amount + 1 : amount;
      }, 0) >= 3
        ? count + 1
        : count;
    },
    0
  );

  return count;
}

function day162(input) {
  let finalOperationMapping = new Map();

  while (possibleOperationMapping.size > 0) {
    for (let [opCode, names] of possibleOperationMapping.entries()) {
      if (names.size === 1) {
        finalOperationMapping.set(opCode, names.values().next().value);
      }
    }

    for (let name of finalOperationMapping.values()) {
      for (let [opCode, names] of possibleOperationMapping.entries()) {
        if (names.has(name)) {
          names.delete(name);
          names.size === 0 && possibleOperationMapping.delete(opCode);
        }
      }
    }
  }

  let registers = [0, 0, 0, 0];

  input.forEach(([opCode, a, b, c]) => {
    registers = operations[finalOperationMapping.get(opCode)](registers, [
      a,
      b,
      c
    ]);
  });

  return registers;
}

module.exports = {day161, day162};
