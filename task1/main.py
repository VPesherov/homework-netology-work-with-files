import os
from pprint import pprint


def get_directory_with_recipes(folder_name, file_name):
    path = os.path.join(os.getcwd(), folder_name, file_name)
    return path


def create_cook_book(path):
    with open(path, 'rt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredients_count = int(file.readline())
            ingredients = []
            # print(dish_name)
            for _ in range(ingredients_count):
                dish = file.readline()
                ingredient_name, quantity, measure = dish.strip().split(' | ')
                dish_dict = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                }
                ingredients.append(dish_dict)
            file.readline()
            cook_book[dish_name] = ingredients
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    path = get_directory_with_recipes('text-files', 'recipes.txt')
    cook_book = create_cook_book(path)

    shop_dict = {}

    for dish in dishes:
        for key, value in cook_book.items():
            if key == dish:
                for val in value:
                    ingredient_name = val.get('ingredient_name')
                    quantity = val.get('quantity')
                    measure = val.get('measure')
                    if ingredient_name in shop_dict:
                        ingredient_info = shop_dict.get(ingredient_name)
                        ingredient_info['quantity'] += int(quantity)
                    else:
                        shop_dict[val.get('ingredient_name')] = {'measure': measure,
                                                                 'quantity': int(quantity) * person_count}

    return shop_dict


def main():
    shop_dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    pprint(shop_dict)


if __name__ == '__main__':
    main()
