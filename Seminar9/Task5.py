# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from functools import wraps
import json
import os
from random import randint
from typing import Callable


def check(func: Callable):
    MIN = 1
    MAX = 101
    MAX_TRY = 10
    @wraps(func)
    def wrapper(*args):
        num, try_num = args
        if num not in range(MIN, MAX):
            num = randint(MIN, MAX+1)
            print(num)

        if try_num not in range(MIN, MAX_TRY):
            try_num = randint(MIN, MAX_TRY+1)
            print(try_num)
        
        print(f'Отгадайте число от {MIN} до {MAX-1} за {try_num} раз')
        func(num, try_num)
        
        return num, try_num    
    return wrapper


def cache_(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        result = func(*args, **kwargs)
        
        if os.path.exists(file_name):
            with open (file_name, 'r+', encoding="utf-8") as file:
                my_dict = json.load(file)
        else:
            my_dict = []
        
        for item in my_dict:
            print(f'{item=}')
        if args and kwargs not in my_dict:
            my_dict.append({
                'args': (args, kwargs),
                'result': result
                }) 

        with open(file_name, 'w', encoding='utf-8') as writer:
            json.dump(my_dict, writer, indent=1, ensure_ascii=False)
            
        return my_dict
    
    return wrapper

def count(num: int ):# для приема параметров
    def deco(func: Callable):# для приема функции
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = []
            result = func(*args, **kwargs)
            for _ in range(num):
                res.append(result)
            print(f'Результаты {res}')
            return result
        return wrapper
    return deco

@cache_
@count(3)
@check
def try_(num, try_num):
        count = 0
        
        while count < try_num: 
            user_num = int(input("Введите число от 1 до 100: "))
            if num == user_num:
                print('Вы отгадали')
                break   
            else:
                count += 1
                print('Вы не угадали')
        else: 
            print('число попыток исчерапно, до свидания') 
            
            
if __name__=="__main__":
    try_(5, 3)
