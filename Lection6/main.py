from super_module import * # секретные не импортируются если не указать в__all__ = ['func', '_secret'] 
from package import super_module1 as sm

print(f'{_secret}')

res = func(10, 20)#qwerty
print(res) #в диапазоне от 10 до 20 получили = 19
res2 = sm.divi(10,5)
print(res2) #2.0

