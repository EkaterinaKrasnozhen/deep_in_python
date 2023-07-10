class User:
    def __init__(self, name, phone, password):
        self.__name__ = name # магическая переменная, неверная запись
        self._phone = phone
        self.__password = password

u1 = User('One', '123-45-67', 'qwerty')
print(f'{u1.__name__ = }, {u1._phone = }, {u1._User__password =}') # неправильно обращаться к защищенной переменной
#u1.__name__ = 'One', u1._phone = '123-45-67', u1._User__password ='qwerty'