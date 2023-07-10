class User:
    count = [] # общий для всех, поэтому обЪединяется
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        # если сделать тут count - то будет у каждого свой
        
u1 = User('One', '123-45-67')
u2 = User('NoOne', '76-54-321')
u1.count.append(42)
u1.count.append(73)
u2.counter = 256
u2.count.append(u2.counter)
u2.count.append(u1.count[-1])
print(f'{u1.name = }, {u1.phone = }, {u1.count = }') #u1.name = 'One', u1.phone = '123-45-67', u1.count = [42, 73, 256, 256]
print(f'{u2.name = }, {u2.phone = }, {u2.count = }')# u2.name = 'NoOne', u2.phone = '76-54-321', u2.count = [42, 73, 256, 256]