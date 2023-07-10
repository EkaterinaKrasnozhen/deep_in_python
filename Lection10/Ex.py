# наследование
class A:
    name = 'A'
    def call(self):
        print(f'I am {self.name}')

class B:
    name = 'B'
    def call(self):
        print(f'I am {self.name}')

class C:
    name = 'C'
    def call(self):
        print(f'I am {self.name}')

class D(C, A): # super() автоматически наследует первый C
    pass

class E(D, B):# super() автоматически наследует первый C
    pass

e = E()
e.call()#I am C
