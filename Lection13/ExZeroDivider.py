def hundred_div_num(text: str = None) -> tuple[int, float]:
    while True:
        try:
            num = int(input(text)) # ошибка получения типа данных
            div = 100 / num # если делитель равено 0 = ошибка денения на 0
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'f'Попробуйте снова')
        except ZeroDivisionError as e: #  в высшей математике деление на 0 приводит к бесконечности
            div = float('inf') # равен бесконечности
            break
    return num, div

if __name__ == '__main__':
    n, d = hundred_div_num('Введите целый делитель: ')
    print(f'Результат операции: "100 / {n} = {d}"')
