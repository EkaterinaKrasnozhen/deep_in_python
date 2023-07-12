class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()
    
    # def __str__(self):
    #     """__str__ для вывода пользователю инф-ии об экземпляре"""
    #     return f'Экземпляр класса User с именем "{self.name}"'
    
    def __repr__(self):
        """для программиста - можно скопировать вывод, вставить в код и будет экземпляр"""
        return f'User({self.name})'


user = User('Спенглер')
print(user)#вывод __str__ Экземпляр класса User с именем "Спенглер" , вывод __repr__ User(Спенглер)
