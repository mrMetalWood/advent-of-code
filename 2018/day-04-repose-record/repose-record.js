function getGuardMostAsleep(input) {
  const inputs = input.split('\n');
  let activeGuard = null;
  const guards = {};

  const events = inputs.map(event => {
    const guard = /(#)([0-9]+)/.exec(event);
    return {
      timestamp: new Date(event.substring(1, 17)).getTime(),
      guard: guard && Number(guard[2]),
      wakes: event.includes('wakes'),
      asleep: event.includes('asleep'),
      minutes: Number(event.substring(15, 17))
    };
  });

  events.sort((a, b) => a.timestamp - b.timestamp);

  events.forEach(event => {
    if (event.guard) {
      guards[event.guard] = guards[event.guard] || {
        minutesAsleep: 0,
        allMinutes: {}
      };
      activeGuard = event.guard;
    }

    if (event.asleep) {
      guards[activeGuard].asleep = event.minutes;
    }

    if (event.wakes) {
      for (let i = guards[activeGuard].asleep; i < event.minutes; i++) {
        guards[activeGuard].allMinutes[i] = guards[activeGuard].allMinutes[i]
          ? guards[activeGuard].allMinutes[i] + 1
          : 1;
      }
      guards[activeGuard].minutesAsleep =
        guards[activeGuard].minutesAsleep +
        event.minutes -
        guards[activeGuard].asleep;
      guards[activeGuard].asleep = 0;
    }
  });

  const guard = Object.entries(guards).sort((a, b) => {
    return b[1].minutesAsleep - a[1].minutesAsleep;
  })[0];

  const minute = Object.entries(guard[1].allMinutes).sort(
    (a, b) => b[1] - a[1]
  )[0];

  // const two = Object.entries(guards).map(guard => {
  //   console.log(
  //     guard[0],
  //     Object.entries(guard[1].allMinutes).sort((a, b) => b[1] - a[1])[0]
  //   );

  //   return {
  //     id: guard[0],
  //     allMinutes: Object.entries(guard[1].allMinutes).sort(
  //       (a, b) => b[1] - a[1]
  //     )[0]
  //   };
  // });

  // two.forEach(t => {
  //   // console.log(two.allMinutes);
  // });

  // console.log(
  //   two.sort((a, b) => {
  //     if (!b.allMinutes || !a.allMinutes) {
  //       return 0;
  //     }
  //     return Number(b.allMinutes[0]) - Number(a.allMinutes[0]);
  //   })[0]
  // );

  return {guard: Number(guard[0]), minutes: Number(minute[0])};
}
module.exports = {getGuardMostAsleep};
