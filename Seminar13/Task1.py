# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.


def get(text: str) -> int:
    while True:
        try:
            num = float(input(text))
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'f'Попробуйте снова')
        else:
            return num if num % 1 != 0 else int(num)


if __name__ == '__main__':
    number = get('Введите целое или вещественное число: ')
    print(f'{type(number)=}')