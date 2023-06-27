# файловая система

# f = open('1.txt', encoding='utf-8')
# print(f)
# print(list(f)) # ['"Hello world"конец\n', 'конец\n', 'конец\n']

# r - read, r+ = читаем и можем записывать в него, не стирает файл
# w - открыть для записи, предварительно очистив, w+  записываем файл и можем читать, сначала очистит потом запишет
# x - открыть, если файл уже существует вернет ошибку
# a - открыть для записи в конец файла, если он существует, добавляет как append, столько раз сколько вызовешь 
# b - в бинарном режиме, набор байтов
# t - текстовый режим, по умолчанию
# + = открыты для обновления (чиения и запись)

# f = open('1.txt', 'a', encoding='utf-8')
# f.write('конец\n')
# f.close()

# f = open('bin_data', 'wb', buffering=64) # режим буфферизации
# f.write(b'x' * 10)
# f.close()

# f = open('bin_data', 'r')
# print(list(f)) # ['xxxxxxxxxx']

# f = open('data.txt', 'wb') # с бинарными кодикровку тут не пишем
# f.write('Привет'.encode('utf-8') + 'мир'.encode('cp1251'))
# f.close()

# f = open('data.txt', 'r', encoding='utf-8', errors='replace') # указали что надо обрабатывать ошибки
# print(list(f)) # ['Привет���']
# f.close()

# with open('1.txt', 'r+', encoding='utf-8') as f1:
#     print(list(f1))# сам закроется

#в старых версиях пайтон    
# with open('1.txt', 'r', encoding='utf-8') as f2, \
#     open('bin_data', 'rb') as f3:
#     print(list(f2))#['"Hello world"конец\n', 'конец\n', 'конец\n']
#     print(list(f3))#[b'xxxxxxxxxx']
    
# в новых 3.10
# with (
#         open('1.txt', 'r', encoding='utf-8') as f2,
#         open('bin_data', 'rb') as f3
# ):
#     print(list(f2))
#     print(list(f3))

# read
# with open('1.txt', 'r', encoding='utf-8') as f2:
#     res = f2.read()
#     print(f'читаем первый раз\n{res}')
#     res = f2.read()
#     print(f'читаем второй раз\n{res}')# ничего, при повторном чтении пустую строку вернет
    
# SIZE = 10 # символов
# with open('1.txt', 'r', encoding='utf-8') as f2:
#     while res := f2.read(SIZE):
#         print(res)

# with open('1.txt', 'r', encoding='utf-8') as f:
#     while res := f.readline():
#         print(res) # между строками - пустая, изза \n в конце строки

# with open('1.txt', 'r', encoding='utf-8') as f2:
#     for line in f2:
#         #print(line, end="") # от начала строки до переноса, end= убирает пустую строку
#         #print(line[:-1]) # тоже убирает посл символ переноса
#         print(line.replace('\n', ''))# тоже
        



    








