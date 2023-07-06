# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, 
# который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json
from typing import Callable
import os

def cache_(func: Callable):
    
    def wrapper(num, *args, **kwargs):
        file_name = func.__name__+ '.json'
        result = func(*args, **kwargs)
        
        if os.path.exists(file_name):
            with open (file_name, 'r+', encoding="utf-8") as file:
                my_dict = json.load(file)
        else:
            my_dict = []
        
        for item in my_dict:
            print(f'{item=}')
        if num and args and kwargs not in my_dict:
            my_dict.append({
                'args': (num, args, kwargs),
                'result': result
                }) 

        with open(file_name, 'w', encoding='utf-8') as writer:
            json.dump(my_dict, writer, indent=1, ensure_ascii=False)
            
        return my_dict
    
    return wrapper


#@check # с синт сахаром
@cache_
def get_any(num, *args, **kwargs):
    return num
            

if __name__ == '__main__': # с синт сахаром
    print(get_any(12, 5, 'эитото'))
    
    
# if __name__ == '__main__': # это без синт сахара
#     res = check(try_)
#     res(0, 0)