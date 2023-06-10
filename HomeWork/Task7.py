# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

number = int(input("введите число от 1 до 999: "))
numberType = ""
numberCounter0 = 10
numberCounter00 = 100
numberCounter000 = 1000
result = 0
if number // numberCounter0 == 0:
    numberType = "цифра"
    result = number * number
elif number // numberCounter00 == 0: #возможно надо было оставить 10, 100 и 1000 числами
    numberType = "двузначное число"
    result = (number%10) * (number//10)
elif number // numberCounter000 == 0:
    numberType = "трёхзначное число"
    num3 = (number%10) * numberCounter00
    number = number//10
    num2 = (number%10) * numberCounter0
    num1 = number//10
    result = num3 + num2 + num1
    
print(numberType, result)