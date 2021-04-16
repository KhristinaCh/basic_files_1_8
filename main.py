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
            temp_dict['quantity'] = int(ingredient[1])
            temp_dict['measure'] = ingredient[2]
            list_of_ingredients.append(temp_dict)
        # print(list_of_ingredients)
        cook_book[dish_name] = list_of_ingredients
        f.readline()


# pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        # print(dish)
        if dish in cook_book:
            # print(dish)
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity'] * person_count)
                else:
                    temp_dict = {}
                    temp_dict['measure'] = ingredient['measure']
                    temp_dict['quantity'] = int(ingredient['quantity'] * person_count)
                    shop_list[ingredient['ingredient_name']] = temp_dict
    return pprint(shop_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
