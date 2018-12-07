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

function sortAlphabet(a, b) {
  return a.localeCompare(b);
}

function getInitialAvailable(instructions) {
  const notAvailable = instructions.map(instruction => instruction.step);

  return instructions
    .filter(({before}) => !notAvailable.includes(before))
    .map(({before}) => before)
    .sort(sortAlphabet);
}

function getNextAvailableSteps(instructions, currentStep, processedItems) {
  return instructions
    .filter(instruction => {
      const hasAllPrerequisites = instructions
        .filter(({step}) => step === instruction.step)
        .map(({before}) => before)
        .every(prerequisites => processedItems.includes(prerequisites));

      return instruction.before === currentStep && hasAllPrerequisites;
    })
    .map(({step}) => step);
}

function day71(input) {
  const {instructions} = prepareData(input);
  const processedItems = [];

  let available = getInitialAvailable(instructions);

  while (available.length) {
    available = [...new Set(available)];
    const currentStep = available.sort(sortAlphabet).shift();

    processedItems.push(currentStep);
    available.push(
      ...getNextAvailableSteps(instructions, currentStep, processedItems)
    );
  }

  return processedItems.join('');
}

function day72(input, workerCount, additionalTime) {
  const {instructions} = prepareData(input);
  const letterNumber = letters.map((letter, index) => ({
    name: letter,
    value: index + 1
  }));

  let time = 0;
  let jobs = [];
  let jobsInProgress = true;
  const processedItems = [];

  let available = getInitialAvailable(instructions);

  while (jobsInProgress) {
    available = [...new Set(available)];

    jobs = jobs.filter(job => {
      const isDone = job.doneAt <= time;

      if (isDone) {
        processedItems.push(job.name);
        available.push(
          ...getNextAvailableSteps(instructions, job.name, processedItems)
        );
      }

      return !isDone;
    });

    let newJobCount = 0;
    available.sort(sortAlphabet).forEach(step => {
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
    } else {
      time++;
    }
  }

  return time;
}

module.exports = {day71, day72};
