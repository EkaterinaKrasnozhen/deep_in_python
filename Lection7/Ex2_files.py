import os
import shutil

from pathlib import Path

#os старая библиотека в старых проектах
# print(os.getcwd()) # C:\Users\медведь\Desktop\Обучение Python\Погружение в Python\Lection7
#Path новая
# print(Path.cwd()) # C:\Users\медведь\Desktop\Обучение Python\Погружение в Python\Lection7, curent werb dir

# os.chdir('../..') # перейти на каталог выше
# print(os.getcwd()) # C:\Users\медведь\Desktop\Обучение Python
# print(Path.cwd()) # C:\Users\медведь\Desktop\Обучение Python

# создание директорий в текущей раб области
# os.mkdir('Lection8')
# Path('Lection88').mkdir()

# создание директорий с некс уровнями вложенности
# os.makedirs('Lec7/Sem7/Files')
#Path('Lec77/Sem77/Files1').mkdir(parents=True)

# удаление
#os.rmdir('Lec77') # удалять по одной
#Path('Lec77/Sem77/Files1').rmdir() # тоже по одному из глубины? удаляется последний в записи
#shutil.rmtree('Lec77') # сразу весь каталог с папками внутри Sem77/Files1 

#пути к файлу

# file1 = os.path.join(os.getcwd(), 'Lection7', 'data.txt' ) # os.getcwd - текущая раб директория
# print(f'{file1=}') # file1='C:\\Users\\медведь\\Desktop\\Обучение Python\\Погружение в Python\\Lection7\\data.txt'
# file2 = Path().cwd() / 'Lection7' / 'data.txt'
# print(f'{file2=}') # file2=WindowsPath('C:/Users/медведь/Desktop/Обучение Python/Погружение в Python/Lection7/data.txt')

# обход и чтение
#print(os.listdir())#['.git', '.gitignore', 'Lection1', 'Lection2', 'Lection3', 'Lection4', 'Lection5', 'Lection6', 'Lection7', 'Seminar1', 'Seminar2', 'Seminar3', 'Seminar4', 'Seminar5', 'Seminar6']

# p = Path(Path.cwd())
# for obj in p.iterdir():
#     print(obj) # C:\Users\медведь\Desktop\Обучение Python\Погружение в Python\.git C:\Users\медведь\Desktop\Обучение Python\Погружение в Python\.gitignore ..


# dir_list = os.listdir()
# for obj in dir_list: # на выходе obj строка
#     print(f'{os.path.isdir(obj)=}')
#     print(f'{os.path.isfile(obj)=}')
#     print(f'{os.path.islink(obj)=}')
#     print(f'{obj=}')
# /Lection7/Ex2_files.py"
# os.path.isdir(obj)=False
# os.path.isfile(obj)=True
# os.path.islink(obj)=False
# obj='1.txt' = объекты строки   

# p = Path(Path().cwd()) 
# for obj in p.iterdir(): # на выходе obj это объект
#     print(f'{obj.is_dir()=}')
#     print(f'{obj.is_file()=}')
#     print(f'{obj.is_symlink()=}')
#     print(f'{obj=}')
    
# obj=WindowsPath('C:/Users/медведь/Desktop/Обучение Python/Погружение в Python/Lection7/1.txt')
# obj.is_dir()=False
# obj.is_file()=True
# obj.is_symlink()=False
# obj=WindowsPath('C:/Users/медведь/Desktop/Обучение Python/Погружение в Python/Lection7/new_text_data2.txt')  объекты это объекты со своими функция


# walk() os
# for dir_path, dir_name, file_name in os.walk(os.getcwd()): # в текущем каталоге
#     print(f'{dir_path=}, {dir_name=}, {file_name=}') # dir_path='C:\\Users\\медведь\\Desktop\\Обучение Python\\Погружение в Python\\Lection7', dir_name=[], file_name=['1.txt', 'bin_data', 'data.txt', 'Ex1.py', 'Ex2_files.py', 'new_text_data.txt', 'new_text_data2.txt']

# файловая система
# rename переименование

#os.rename('data.txt', 'renamed_data.txt')

# p = Path('renamed_data.txt') # сохранить промежучтоное значение в переменной
# p.rename('renamed2_data.txt')

# Path('renamed2_data.txt').rename('renamed3_data.txt')

# replace перенос

#os.replace('renamed3_data.txt', os.path.join(os.getcwd(), 'Example_dir', 'last_name.txt')) #возьми renamed3 из текущего каталога и перенеси в каталог Example (находится в текущем каталоге) и присовй новое имя last_name

# old_file = Path('last_name.txt')
# new_file  = old_file.replace(Path.cwd() / 'Ex2_dir' / old_file) # со старым именем перенос, нахожусь в каталоге где файл и можно переместить во внутр каталог

# copy, copy2 оригинал остается

# shutil.copy('1.txt','dir') # копирует без мета данных (например только фото без гео)
# shutil.copy2('last_name.txt', 'dir/one_more,txt') #скопировали и переименовали, с метаданными (например геометка с фото)

# shutil.copytree('dir1', 'copy_dir1') # все каталоги внутри также и файлы

# удаление
#os.remove('dir/some.txt')
# Path('dir/some.txt').unlink()

# for i in range(1, 2):
#     with open(f'file{i}.txt', 'w', encoding='utf-8') as f:
#         f.write('Hello')

# for i in range(1, 2, 1):
#     f = Path(f'file{i}.txt')
#     f.replace('new_dir' / f) # переместили в new_ir file1.txt
    
# shutil.rmtree('new_dir') # удалили директорию
