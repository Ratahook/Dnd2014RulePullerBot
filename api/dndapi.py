import requests

BASE_URL = 'https://www.dnd5eapi.co/api/2014/'

def getspellbylvl(lvl):
    response = (requests.get(f'{BASE_URL}spells')).json()
    namelist = []
    for spell in response['results']:
        if spell['level'] == lvl:
            namelist.append(spell['name'])
    return namelist

def getspellbyname(name):
    response = (requests.get(f'{BASE_URL}spells')).json()
    namelist = []
    indexlist = []
    for spell in response['results']:
        spellname = spell['name'].lower()
        if spellname == name.lower():
            namelist.append(f'Название: {spell['name']}')
            indexlist.append(spell['index'])
    if not namelist:
        for spell in response['results']:
            spellname = spell['name'].lower()
            if spellname.startswith(name.lower()):
                namelist.append(f'Название: {spell['name']}')
                indexlist.append(spell['index'])
    if len(namelist) > 1:
        return namelist
    else:
        spellresponce = (requests.get(f'{BASE_URL}spells/{indexlist[0]}')).json()
        namelist.append(f'Описание: {'\n'.join(spellresponce["desc"])}')
        namelist.append(f'Дальность: {spellresponce["range"]}')
        namelist.append(f'Время накладывания: {spellresponce["casting_time"]}')
        namelist.append(f'Длительность: {spellresponce["duration"]}')
        namelist.append(f'Круг: {spellresponce["level"]}')
        namelist.append(f'Школа: {spellresponce["school"]['name']}')
        return namelist

def getspellbyschool(school):
    response = (requests.get(f'{BASE_URL}spells/?school={school}')).json()
    namelist = []
    for spell in response['results']:
            namelist.append(spell['name'])
    return namelist

def getspellbyclass(dnd_class):
    response = (requests.get(f'{BASE_URL}classes/{dnd_class}/spells')).json()
    namelist = []
    for spell in response['results']:
            namelist.append(spell['name'])
    return namelist



