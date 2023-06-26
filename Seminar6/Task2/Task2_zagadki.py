# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными верными 
# вариантами отгадок и количество попыток на угадывание.
# Функция возвращает номер попытки, с которой была отгадана загадка или ноль, 
# если попытки исчерпаны.

def get_info(text: str, list_: list, answer: str, count: int) -> int:
    ind = 1
    while count-1:
        if answer in list_:
            return ind
            break
        else:
            count -= 1
            answer = input("введите отгадку: ")
            
    else:
        return 0