# Course Assignment Deliverables

> [Lesson Link](https://www.boot.dev/lessons/c21bdb7e-e688-4c0c-84af-d0f9dd77e704)

**Complete the `check_ingredient_match function`.** It accepts two lists of strings:

- `recipe`: The list of ingredients needed.
- `inventory`: The list of ingredients the character has.

It should return two values:

- A float representing the percentage of required ingredients the character has.
- A new list of ingredients the character is missing but that are required.

Assume that the `recipe` list won't contain any duplicates (recipes require only one ingredient of each kind).

For example, if these were the lists:

```
recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
inventory = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]

percentage, missing_ingredients = check_ingredient_match(recipe, inventory)
print(percentage, missing_ingredients)
# Prints: 75.00 ["Unicorn Hair"]
```
