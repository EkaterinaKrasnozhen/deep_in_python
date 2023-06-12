# простые типы данных
# txt = "Hello Kate"
# print(txt, id(txt))
# txt = txt.replace(" ", "+")
# print(txt, id(txt))

# x = 1
# y = "zdf"
# z = 3.14
# print(hash(x), hash(y), hash(z)) # неизменяемые объекты
#a = [x , y, z]
#print(hash(a)) unhashable type: 'list' нельзя получить hash изменяемого объекта list

# string = input("Введите текст: ")
# print(type(string), id(string), hash(string)) #тип , адрес в оперативной памяти, хеш

#аннотация типов данных
# a: int = 42
# b: float = float(input("ddtlbnt xbckj"))


# def my_func(data: list[int, float]) -> float: # хочу получать инт и флоат, -> на выходе флоат
#     res = sum(data) / len(data)
#     return res

# print (my_func([2, 3.5, 7.1, 5, 13.6]))

# a: int | float = 42
# b: float = float(input("введите вещественное число: "))
# a = a / b
# print(a)

#объект, его атрибуты и методы

# print("Hello".__doc__ ) # дандер метод
# print("Hello".upper())
# print("Hellp".count("l"))

# print(dir("hekko")) # посмотреть доступные методы
# help(str)

#help() # запускаем и узнаем справку

# простые объекты
# x = int("43") #42
# y = int(3.14)#3
# z = int("hello", base=30)#14167554
# print(x, y, z, sep="\n") #разделительновая строка

# for _ in range(10): # когда не нужна переменная 
#     print("+", end=",")
    
# num = 1_343_500 #для удобства разделитель на печать не идет
# print(num)
# b = bin(num)
# o = oct(num)
# h = hex(num)
# print(b, o, h) #строковые объекты

# вещественные числа - обрезает большие числа, не высокая точность

# логические типы = 0 это ложь для python
# DEFAULT = 42
# num = 0 # если не 0 -> выведет num тк or ленивый
# level = num or DEFAULT 
# print(level)#42

# name = input("введите имя: ")
# if name: # не пустая строка - истина
#     print("Привет, " + name)
# else: #пустая строка ложь
#     print("Привет, аноним")
    
data = [1, 2, 3, 0]
while data: # список не пуст
    print(data.pop())
    
#строки и способы их записи
txt = "строка 'z ybb'"
print(txt)

#описание документации
class str(object):
    """
    str(object) = string
    ...
    """

# длинная строка 0   \ не вместилось на одну строку 
# t = """
#     str(object) = string\ \
#     порлрлдждэдэдэдэдээжэдэдээдэдэдэдэдэдэдээ\
#     ...
#     """
# print(t)


txt = input("Введите число: ")
if txt.isdigit(): #если число
    print(bin(int(txt)), oct(int(txt)), hex(int(txt)))
else:
    if txt.isascii(): # если латиница
        print(txt.isascii())
    else:
        print("не латинские")
