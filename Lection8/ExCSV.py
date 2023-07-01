# comma-seppreted-values
# для хранения табличных данных, обычно "текст" а числа 90 без ""
import csv

# чтение read
# with open('bio.csv', 'r', newline='') as f: # newline для правильного чтения
#     csv_file = csv.reader(f)
#     for line in csv_file:
#         print(line)#['Alex' '42' 'City']

# если хотим читать таблицы с симоволом табуляции, excel и получать цифры а не строки
# with open('bio.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC) # если в "" - строка, без = число
#     for line in csv_file:
#         print(line) #['Alex' 42.00 'City'] всегда вернет float
        
# запись write
# with (
#     open('bio.csv', 'r', newline='') as f_read,
#     open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
# ):
#     csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL) # не работает delimiter
#     all_data = []
#     for i, line in enumerate(csv_read):
#         if i == 0:
#             csv_write.writerow(line)
#         else:
#             line[2] += 1
#             for j in range(2, 4 + 1):
#                 line[j] = int(line[j])
#             all_data.append(line)
#     csv_write.writerows(all_data)

# чтение в словарь
# fieldnames - названия столбцов
# with open('bio.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex","age", "height", "weight", "office"], # поля офис в изначальной таблице нет, будем использовать restval = Main office
#                                 restkey="new", restval="Main Office", dialect='excel-tab', 
#                                 quoting=csv.QUOTE_NONNUMERIC) # если есть числа - получаем как числа
#     for line in csv_file:
#         print(f'{line = }')
#         print(f'{line["name"] = }\t{line["age"] = }') # получаем по ключу



# with open('bio.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", ], restkey="new", restval="Main Office", # если ячеек меньше указали в fieldnames - остальное попадет restkey
#                               dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line = }')
#         print(f'{line["name"] = }\t{line["age"] = }')

from typing import Iterator
with (
    open('bio.csv', 'r', newline='') as f_read,
    open('bio_new.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read: Iterator[dict] = csv.DictReader(f_read, fieldnames=["Name", "Sex", "Age", "Height (in)", "Weight (lbs)", "Office"], # поля офисе нет в изначальном файле и бдует = restival
                                            restval="Main Office", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.DictWriter(f_write, fieldnames=["id", "Name", "Office", "Sex", "Age", "Height", "Weight"],
                            dialect='excel-tab', quoting=csv.QUOTE_ALL) # заключить в кавычки все неважно текст или числа
    csv_write.writeheader() # записываем заголовки из  61 строки
    all_data = []
    for i, dict_row in enumerate(csv_read):
        if i != 0: # если не первая строка, тк это заголовок и его игнорируем
            dict_row['id'] = i
            #dict_row['age'] = int(dict_row['age'])
            dict_row['Age'] += 1 # не работает как int
            all_data.append(dict_row)
    csv_write.writerows(all_data)


