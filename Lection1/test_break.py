data = 0
# while data < 100:
#     data +=2
#     if data %40 == 0:
#         break
# print(data) #40

while data < 100:
    data +=3
    if data % 40 == 0:# с шагом 3 не будет 40 или 80
        break

else: # когда будет 102, перейдем к else тк не сработал break
    data +=5

print(data) # 107