import requests                # для HTTP-запросов
from bs4 import BeautifulSoup  # парсер HTML
import csv                     # запись данных в CSV
import argparse                # парсинг аргументов командной строки
import os                      # работа с файловой системой (проверка существования файла)
import time                    # для паузы

#рписывает и читает аргументы командной строки
parser = argparse.ArgumentParser(description="Extract country data from doheth.co.uk")
parser.add_argument("--input", default="countries.txt", help="Input file with country names (English)")
parser.add_argument("--output", default="countries_data.csv", help="Output CSV file")
parser.add_argument("--cache", default="cached_page.html", help="Local cache of the HTML page")
args = parser.parse_args()

#загружает HTML либо из кэша, либо с сайта и сохраняем в кэш
url = "https://doheth.co.uk/info/countries-of-the-world.php"

if os.path.exists(args.cache):  #если кэш-файл существует
    with open(args.cache, "r", encoding="utf-8") as f:
        html = f.read() #читает HTML из кэша без инета
else:
    response = requests.get(url) #иначе делаем сетевой запрос
    response.raise_for_status()  # проверяет, что ответ 200 (значит что успешнр подключился к сайту) иначе бросит исключение
    html = response.text  # получает HTML как текст
    with open(args.cache, "w", encoding="utf-8") as f:
        f.write(html) #сохраняет HTML в кэш-файл, чтобы в следующий раз не обращаться к сети
    time.sleep(1)   # пауза после запроса, чтобы не перегружать сервер

#создаёт объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html, "html.parser")

#читает входной файл со списком стран на английском
with open(args.input, "r", encoding="utf-8") as f:
    english_names = [line.strip() for line in f if line.strip()]  #убирает пустые строки и пробелы

#проходит по строкам таблицы и извлекает нужные поля
results = []
rows = soup.select("tr")                      #берёт все строки таблицы

for row in rows:
    cells = row.find_all("td")                #ячейки в строке
    if len(cells) >= 6:                       #только строки с достаточным количеством колонок
        country = cells[0].text.strip()       #название страны: <td class="name">Abkhazia</td>
        capital = cells[2].text.strip()       #столица: третья колонка
        population = cells[4].text.strip().replace(",", "")  #население: пятая колонка, удаляет запятые
        area = cells[5].text.strip().replace(",", "")        #площадь: шестая колонка, удаляет запятые

        #берёт только те страны, что присутствуют во входном файле
        if country in english_names:
            results.append([country, capital, area, population])
            print(f"{country},{capital},{area},{population}")

#записывает результат в выходной CSV
with open(args.output, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["country", "city", "area", "population"])  #заголовки CSV
    writer.writerows(results)                                   #все строки данных

#для запуска  python task1.py --input countries.txt --output countries_data.csv --cache cached_page.html
# --input - файл со списком стран
# --output - куда сохранить CSV
# --cache - локальный HTML-файл, чтобы не качать сайт каждый раз