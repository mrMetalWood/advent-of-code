const letters = [...Array(26)].map((_, index) =>
  String.fromCharCode(index + 65)
);

function prepareData(input) {
  const lines = input.split('\n');

  const instructions = lines.map(line => {
    return {
      step: line.substring(36, 37),
      before: line.substring(5, 6)
    };
  });

  return {instructions};
}

function getInitialAvailable(instructions) {
  const notAvailable = instructions.map(instruction => instruction.step);

  return instructions
    .filter(instruction => !notAvailable.includes(instruction.before))
    .map(instruction => instruction.before)
    .sort((a, b) => a.localeCompare(b));
}

function getNextAvailableSteps(instructions, nextStep, order) {
  return instructions
    .filter(instruction => {
      const hasAllPrerequisites = instructions
        .filter(i => i.step === instruction.step)
        .map(i => i.before)
        .every(prerequisites => order.includes(prerequisites));

      return instruction.before === nextStep && hasAllPrerequisites;
    })
    .map(instruction => instruction.step);
}

function day71(input) {
  const {instructions} = prepareData(input);
  const order = [];

  let available = getInitialAvailable(instructions);

  while (available.length) {
    available = [...new Set(available)];
    const nextStep = available.sort((a, b) => a.localeCompare(b)).shift();

    order.push(nextStep);
    available.push(...getNextAvailableSteps(instructions, nextStep, order));
  }

  return order.join('');
}

function day72(input, workerCount, additionalTime) {
  const {instructions} = prepareData(input);
  const letterNumber = letters.map((letter, index) => ({
    name: letter,
    value: index + 1
  }));

  let time = 0;
  let jobs = [];
  let jobsInProgress = false;
  const order = [];

  let available = getInitialAvailable(instructions);

  while (available.length || jobsInProgress) {
    available = [...new Set(available)];

    jobs = jobs.filter(job => {
      const isDone = job.doneAt <= time;

      if (isDone) {
        order.push(job.name);
        available.push(...getNextAvailableSteps(instructions, job.name, order));
      }

      return !isDone;
    });

    const nextSteps = available.sort((a, b) => a.localeCompare(b));

    let newJobCount = 0;
    nextSteps.forEach(step => {
      if (jobs.length < workerCount) {
        jobs.push({
          name: step,
          doneAt:
            time +
            additionalTime +
            letterNumber.find(letter => letter.name === step).value
        });

        jobsInProgress = true;
        newJobCount++;
      }
    });

    available.splice(0, newJobCount);

    if (jobs.length === 0) {
      jobsInProgress = false;
    }

    if (available.length || jobsInProgress) {
      time++;
    }
  }

  return time;
}

module.exports = {day71, day72};
