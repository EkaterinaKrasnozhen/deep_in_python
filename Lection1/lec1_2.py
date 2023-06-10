pwd = 'text'
res = input('password: ')
if res == pwd:
    my_match = int(input('2+2 = '))
    if 2+2 == my_match: #разная вложенность
        print('ура')
    else:
        print('эх')
    print ('доступ разрешен')
else:
    print('доступ нет')