# Задача №1. Кто самый умный супергерой?

import requests

def get_resourse(link):
    resp = requests.get(link)
    return resp.json()

def smartest_super(names, url):
    base_super = get_resourse(url)
    dict_supers = {}
    for i in range(len(base_super)):
        current_dict = base_super[i]
        for name in names:
            if current_dict['name'] == name:
                dict_supers.setdefault(current_dict['name'], current_dict["powerstats"]["intelligence"])
    return max(dict_supers, key=dict_supers.get)

super_herous = ['Hulk', 'Captain America', 'Thanos']
url = 'https://akabab.github.io/superhero-api/api/all.json'
print(f'Самый умный супергерой это: {smartest_super(super_herous, url)}')