import math
import decimal
# decimal - точность 28 знаков 

pi = float(3.123456678909877765655543322)
print(pi) #3.1234566789098777
pi2 = decimal.Decimal(3.123456678909877765655543322)
print(pi2) #3.123456678909877765655543322
decimal.getcontext().prec = 120 # символов
science = pi2 * 2 * decimal.Decimal(23.456) ** 2
print(science)

