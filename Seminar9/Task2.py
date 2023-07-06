# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.
 
from random import randint
from typing import Callable


def check(func: Callable):
    MIN = 1
    MAX = 101
    MAX_TRY = 10
    
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




#@check # с синт сахаром
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
            
# if __name__ == '__main__': # с синт сахаром
#     try_(0, 0)
    
    
if __name__ == '__main__': # это без синт сахара
    res = check(try_)
    res(0, 0)