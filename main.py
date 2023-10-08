import requests
import json

heroes_list = ['Hulk', 'Captain America', 'Thanos']
# создадим словарь, в котором будет находиться информация о интеллекте каждого героя (изначально 0)
intelligence_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
response = requests.get(url)
data = response.json()
# print(data[1]['name'])
for i in data:
    if i['name'] in heroes_list:
        intelligence_dict[i['name']] =i['powerstats']['intelligence']

sorted_dict = sorted(intelligence_dict.items(), key=lambda x: x[1])

print(sorted_dict)
print('Самый умный это ', sorted_dict[-1][-2])

