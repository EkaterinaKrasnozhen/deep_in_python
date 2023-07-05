from functools import wraps
from typing import Callable
import time

def count(num: int = 1):# для приема параметров
    def deco(func: Callable):# для приема функции
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result
        return wrapper
    return deco


@count(3)
def factorial(n: int) -> int:
    """returns произведение чисел от 1 до N
    """
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print(f'{factorial(3)=} {factorial.__name__=}') #Результаты замеров [6.6999346017837524e-06, 2.9001384973526e-06, 2.200016751885414e-06] 
#factorial.__name__='factorial' - не декоратор как без @wraps
help(factorial)
#factorial(n: int) -> int
#   returns произведение чисел от 1 до N#