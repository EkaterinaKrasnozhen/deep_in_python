year = int(input("введите год уууу"))
# if year % 4 != 0:
#     print("обычный")
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print("високосный")
#     else:
#         print("обычный")
# else:
#     print("Високосный")
    
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0: #несколько логических проверок, по pep8 так не надо, 
    #проверяет только до первой истины, если слева от and ложь то право не будет проверять
    print("обычный")
else:
    print("високосный")