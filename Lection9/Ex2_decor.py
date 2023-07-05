import time 
from typing import Callable
import random

# def main(func: Callable):
    
#     def wrapper(*args, **kwargs):
        
#         print(f'Запуск функции {func.__name__} в {time.time()}')
#         result = func(*args, **kwargs)
#         print(f'Результат функции {func.__name__}: {result}')
#         print(f'Завершение функции {func.__name__} в {time.time()}')
#         return result
    
#     return wrapper


# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f


# print(f'{factorial(10) = }')#factorial(10) = 3628800
# control = main(factorial)
# print(f'{control.__name__ = }')#control.__name__ = 'wrapper'
# print(f'{control(10) = }')#control(10) = 3628800


# def main(func: Callable):
    
#     def wrapper(*args, **kwargs):
        
#         print(f'Запуск функции {func.__name__} в {time.time()}')
#         result = func(*args, **kwargs)
#         print(f'Результат функции {func.__name__}: {result}')
#         print(f'Завершение функции {func.__name__} в {time.time()}')
#         return result
    
#     return wrapper

# @main # благодаря @ наша функция превращается в декорированную и выведет все с учетом декорирования выше в main
# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f

# print(factorial(10))
# Запуск функции factorial в 1688545594.9840994
# Результат функции factorial: 3628800
# Завершение функции factorial в 1688545594.9840994
# 3628800


# def deco_a(func: Callable):
#     def wrapper_a(*args, **kwargs):
#         print('Старт декоратора A')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора A')
#         return res
#     print('Возвращаем декоратор A')
#     return wrapper_a

# def deco_b(func: Callable):
#     def wrapper_b(*args, **kwargs):
#         print('Старт декоратора B')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора B')
#         return res
#     print('Возвращаем декоратор B')
#     return wrapper_b

# def deco_c(func: Callable):
#     def wrapper_c(*args, **kwargs):
#         print('Старт декоратора C')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора C')
#         return res
#     print('Возвращаем декоратор C')
#     return wrapper_c

# @deco_c
# @deco_b
# @deco_a
# def main():
#     print('Старт основной функции')
    
# main()
#Возвращаем декоратор A - декораторы даже раньше функции, пайтон включает их единожды до вызова функции
# Возвращаем декоратор B
# Возвращаем декоратор C
# Старт декоратора C - декораторы стартуют сверху вниз
# Запускаю wrapper_b
# Старт декоратора B
# Запускаю wrapper_a
# Старт декоратора A
# Запускаю main
# Старт основной функции
# Завершение декоратора A
# Завершение декоратора B
# Завершение декоратора C

def cache(func: Callable):
    _cache_dict = {}
    
    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]
    return wrapper


@cache
def factorial(n: int) -> int:
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


# print(f'{factorial(10) = }')
# print(f'{factorial(15) = }')
# print(f'{factorial(10) = }') # повторно функция не вычисляет, так в словаре в декораторе уже хранится значение
# print(f'{factorial(20) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')

# # Вычисляю факториал для числа 10
# # factorial(10) = 3628800
# # Вычисляю факториал для числа 15
# # factorial(15) = 1307674368000
# # factorial(10) = 3628800
# # Вычисляю факториал для числа 20
# # factorial(20) = 2432902008176640000
# # factorial(10) = 3628800
# # factorial(20) = 2432902008176640000

# import random
# from typing import Callable
# def cache(func: Callable):
#     _cache_dict = {}
    
#     def wrapper(*args):
#         if args not in _cache_dict:
#             _cache_dict[args] = func(*args)
#         return _cache_dict[args]
    
#     return wrapper

# @cache
# def rnd(a: int, b: int) -> int:
#     return random.randint(a, b)

# print(f'{rnd(1, 10) = }')
# print(f'{rnd(1, 10) = }')
# print(f'{rnd(1, 10) = }')
# rnd(1, 10) = 9 вернет одно и тоже, так как наши параметры 1 9 и уже записаны в словарь как ключи  и значение тоже записано
# rnd(1, 10) = 9
# rnd(1, 10) = 9

# декораторы с параметрами

# def count(num: int = 1):# для приема параметров
#     def deco(func: Callable):# для приема функции
#         def wrapper(*args, **kwargs):
#             time_for_count = []
#             result = None
#             for _ in range(num):
#                 start = time.perf_counter()
#                 result = func(*args, **kwargs)
#                 stop = time.perf_counter()
#                 time_for_count.append(stop - start)
#             print(f'Результаты замеров {time_for_count}')
            
#             return result
#         return wrapper
#     return deco


# @count(10) # попадет 10 в num
# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f


# #print(f'{factorial(10) = }')
# # Результаты замеров [9.400071576237679e-06, 4.800036549568176e-06, 3.90014611184597e-06, 3.400025889277458e-06, 3.500143066048622e-06, 3.400025889277458e-06, 3.4999102354049683e-06, 3.5997945815324783e-06, 3.400025889277458e-06, 3.600027412176132e-06]
# # factorial(10) = 3628800

# print(f'{factorial(10) = }')

def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter # данный декоратор изменяет работу фуне=кции, возвращет не ее работу а свой список
        return wrapper
    return deco


@count(10)
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)

print(f'{rnd(1, 10) = }')
print(f'{rnd(1, 100) = }')
print(f'{rnd(1, 1000) = }')

# rnd(1, 10) = [7, 7, 2, 2, 6, 1, 5, 2, 2, 7] список из 10 (count10)
# rnd(1, 100) = [7, 7, 2, 2, 6, 1, 5, 2, 2, 7, 61, 61, 45, 26, 15, 3, 94, 51, 32, 14] из 20 тк уже было 10 ранее
# rnd(1, 1000) = [7, 7, 2, 2, 6, 1, 5, 2, 2, 7, 61, 61, 45, 26, 15, 3, 94, 51, 32, 14, 508, 750, 864, 146, 13, 145, 292, 850, 568, 159] из 30 и тд
