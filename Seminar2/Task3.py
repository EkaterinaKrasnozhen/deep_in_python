#num = int(input("Введите целое число: "))
#print(bin(num), oct(num), hex(num))

#перевод в 2 и 8 систему

def degree(num, index):
    data = " "
    while num > 0:
        x = num % index
        data = str(x) + data
        num = num // index                                   
    return data

print(degree(19, 2))
