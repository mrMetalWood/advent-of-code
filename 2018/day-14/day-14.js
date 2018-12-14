function day14(requiredRecipes) {
  const elves = [{index: 0, recipe: 3}, {index: 1, recipe: 7}];
  const recipes = [3, 7];

  while (recipes.length <= requiredRecipes + 10) {
    const [elf1, elf2] = elves;

    const newRecipes = String(elf1.recipe + elf2.recipe)
      .split('')
      .map(Number);

    recipes.push(...newRecipes);

    elf1.index = (elf1.index + elf1.recipe + 1) % recipes.length;
    elf1.recipe = recipes[elf1.index];

    elf2.index = (elf2.index + elf2.recipe + 1) % recipes.length;
    elf2.recipe = recipes[elf2.index];
  }

  return recipes.slice(requiredRecipes, requiredRecipes + 10).join('');
}

function day142(requiredRecipes) {
  const elves = [{index: 0, recipe: 3}, {index: 1, recipe: 7}];
  const recipes = [3, 7];

  let newestRecipes = recipes.join('');

  while (newestRecipes.indexOf(requiredRecipes) === -1) {
    const [elf1, elf2] = elves;

    const newRecipes = String(elf1.recipe + elf2.recipe)
      .split('')
      .map(Number)
      .forEach(r => recipes.push(r));

    elf1.index = (elf1.index + elf1.recipe + 1) % recipes.length;
    elf1.recipe = recipes[elf1.index];

    elf2.index = (elf2.index + elf2.recipe + 1) % recipes.length;
    elf2.recipe = recipes[elf2.index];

    newestRecipes = recipes.slice(-10).join('');
  }

  return recipes.join('').indexOf(requiredRecipes);
}

module.exports = {day14, day142};
