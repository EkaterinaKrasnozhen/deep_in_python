# площадь круга и длина окружности по введенному диаметру
# точность вычисления не менее 42 знаков
import decimal

decimal.getcontext().prec = 42
pi  = 3.141592653589793238462643383279502884197169399375105820974
d = 100

s = (d**2) / (4 * decimal.Decimal(pi))
l = pi * d
print(decimal.Decimal(s), decimal.Decimal(l))
