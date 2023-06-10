data = [0,1,2,4,5,7,6]
num = int(input("введите число"))
if num in data:
    print("да")
elif num not in data: #отрицание not
    print("эх")
    
    
my_macth = input("2+2 = ")
# if 2 + 2 == my_macth:
#     print("да")
# else:
#     print("нет")

print("Верно" if 2 + 2 == my_macth else "нет") #тернарный оператор