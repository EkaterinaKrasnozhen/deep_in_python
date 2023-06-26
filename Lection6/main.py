from super_module import * # секретные не импортируются если не указать в__all__ = ['func', '_secret'] 


print(f'{_secret}')

res = func(10, 20)#qwerty
print(res) #в диапазоне от 10 до 20 получили = 19

