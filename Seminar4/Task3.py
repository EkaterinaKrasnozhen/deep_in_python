# * Функция получает на вход строку из двух чисел через пробел.
# * Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — его порядковый номер из диапазона, границами которого являются введенные числа.
# * Границы диапазона учитывать.

a, b = map(int, input('Введите два числа через пробел: ').split(' '))
my_dict = {}
max1 = 0
min1 = 0
if a > b:
    max1 = a
    min1 = b
else:
    max1 = b
    min1 = a
    
for i in range(min1, max1+1): # in range(min(a,b),max(a,b))
    my_dict.setdefault(chr(i), i) # my_dict[chr(i)] = i]
    
print(my_dict)