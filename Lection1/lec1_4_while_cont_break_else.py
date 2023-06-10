# num = float(input("введите число"))
# # count = 0
# # while count < num:
# #     print(count, end=',')
# #     count += 2
    
# STEP = 2
# limit = num -STEP
# count = - STEP
# while count < limit:
#     count += STEP
#     if count % 12 == 0:
#         continue #перебрасывает в начало цикла
#     print(count)


min_limit = 0
max_limit = 5
# while True: #бесконечный цикл
#     print('введи число между ', min_limit, 'и', max_limit )
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('неверно')
#     else:
#         break #прекращает цикл, переходим к 10 строке
# print('введено число', num)

count = 3
num = None #так как обьявляем ее внутри цикла, может не дойти до последнего принт, поэтому здесь none
while count > 0:
    print('осталось попыток', count)
    count -= 1
    
    print('введи число между ', min_limit, 'и', max_limit )
    num = float(input())
    if num < min_limit or num > max_limit:
        print('неверно')
    else:
        break #если внутри цикла срабатывает break, то else внутри цикла (39 строка) не срабатывает

else: #относится к while, на одном уровне
    print('попытки кончились')
    quit() # завершили программу, если передать код отличны от 0 - не успешно

print('введено число', num)