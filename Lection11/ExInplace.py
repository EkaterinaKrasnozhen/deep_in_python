from decimal import Decimal
class Money:
    def __init__(self, value: int | float):
        self.value = Decimal(value)

    def __repr__(self):
        return f'Money({self.value:.2f})'
    
    def __imod__(self, other): # переопределили метод %
        self.value = self.value * Decimal(1 + other / 100)
        return self

m = Money(100)
print(m)#Money(100.00)
m %= 50
print(m)#Money(150.00)
m %= 100
print(m)#Money(300.00)
