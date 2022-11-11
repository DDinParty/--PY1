import string
import random


def get_random_password(n=8) -> str:
    str_all = string.ascii_letters + string.digits
    password = "".join(random.sample(str_all, n, counts=None))
    return password


# TODO написать функцию генерации случайных паролей
print(get_random_password())
