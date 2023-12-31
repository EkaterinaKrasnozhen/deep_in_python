# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

names = ['Ivan', 'Serg', 'Petr']
salary = [1000, 2000, 3000]
awards = ['10.25%', '10.00%', '10.5%']

for name, salary, award in zip(names, salary, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary * float(award[:-1]) / 100 }') # в award исключаем последний символ

