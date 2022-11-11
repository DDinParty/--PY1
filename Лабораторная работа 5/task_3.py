from random import randint


def get_unique_list_numbers() -> list[int]:
    set_list = {randint(-10, 10) for _ in set(range(15))}
    while len(set_list) < 15:
        set_list = {randint(-10, 10) for _ in set(range(15))}
        list_ = list(set_list)
    return list_


# TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
