# Время запуска кода в менеджере контекста;
# Время окончания работы кода;
# Сколько было потрачено времени на выполнение кода.


from datetime import datetime
import sys
from contextlib import contextmanager


@contextmanager
def timer():
    try:
        start = datetime.now()
        yield start
    finally:
        exc_type, exc_val, exc_tb = sys.exc_info()
        finish = datetime.now()
        execution = finish - start
        print(finish)
        print(execution)


def read_recipes():
    cook_book = {}
    with open("recipes.txt") as f:
        while True:
            dish_name = f.readline().strip()
            ingredient_list = []
            if not dish_name:
                break
            number_of_ingredients = f.readline().strip("\r\n").strip()
            if number_of_ingredients:
                int_number_of_ingredients = int(number_of_ingredients)
            for ingredient in range(int_number_of_ingredients):
                ingredient_list.append(f.readline().strip().split("|"))
            f.readline()


            ingr_list = []
            for ingr in ingredient_list:
                ingr_dict = {}
                ingr_dict["ingredient_name"] = ingr[0].strip()
                ingr_dict["quantity"] = ingr[1].strip()
                ingr_dict["measure"] = ingr[2].strip()
                ingr_list.append(ingr_dict)
            cook_book[dish_name] = ingr_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_recipes()
    dictionary_of_ingredients = {}
    for dish in dishes:
        try:
            for ingredient in cook_book.get(dish):
                if ingredient["ingredient_name"] not in dictionary_of_ingredients:
                    dictionary_of_measures = {}
                    dictionary_of_measures["measure"] = ingredient["measure"]
                    dictionary_of_measures["quantity"] = int(ingredient["quantity"]) * person_count
                    dictionary_of_ingredients[ingredient["ingredient_name"]] = dictionary_of_measures
                else:
                    dictionary_of_ingredients[ingredient["ingredient_name"]]["quantity"] = \
                    dictionary_of_ingredients[ingredient["ingredient_name"]]["quantity"] + int(
                        ingredient["quantity"]) * person_count
        except TypeError:
            print(f"У меня нет блюда {dish}")
    print(dictionary_of_ingredients)


with timer() as start:
    print(start)
    get_shop_list_by_dishes(["Фахтос", "Омлет"], 2)


