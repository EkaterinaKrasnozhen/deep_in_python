# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from random import choices, randint
import string


def create_file(extention, min_name=6, max_name=30, min_size=1, max_size=257, count=2):
    
    for _ in range(count):
        name = ''.join(choices(string.ascii_letters.lower(), k=randint(min_name, max_name)))
        with open(f'{name}.{extention}', 'wb') as f:
            f.write(b'x' * randint(min_size, max_size))
            

def create_diff_ext(**kwargs):
    for ext, num in kwargs.items():
        create_file(ext, count=num)


#create_diff_ext(txt=2)
#create_file('txt')    
    