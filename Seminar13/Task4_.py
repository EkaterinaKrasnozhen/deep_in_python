import json


def add_user_to_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            my_dict = json.load(f)
    except Exception:
        my_dict = {str(level): {} for level in range(1, 8)}
        #print(f'{my_dict = }')
    
    while True:
        name, user_id, level, *_ = input("Введите имя, личный идентификатор, уровень доступа: ").split()
    # если идентификатора нет в ключах словаря, то добавляем пару {идентификатор : имя} в словарь
        
        try:
            if user_id not in my_dict:
                my_dict[level].update({user_id: name})
                break
            else:
                print('Идентификатор не уникален')
        except KeyError as e:
            print(f'Ошибка ввода уровня {e}')
        #print(f'{my_dict = }')
    
    with open(filename, "w", encoding="utf-8") as f:
    # записываем словарь в json-файл с отступом=1
        json.dump(my_dict, f, indent=1, ensure_ascii=False)
        

start = add_user_to_file('users.json')