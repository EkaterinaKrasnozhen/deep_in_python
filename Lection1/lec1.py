name = 'Alex'
age = None
a = 42

a = 'hello'
#print(id(a))# адрес в памяти
print(name, age, a, 'kate', sep=' !! ', end='&')
print('hey') # не передйет на другую строку из-за end=
res = input('Введите значение') #примет строковое значение от пользователя
print('вы ввели',res)
age = int(input('ск лет')) #тут число, если ввести не число будет ошибка
ADULT = 18 #без магических чисел и исправить только здесь
how_old = ADULT - age
print('до 18 осталось', how_old)
