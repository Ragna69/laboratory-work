# состоавить структуру в которой будет храниться фамилия призывника,
# рот войск в которыъ он будет призван, дата призыва, дата демобилизации,
#с возможностью ввода где мы вводим имя призывника и роту войск, если рота уже есть то не добавлять, а если нет то добавить

import time
import random

prizivniki = []
names = ["Ivanov", "Sak", "Petrov", "Haraldin"]
rots = ["ВДВ","ТВ","ВВС"]

def add_prizivnik(name, rota):
    for x in prizivniki:
        if x["name"] == name and x["rota"] == rota:
            print(f"{name} уже есть в роте {rota}")
            return
    mobilization_day = time.strftime("%Y-%m-%d", time.localtime())
    demobilization_day = time.strftime("%Y-%m-%d", time.localtime(time.time() + 365*24*3600))

    prizivnik = {
        "name":name,
        "rots":rota,
        "mobilization_day":demobilization_day,
        "demobilization_day":mobilization_day,
    }
    prizivniki.append(prizivnik)
    print("Добавлен призывник", prizivnik)

def show_prizivniki():
    for x in prizivniki:
        print(x)
def save_prizivniki(file="prizivniki.txt"):
    now = time.strftime("%Y-%m-%d %H:%M:%S)")
    with open("prizivniki.txt","w", encoding = 'utf-8') as file:
        for x in prizivniki:
            file.write(f"{now}; {x['name']}; {x['rots']}; {x['mobilization_day']}; {x['demobilization_day']};\n")
    print("Сохранено в файл", file)

name = random.choice(names)
rota = random.choice(rots)
add_prizivnik(name, rota)

input_name = input('Введите имя призывника: ')
input_rota = input('Введите рот войск: ')
add_prizivnik(input_name, input_rota)

print('Список призывников:')
show_prizivniki()
save_prizivniki()











