class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __getattribute__(self, item):# обращение к атрибутам
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)
    
    def __setattr__(self, key, value): #установить атрибут
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):# обращение к несущ аттрибуту
        return None

    def __delattr__(self, item):# удалить артрибут
        if item in ('x', 'y'): # если значение которое хотим удалть лежит в х или у
            setattr(self, item, 0) # то просто заменяем его на 0
        else:
            object.__delattr__(self, item) # если не х у - то удаляем

a = Vector(2, 4)
b = Vector(3, 7)
# c = a + b
# print(f'{a = }\t{b = }\t{c = }')#a = Vector(2, 4)        b = Vector(3, 7)
# c = Vector(5, 11)

#print(a.z) # AttributeError: У нас вектор на плоскости, а не в пространстве
print(f'{a = }')#a = Vector(2, 4)

#print(a.z) # AttributeError: У нас вектор на плоскости, а не в пространстве
#a.z = 73 # AttributeError: У нас вектор на плоскости, а не в пространстве
a.x = 3
print(f'{a = }')#a = Vector(3, 4)
print(a.z) # None

a.s = 73
print(f'{a = }, {a.s = }')#a = Vector(3, 4), a.s = 73
del a.x
del a.s
print(f'{a = }, {a.s = }')#a = Vector(0, 4), a.s = None