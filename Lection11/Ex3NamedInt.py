class NamedInt(int):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance
    
print('Создаём первый раз')
a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
# Создаём первый раз
# Создал класс <class '__main__.NamedInt'>

print('Создаём второй раз')
b = NamedInt(73, 'Лучшее просто число')
# Создаём второй раз
# Создал класс <class '__main__.NamedInt'>

print(f'{a = }\t{a.name = }\t{type(a) = }')#a = 42  a.name = 'Главный ответ жизни, Вселенной и вообще'      type(a) = <class '__main__.NamedInt'>
print(f'{b = }\t{b.name = }\t{type(b) = }')#b = 73  b.name = 'Лучшее просто число'  type(b) = <class '__main__.NamedInt'>

c = a + b
print(f'{c = }\t{type(c) = }')#c = 115 type(c) = <class 'int'>
