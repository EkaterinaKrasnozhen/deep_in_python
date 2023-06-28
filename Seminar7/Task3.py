# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

from pathlib import Path
import typing

def read_line(file: typing.TextIO):
    line = file.readline()
    if line == '':
        file.seek(0)
        line = file.readline()
    
    return line[:-1]

def my_func():
    my_list = [] # результат перемножения
    my_list_names = []
    with (
            open('1.txt', 'r', encoding='utf-8') as fnums,
            open('names.txt', 'r', encoding='utf-8') as fnames,
            open('res.txt', 'a', encoding='utf-8') as fres
    ):
    #     lines1 = len(f2.readlines())
        len1 = sum(True for _ in fnums)
        len2 = sum(True for _ in fnames)
        
        for _ in range(max(len1, len2)):
            names = read_line(fnames)
            nums = read_line(fnums)
        
    #     for line in f2:
    #         my_list.append(int(line.split('|')[0]) * float(line.split('|')[1][:-1]))
        
    #     lines2 = len(f1.readlines())
        
    #     for line in f1:
    #         my_list_names.append(line.replace('\n', '').split(' '))
    #     print(my_list_names)
    #     #while line := lines1:
    #         # for num in my_list:
    #         #     if num < 0:'
    #         #f3.write('\n'.join(str(c).lower(), n) for c in my_list_names for n in my_list if n < 0)
        
        
    # with open('1.txt', 'r', encoding='utf-8') as f2:
    #     for line in f2:
    #         my_list.append(int(line.split('|')[0]) * float(line.split('|')[1][:-1]))
            
    
    # with open('names.txt', 'r', encoding='utf-8') as f1:
    #     for line in f1:
    #         my_list_names.append(line.strip().split(' '))
    
    # # with open('result.txt', 'a', encoding='utf-8') as f3:
    # #     for line in f3:
    # #         my_list_names.append(line.replace('\n', '').split(' '))
    # print(my_list, my_list_names)
    # #result1 = [(str(c).lower().replace("[", "").replace("]", ""), n) for c in my_list_names for n in my_list if n > 0]
    # result1 = [tuple(filter(lambda c: str(c).lower(), my_list_names))], [tuple(filter(lambda x: x > 0, my_list))]
    # print(*result1)

my_func()