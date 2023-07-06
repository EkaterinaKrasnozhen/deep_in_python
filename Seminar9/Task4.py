# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.


from typing import Callable

num = 2

def count(num: int ):# для приема параметров

    def deco(func: Callable):# для приема функции
        def wrapper(*args, **kwargs):
            res = []
            result = func(*args, **kwargs)
            for _ in range(num):
                res.append(result)
            print(f'Результаты {res}')
            return result
        return wrapper
    return deco


@count(num)
def get_any(num, *args, **kwargs):
    return num


if __name__ == "__main__":
    get_any(10, 'get', 'сущность')