import json

file = open("../input.json", encoding="utf-8")
raw_content = file.read()
file.close()
json_content = json.loads(raw_content)

print('''Задание 2
Создать словарь, где ключ — это код страны, а значение — количество городов.''')

result = {info['country']: info['name'] for info in json_content}

print('Словарь:', result)
