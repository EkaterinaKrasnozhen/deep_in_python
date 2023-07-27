from datetime import datetime, timedelta

d = datetime.now()
td = timedelta(hours=1)# разница во времени 1 час
for i in range(24*7): # считает сколько часов до воскресенья
    if d.weekday() == 6:
        break
else:
    d = d + td


print(i)
