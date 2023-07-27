from collections import namedtuple
from datetime import datetime
import time

# User = namedtuple('User', ['first_name', 'last_name', 'birthday'])# создаем класс
# u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))# указываем конкретную дату рождения
# print(u_1)

# print(f'{type(User)}, {type(u_1)}')
# print(u_1.first_name, u_1.birthday.year)#Исаак 1643

# User = namedtuple('User', ['first_name', 'last_name','birthday'], defaults=['Иванов', datetime.now()]) # фамилию и дату рождения ставим по умолчанию, default значения передадутся всем следующим экз класса
# u_1 = User('Исаак') # имя передаем как обязатлеьный параметр при создании
# print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')
# time.sleep(7)# задежржка в 7 сек
# u_2 = User('Галилей', 'Галилео')
# print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}') # новая дата рождения не созастся, а будет по default
# #Иванов, 12:06:35
# #Галилео, 12:06:35

# Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
# a = Point(2, 3, 4)
# b = a._replace(z=0, x=a.x + 4)# заменяем значения
# print(b)# Point(x=6, y=3, z=0)

# Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
# data = [Point(2, 3, 4), Point(10, -100, -500), Point(3, 7, 11),
# Point(2, 202, 1)]
# print(sorted(data))
# #[Point(x=2, y=3, z=4), Point(x=2, y=202, z=1), Point(x=3, y=7, z=11), Point(x=10, y=-100, z=-500)]
# # при сортировке сначала смотрим x, если х совпали - смотрим y

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
d = {
    Point(2, 3, 4): 'first',
    Point(10, -100, -500): 'second',
    Point(3, 7, 11): 'last',
}
print(d)
mut_point = Point(2, [3, 4, 5], 6)# в качестве y - список, изменеяемый тип данных, не возвращает хэш и не может быть ключом
print(mut_point)
d.update({mut_point: 'bad_point'}) # TypeError: unhashable type:'list'