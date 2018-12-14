function day121(state, spread, generations) {
  let value = 0;

  state = `${state}`.split('');
  let zeroPointer = 0;

  let oldvalue = 0;

  for (let i = 0; i < generations; i++) {
    while (state.slice(-3).join('') !== '...') {
      state.push('.');
    }

    while (state.slice(0, 3).join('') !== '...') {
      state.unshift('.');
      zeroPointer++;
    }

    const newState = [...Array.from({length: state.length}).map(pot => '.')];

    state.forEach((pot, index) => {
      if (state[index - 2] && state[index + 2]) {
        const toCheck = state.slice(index - 2, index + 3).join('');

        if (spread[toCheck]) {
          newState[index] = spread[toCheck];
        }
      }
    });

    state = newState;

    const newValue = state.reduce((sum, pot, index) => {
      if (pot === '#') {
        sum += index - zeroPointer;
      }

      return sum;
    }, 0);

    const total = oldvalue + (50000000000 - i) * (newValue - oldvalue);

    oldvalue = newValue;
  }

  value = state.reduce((sum, pot, index) => {
    if (pot === '#') {
      sum += index - zeroPointer;
    }

    return sum;
  }, 0);

  return value;
}

module.exports = {day121};
