# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.
class Range:        
    def __set_name__(self, owner, name):
        self.param_name = '_' + name # защищенное сохраняем
    
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name) # когда хотим прочитать свойство-  говорим прочитай и верни его

    def __set__(self, instance, value):
        self.validate(value) # внутр метод
        setattr(instance, self.param_name, value)
        
    def validate(self, value): # валидация
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if value < 0:
            raise ValueError(f'Значение {value} должно быть больше 0')
        
            
class Rectangle():
    
    #__slots__ = ('_length', '_width')
    _length = Range()
    _width = Range()
        
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
            raise ValueError(f'Новая длина должна быть больше {min}')
        

if __name__ == '__main__':
    new_rect = Rectangle(2, 3)
    print(new_rect)
    new_rect.length = -100
    print(new_rect)