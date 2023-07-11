# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь
import math 

class Circle(): 
    def __init__(self, radius):
        self.radius = radius
       
    
    def length(self):
        return math.pi * 2  * self.radius
        
    def square(self):
        return math.pi  * self.radius**2

a = Circle(7)
print(a.length())
print(a.square())