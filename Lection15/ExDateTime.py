from datetime import time, date, datetime
from datetime import timedelta


d = date(year=2007, month=6, day=15)

t = time(hour=2, minute=14, second=0, microsecond=24)

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,

second=0, microsecond=24)

print(f'{d = }\t-\t{d}')
print(f'{t = }\t-\t{t}')
print(f'{dt = }\t-\t{dt}')

# d = datetime.date(2007, 6, 15)  -       2007-06-15
# t = datetime.time(2, 14, 0, 24) -       02:14:00.000024
# dt = datetime.datetime(2007, 6, 15, 2, 14, 0, 24)       -       2007-06-15 02:14:00.000024

# в дате по умолчанию ничего нельзя поставить, время - по умолчанию будет 00 если не ставим
# = вывод в repr формате, вставим и получим тот же объект


delta = timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5,
milliseconds=6, microseconds=7)
print(f'{delta = }\t-\t{delta}')
#delta = datetime.timedelta(days=9, seconds=11045, microseconds=6007)    -       9 days, 3:04:05.006007

delta = timedelta(weeks=53, days=500, hours=73, minutes=101,
seconds=303, milliseconds=67890,
microseconds=1234567)
neg_delta = timedelta(days=-3, minutes=-42)
print(f'{delta = }\t-\t{delta}')
print(f'{neg_delta = }\t-\t{neg_delta}')
# delta = datetime.timedelta(days=874, seconds=10032, microseconds=124567)        -       874 days, 2:47:12.124567
# neg_delta = datetime.timedelta(days=-4, seconds=83880)  -       -4 days, 23:18:00


# пример с днем рождения
date_1 = datetime(2012, 12, 21)
date_2 = datetime(2017, 8, 19)
delta = date_2 - date_1
print(f'{delta = }\t-\t{delta}')
birthday = datetime(1503, 12, 14)
dlt = timedelta(days=365.25 * 33)
new_date = birthday + dlt
print(f'{new_date = }\t-\t{new_date}')
#new_date = datetime.datetime(1536, 12, 13, 6, 0)        -       1536-12-13 06:00:00

print('______') # работа с неизменяемыми объектами
d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
microsecond=24)
delta = timedelta(weeks=53, hours=73, minutes=101,
seconds=303, milliseconds=60)
print(f'{d.month}')
print(f'{t.second}')
print(f'{dt.hour}')
print(f'{delta.days}')

t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
microsecond=24)
new_dt = dt.replace(year=2012)
one_more_hour = t.replace(t.hour + 1)# изменяем
print(f'{new_dt}\n{one_more_hour}')

print('____') # начало времен 01.1970

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
microsecond=24)
print(dt)
print(dt.timestamp())
print(dt.isoformat())
print(dt.weekday())
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.')) # вывод в удобном формате

print('_____')
date_original = '2022-12-12 18:01:21.555470'
date_timestamp = 1181862840.000024
date_iso = '2007-06-15T02:14:00.000024'
date_text = 'Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.'
original_date = datetime.fromisoformat(date_original)
timestamp_date = datetime.fromtimestamp(date_timestamp)
iso_date = datetime.fromisoformat(date_iso)

text_date = datetime.strptime(date_text, 'Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.')# сложная строка с датой и временем
print(original_date)
print(timestamp_date)
print(iso_date)
print("___!___")
print(text_date)
