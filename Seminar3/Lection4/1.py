# функции

# дискриминант
def quadric_(a: int | float, b: int | float, c: int | float) -> tuple[float | float] | float | None:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-d + b ** 0.5) / (2 * a), (-d - b ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    # else: пайтон сам вернет none
    #     return None
    
print(quadric_(2, -3, -9))

# изменяемые и неизменяемые

# передаем неизменяемый объект и он не изменится
def no_mutable(a: int) -> int:
    a += 1
    print(f'{a=}') #внутри функции меняется a =43
    return a
    
a = 42 # разные объекты
print(f'{a=}')
z = no_mutable(a)
print(f'{z=} {a=}') # а не изменяется z=43 a=42

#если передаем изменяемый объект (список) то он и изменится в исходных данных
def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'в функции {data=}')#в функции data=[2, 3, 4, 5]
    return data

my_list = [1, 2, 3, 4]
print(f'{my_list=}')#my_list=[1, 2, 3, 4]
res = mutable(my_list)
print(f' результат после функции {res=} изначальный список {my_list=}')#результат после функции res=[2, 3, 4, 5] изначальный список my_list=[2, 3, 4, 5]

#значения по умолчанию
def quadric_2(a, b=0, c=0):# пробелы при установки по умолчанию не ставят
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-d + b ** 0.5) / (2 * a), (-d - b ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    
print(quadric_2(2, -9)) # для с = 0

def from_to(n, data=None): #None не изменяемый, если поставить пустой список[], мы все время будем добавлять в старый список при каждом вызове функции, тк список изменяемый
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data

first_list = from_to(5) # [1, 2, 3, 4, 5]
second_list = from_to(7) # [1, 2, 3, 4, 5, 6, 7], если не сделать None  то списки объединяться
third_list = from_to(8,[1,3,4,8]) # [1, 3, 4, 8, 1, 2, 3, 4, 5, 6, 7, 8]
print(first_list, second_list, third_list)

# ключевые и позиционные параметры

def standard_arg(arg):
    print(arg)

standard_arg(42) # 42, позиционное знаячение, попадает в первую позицию
standard_arg(arg=42) # 42, ключевой стиль, попадает по ключу arg

def standard_arg2(arg, /): #первая переменная только позиционная, нельзя по ключу
    print(arg)

standard_arg2(43)# 43
#standard_arg2(arg=42)#TypeError: standard_arg2() got some positional-only arguments passed as keyword arguments: 'arg'

def key_only(*, arg): # только ключевая функция
    print(arg)

#если до этого вызова будет ошибка - код остановится    
key_only(arg=70)#70

def combined(pos_only, /, standard, *, key_only):
    print(pos_only, standard, key_only)
    
combined(1, 2, key_only=3)#1 2 3
combined(1, standard=2, key_only=3)#1 2 3

# *args **kwargs - можно назвать по другому, но лучше так, *args - любое число позиционных аргументов, **kwargs - любое число ключевых
# если оба варианта: все позиционные *args - попадают в кортеж, все ключевые **kwargs - в словарь

def mean(args):
    return sum(args)/ len(args)

print(mean([1, 2, 3])) # 2.0, список как одна переменная
#print(mean(1,2,3))#TypeError: mean() takes 1 positional argument but 3 were given

def mean2(*args):
    return sum(args)/ len(args)

print(mean2(*[1, 2, 3]))#2.0
print(mean2(1, 2, 3))#2.0

def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f'предмет {key} оценка {value}')
        
school_print(химия=5, русский=3)#предмет химия оценка 5 предмет русский оценка 3

#области видимости

#локальные переменные
def func(y: int) -> int:
    x = 100
    print(f'in func {x=}')
    return y+1

x = 42
print(f'main {x=}')#main x=42
z = func(x)
print(f'после функции {z=} {x=}') # после функции z=43 x=42

# глобальные переменные 

# def func2(y: int) -> int:
#     global x
#     x += 100
#     print(f'in func {x=}') #in func x=142
#     return y+1

# x = 42
# print(f'in main {x=}') #in main x=42
# z = func2(x)
# print(f'после функции {x=} {z=}') #после функции x=142 z=43

# не локальные переменные

def main(a):
    c = 1 # меняем этот с
    def func3(y): # вышли из функции на 1 уровень и увидели с = 1
        nonlocal c
        c += 300 # прибаивили 1 + 300
        print(f' in func {c=}') #in func c=301
        return y+1
    return c + func3(a)

c = 3 # этот с не меняется
print(f' in main {c=}') # in main c=3
z = main(c)
print(f'после функции {c=} {z=}') # после функции c=3 z=5 ( c= 1 + y+1 (2), 3 + func(было внутри 2) = 5)

# константы
LIMIT = 1000

def funct(x, y):
    res = x ** y % LIMIT # обратились к внешней переменной, неизменяемый тип
    return res

print(funct(42, 73)) # 112

#lambda анонимная функция

def add_two(a, b):
    return a + b

add_2 = lambda a, b: a + b # lambda анонимная функция и присваивать неправиьно

print(add_two(3, 6))#9
print(add_2(3, 6))#9

my_dict = {'two': 2, 'one': 1, 'four': 4}
sort_key = sorted(my_dict.items())
sort_value = sorted(my_dict.items(), key=lambda x : x[1]) # x = пара ключ[0] значения[0], сортировка по первому значению
print(f'{sort_key=} {sort_value=}') #sort_key=[('four', 4), ('one', 1), ('two', 2)] sort_value=[('one', 1), ('two', 2), ('four', 4)]


#документирование функций

def max_before_100(*args):
    """Возвращает макс число до 100.
    :param args: tuple of int or float
    :return: int or float from the tuple
    """
    m = float('-inf')
    for item in args:
        if m < item < 100:
            m = item
    return m

print(max_before_100(99, 250, -10)) # 99
help(max_before_100) # выведет описание, функцию пишем без кавычек в конце

#map func iterable, принимает функцию и последовательность
txt = ['привет', 'Здрав', 'привЕтикии']
res = map(lambda x: x.lower(), txt) # принимает значение х и вызывает lower
print(*res) # привет здрав приветикии * - распаковать объект

#filter func iterable
num = [-42, 6, 1020]
res = tuple(filter(lambda x: x > 0, num)) # проверяем х >0, чтобы не писать * в принте оборачиваем tuple
print(res) # (6, 1020)

#zip
names = ['Катя', 'Паша', 'Чун']
salaries = [1000, 2000, 20]
awards = [0.2, 0.5, 0.1, 0.09] #0.09 будет проигнорировано
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}') #2f 2 знака после .
    
#max(iterable, *[, key, default]) or (arg1, arg2, *args[, key])
lst1 = []
lst2 = [42, 34, 5]
lst3 = [('Иван', 100000), ('Петр', 2000), ('Вася', 9000000)]
print(max(lst1, default='empty')) # empty указываем сами что вернуть по умочанию
print(max(*lst2))#42
print(max(lst3, key=lambda x: x[1])) # ('Вася', 9000000) ищем по значению x[1] где самя высокая

#min()

print(min(lst1, default='empty')) # empty указываем сами что вернуть по умочанию
print(min(*lst2))#5
print(min(lst3, key=lambda x: x[1])) # ('Петр', 2000)

#sum(iterable, /, start=0)
print(sum(lst2))# 81
print(sum(lst2, start=1000))#1081 просуммировать + start

#all(iterable)


def all_(iterable): # если бы писали сами и не существовало
    for elem in iterable:
        if not elem:
            return False
    return True


nums = [1, -54, 34, 76] # есть отрицательные или 0
if all(map(lambda x: x > 0, nums)):
    print('все эелементы положительные')
else:
    print('есть отрицательные или 0')
    
#any(iterable)


def any_(iterable): # пример самописной any
    for elem in iterable:
        if elem:
            return True
    return False


if any(map(lambda x: x > 0, nums)): # хотя бы один положительный
    print('хотя бы один положительный')
else:
    print('все элементы не больше 0')
    

#chr - принимает целое число до 10014111 и возращает символ
print(chr(1105))#ё

#ord - по символу вернет код
print(ord('ё'))#1105