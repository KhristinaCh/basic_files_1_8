from pprint import pprint

with open('recipes.txt', 'r', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        # print(dish_name)
        count = int(f.readline().strip())
        # print(count)
        list_of_ingredients = []
        for i in range(count):
            temp_dict = {}
            ingredient = f.readline().strip().split(' | ')
            temp_dict['ingredient_name'] = ingredient[0]
            temp_dict['quantity'] = ingredient[1]
            temp_dict['measure'] = ingredient[2]
            list_of_ingredients.append(temp_dict)
        # print(list_of_ingredients)
        cook_book[dish_name] = list_of_ingredients
        f.readline()


pprint(cook_book)