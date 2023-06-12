#банкомат
# начальнас сумма = 0
# действия: пополнить, снять, выйти
# суммы пополнения и снятия кратны 50 у.е.
# процент за снятие 1.5% не менее 30 и неболее 600
# после каждой 3 операции снятия или поплнения начисляются проценты = 3%
# нельзя снять больше чем на счете
# если больше 5 млн - налог на богатство 10% перед каждой операцией, даже ошибочной
# любое действие выводит сумму денег

balance = 6000
def minus(summ, balance):
    percent = (balance / 100) * 1.5
    if 30 > percent:
        percent = 30
    elif percent > 600:
        percent = 600
    balance = balance - summ - percent
    print(balance)

def plus_(summ, balance):
    if balance > 5000:
        balance /= 10
    balance = float(balance + summ)
    print(balance)

def bye():
    print("До свидания")
    
def get_sum_50():
    user_summ = int(input("Введите сумму, кратную 50: "))
    if user_summ % 50 != 0:
        user_summ = int(input("Введите сумму, кратную 50: "))
    return user_summ
    
answer = input("Действия: 1 - Пополнить, 2 - Снять, 3 - Выход")

match answer:
    case "1":
        user_summ = int(input("Введите сумму, кратную 50: "))
        if user_summ % 50 == 0:
            plus_(user_summ, balance)
        else:
            user_summ = input("Сумма не кратна 50, повторите ввод: ")
            plus_(user_summ, balance)

    case "2":
        user_summ = int(input("Введите сумму, кратную 50: "))
        if user_summ % 50 == 0:
            minus(user_summ, balance)
        

    case "3":
        bye()