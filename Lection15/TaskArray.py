from collections import namedtuple

Data = namedtuple('Data', ['mathematics', 'chemistry', 'physics',
'genetics'], defaults=[5, 5, 5, 5]) # создаем класс Data и 4 свойства, значения по умолч 5 5 5 5

d = {
    'Ivanov': Data(4, 5, 3, 5),
    'Petrov': Data(physics=4, genetics=3), # можно менять местами если явно указать
    'Sidorov': Data(),
}

print(d) #{'Ivanov': Data(mathematics=4, chemistry=5, physics=3, genetics=5), 'Petrov': Data(mathematics=5, chemistry=5, physics=4, genetics=3), 'Sidorov': Data(mathematics=5, chemistry=5, physics=5, genetics=5)}