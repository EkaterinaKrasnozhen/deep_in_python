class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):# можем читать скрытые имена но не менять
        return self._name


user = User('Стивен')
print(f'{user.name = }')#user.name = 'Стивен'
user.name = 'Славик' # AttributeError: can't set attribute'name'
