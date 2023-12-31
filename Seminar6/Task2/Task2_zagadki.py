# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными верными 
# вариантами отгадок и количество попыток на угадывание.
# Функция возвращает номер попытки, с которой была отгадана загадка или ноль, 
# если попытки исчерпаны.

# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, из предыдущей задачи, чтобы передать ей все свои загадки.

# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, 
# с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

import random as rnd

def get_info(txt: str, list_: list, ind=3) -> int:
    count = 1
    print(f'Напишите отгадку: {txt}')
    #count = int(input(' Введите количество попыток: '))
    
    while count < ind:
        answer = input('Введите отгадку').lower()
        if answer in list_:
            print(f'отгадали с {count}')
            return count
        else:
            print('Не отгадали')
            count += 1
        
        if count == ind:
            print('попыток больше нет')
            return 0
    
def ridd_dic():
    my_dict = {'висит шруша нельзя скушать': ['лампочка', 'Лампочка'],
        'зимой и летом одни цветом': ['елка', 'ель', 'елочка', 'ёлка'],
        'сто одежек и все без застежек': ['капуста'],}
    for key, value in my_dict.items():
        res_(key, get_info(key, value))


def res_(text, count):
    __res[text] = count
       
def show_res_dict():
    output = '\n'.join([f'Отгадали загадку {key} за {value} раз' for key, value in __res.items()])
    print(output)
     
__res = {}
        
    
    
    
