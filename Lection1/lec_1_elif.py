# color = input('кокой цвет?: ')
# if color =='красный': # выполняется жо первого совпадпения и дальше не выполняется
#     print('да красный')
# elif color == 'синий':
#     print('небо')
# elif color == 'зеленый':
#     print('травка')
# else: # если все ложь - выполняется else
#     print('no')

color = input('кокой цвет?: ')
match color:
    case'красный' | 'оранжевый': # | или
        print('да ярко')
    case 'синий':
        print('небо')
    case 'зеленый' | 'белый':
        print('травка')
    case _: #как else, ничего не совпало в python 3.10 и выше
        print('no')