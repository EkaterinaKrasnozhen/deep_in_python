#from super_module import * # секретные не импортируются если не указать в__all__ = ['func', '_secret'] 
from package import super_module1 as sm
import super_module

#print(f'{_secret}')

res = super_module.func 
print(res(3, 5)) # в диапазоне от 3 до 5 получили = 3
res2 = sm.divi(10,5)
print(res2) #2.0

