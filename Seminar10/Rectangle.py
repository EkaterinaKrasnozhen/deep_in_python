# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle():
    def __init__(self, length, width = None):
        self.length = length
        if width == None:
            self.width = length
        else:
            self.width = width
        
    def perimeter(self):
       return (self.length + self.width) * 2 * self.length
   
    def s(self):
        return self.length * self.width


a = Rectangle(10)
b = Rectangle(10, 4)
print(a.perimeter(), a.s())
print(b.perimeter(), b.s())