import json

file = open("../input.json", encoding="utf-8")
raw_content = file.read()
file.close()
json_content = json.loads(raw_content)

print('''Задание 1
Определить количество городов в файле.''')

print('Количество городов в файле:', len(json_content))
