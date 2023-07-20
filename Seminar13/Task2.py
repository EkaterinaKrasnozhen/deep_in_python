# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

dict1 = {1: 'один', 2: 'два'}


def get_key(dictionary, key, default_value):
    try:
        res = dictionary[key]
        return res
    except KeyError:
        return default_value
    

res = get_key(dict1, 5, None)
print(res)