import json

file = open("../input.json", encoding="utf-8")
raw_content = file.read()
file.close()
json_content = json.loads(raw_content)

print('''Задание 3
Подсчитать количество городов в северном полушарии и в южном.''')

south_amount = 0
north_amount = 0
for city in json_content:
    print(type(city['coord']['lat']))
    if city['coord']['lat'] < 0:
        south_amount += 1
    else:
        north_amount += 1

print('Количество городов в северном полушарии:', north_amount)
print('Количество городов в южном полушарии:', south_amount)
