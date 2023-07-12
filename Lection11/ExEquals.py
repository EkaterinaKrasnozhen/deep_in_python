from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second
    
    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return _area

    def __lt__(self, other):
        return self.area() < other.area()

# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# four = Triangle(4, 3, 5)
# print(f'{one == two = }') #one == two = True
# print(f'{one == three = }')#one == three = True
# print(f'{one == four = }')#one == four = True
# print(f'{one != one = }')#one != one = False

one = Triangle(3, 4, 5)
two = Triangle(5, 5, 5)
print(f'{one} имеет площадь {one.area():.3f} у.е.²') #Треугольник со сторонами: 3, 4, 5 имеет площадь 6.000 у.е.²
print(f'{two} имеет площадь {two.area():.3f} у.е.²')# Треугольник со сторонами: 5, 5, 5 имеет площадь 10.825 у.е.²
print(f'{one > two = }\n{one < two = }')# one > two = False one < two = True

data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4),
Triangle(3, 5, 3)]
result = sorted(data)
print(*result)#Треугольник со сторонами: 3, 5, 3 Треугольник со сторонами: 6, 2, 5 Треугольник со сторонами: 3, 4, 5 Треугольник со сторонами: 4, 4, 4
print(', '.join(f'{item.area():.3f}' for item in result)) #4.146, 4.684, 6.000, 6.928