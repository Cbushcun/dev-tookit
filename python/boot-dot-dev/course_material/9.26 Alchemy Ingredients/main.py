# Submitted Solution

def check_ingredient_match(recipe, inventory):
    percentage = 0.00
    missing_ingredients = []
    for ingredient in recipe:
        if ingredient not in inventory: 
            missing_ingredients.append(ingredient)

    percentage = (1 - (len(missing_ingredients) / len(recipe))) * 100
    return percentage, missing_ingredients
