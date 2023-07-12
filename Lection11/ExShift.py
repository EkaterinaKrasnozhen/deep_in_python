from random import choices
class Closet:
    CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка', 'перчатки', 'носки', 'туфли')
    def __init__(self, count: int, storeroom=None):
        self.count = count
        if storeroom is None:
            self.storeroom = choices(self.CLOTHES, k=count)
        else:
            self.storeroom = storeroom

    def __str__(self):
        names = ', '.join(self.storeroom)
        return f'Осталось вещей в шкафу {self.count}:\n{names}'
    
    def __rshift__(self, other): # сдвиг вправо
        shift = self.count if other > self.count else other 
        self.count -= shift
        return Closet(self.count, choices(self.storeroom, k=self.count))

storeroom = Closet(10)
print(storeroom)

for _ in range(4):
    storeroom = storeroom >> 3
    print(storeroom)

# Осталось вещей в шкафу 10:
# костюм, футболка, брюки, брюки, туфли, костюм, туфли, туфли, рубашка, брюки
# Осталось вещей в шкафу 7:
# рубашка, брюки, брюки, костюм, костюм, туфли, брюки
# Осталось вещей в шкафу 4:
# рубашка, рубашка, рубашка, костюм
# Осталось вещей в шкафу 1:
# костюм
# Осталось вещей в шкафу 0:
