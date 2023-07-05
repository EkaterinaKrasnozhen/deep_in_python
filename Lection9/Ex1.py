from typing import Callable


#замыкание
# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
    
#     return add_two_str


# print(add_one_str('Hello')('world!')) #Hello world!

# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
#     return add_two_str


# hello = add_one_str('Hello') # на выходе функция, которая замкнула в себе Hello
# bye = add_one_str('Good bye')

# print(hello('world!')) #Hello world!
# print(hello('friend!'))#Hello friend!
# print(bye('wonderful world!'))#Good bye wonderful world!

# print(f'{type(add_one_str) = }, {add_one_str.__name__ = },{id(add_one_str) = }') #type(add_one_str) = <class 'function'>, add_one_str.__name__ = 'add_one_str',id(add_one_str) = 2628202705344
# print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')#type(hello) = <class 'function'>, hello.__name__ = 'add_two_str', id(hello) = 2628201496096
# print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')#type(bye) = <class 'function'>, bye.__name__ = 'add_two_str', id(bye) = 2628202706064


#  изменяемые списки

def add_one_str(a: str) -> Callable[[str], str]:
    names = []
    
    def add_two_str(b: str) -> str:
        names.append(b) # список накапливает
        return a + ', ' + ', '.join(names)
    
    return add_two_str


# hello = add_one_str('Hello') # списки names у каждого свои
# bye = add_one_str('Good bye')
# print(hello('Alex')) #Hello, Alex
# print(hello('Karina'))#Hello, Alex, Karina  
# print(bye('Alina'))#Good bye, Alina
# print(hello('John'))#Hello, Alex, Karina, John
# print(bye('Neo'))#Good bye, Alina, Neo

#неизменяемыми переменными str и число

def add_one_str(a: str) -> Callable[[str], str]:
    text = ''
    
    def add_two_str(b: str) -> str:
        nonlocal text # если сомневаемся можно и на изменяемые переменные писать, неизменяемые без этого не раюотают
        text += ', ' + b
        return a + text # либо join
    
    return add_two_str

hello = add_one_str('Hello')
bye = add_one_str('Good bye')

# print(hello('Alex')) # тот же результат
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))


def main(x: int) -> Callable[[int], dict[int, int]]:
    d = {}
    def loc(y: int) -> dict[int, int]:
        for i in range(y):
            d[i] = x ** i
        return d
    return loc

small = main(42) # замкнули в х 42,  
big = main(73)
print(small(7))# в loc положили 7 0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744}
print(big(7))
print(small(3)) # {0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744} вызов уже был и значения те же в словаре

# передача функции как объекта
