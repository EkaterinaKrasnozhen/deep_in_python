d = {'42': 73}
try:
    key, value = input('Ключ и значение: ').split()
    if d[key] == value:
        r = 'Совпадение'
except ValueError as e:
    print(e)
except KeyError as e:
    print(e)
else:
    print(r)
finally:
    print(d)
    
# >>> Ключ и значение: 42 13 #print(r) NameError: name 'r' is not defined в r ничего не присвоится. и такую ошибку мы вообще не предусмотрели
# >>> Ключ и значение: 42 73 3 # too many values to unpack (expected 2) {'42': 73}
# >>> Ключ и значение: 73 42 # '73' {'42': 73}
# >>> Ключ и значение: 42 73 #   print(r) NameError: name 'r' is not defined

