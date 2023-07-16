# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств

# Задание №5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.


class Rectangle():
    __slots__ = ('_length', '_width')
    
    
    def __init__(self, length, width = None):
        self._length = length
        if width == None:
            self._width = length
        else:
            self._width = width
        
    def perimeter(self):# периметр
       return (self._length + self._width) * 2
   
    def s(self):# площадь
        return self._length * self._width
    
    def __str__(self):#вывод
        return f'{self._length = } {self._width = }'
    
    def __add__(self, other):# +
        perim = self.perimeter() + other.perimeter()
        new_rect = Rectangle(perim / 2 / 2, perim / 2 / 2)
        return new_rect
    
    def __sub__(self, other):# -
        if self.perimeter() > other.perimeter():
            perim = self.perimeter() - other.perimeter()
        else:
            return f'Первый прямоугольник меньше или равен второму, их вычитание = 0'      
        new_rect = Rectangle(perim / 2 / 2, perim / 2 / 2)
        return new_rect
    
    def __eq__(self, other):# ==
        return self.perimeter() == other.perimeter()

    def __gt__(self, other):# >
        return self.perimeter() > other.perimeter()
    
    def __lt__(self, other):# <
        return self.perimeter() < other.perimeter()
    
    def __ge__(self, other):# >=
        return self.perimeter() >= other.perimeter()
    
    def __le__(self, other):# <=
        return self.perimeter() <= other.perimeter()
    
    @property
    def length(self): # названия сеттеров и геттеров не должны совпадать со свойствами экз
        return self._length
    
    @length.setter
    def length(self, value, min=0):
        if value > min:
            self._length = value      
        else:
            raise ValueError(f'Новая длина должна быть больше 0')
        
    @property
    def width(self): # названия сеттеров и геттеров не должны совпадать со свойствами экз
        return self._width
    
    @width.setter
    def width(self, value, min=0):
        if value > min:
            self._width = value      
        else:
            raise ValueError(f'Новая длина должна быть больше 0')
            

if __name__ == '__main__' :    
    my_rect = Rectangle(4, 3)
    print(my_rect.length)
    print(my_rect.width)
    my_rect.length = 10
    my_rect.width = 5
    print(my_rect.length)
    print(my_rect.width)
    print(Rectangle.__dict__)