class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name: str):
        self.name = name

a = Singleton('Первый')
print(f'{a.name = }')#a.name = 'Первый'

b = Singleton('Второй')
print(f'{a is b = }')#a is b = True
print(f'{a.name = }\n{b.name = }')#a.name = 'Второй' b.name = 'Второй'