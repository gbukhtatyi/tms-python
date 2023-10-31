import json

file = open("../input.json", encoding="utf-8")
raw_content = file.read()
file.close()
json_content = json.loads(raw_content)

print('''Задание 4
Необходимо сформировать geojson файл с координатами городов для одной страны. Формат geojson используется для 
хранения и обмена географическими данными в виде JSON.''')

geo = {
    "type": "FeatureCollection",
    "features": []
}

country_code = input('Введите код страны:').lower()
amount = 0
for city in json_content:
    if amount == 100:
        break

    if city['country'].lower() == country_code:
        geo['features'].append({
            "type": "Feature",
            "id": city['id'],  # Идентификатор берем из данных города
            "geometry": {
                "type": "Point",
                "coordinates": [
                    city['coord']['lon'],
                    city['coord']['lat']
                ],
            },
            "properties": {
                "description": city['name'],
                "iconCaption": city['name'],
                "marker-color": "#b51eff",
            }
        })
        amount += 1

with open("geo.json", "w", encoding="utf-8") as new_file:
    new_file.write(json.dumps(geo))
