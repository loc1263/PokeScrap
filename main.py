import requests
import csv
from bs4 import BeautifulSoup

url = 'https://pokemondb.net/pokedex/all'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tabla = soup.find('table')
filas = tabla.find_all('tr')

with open('PokeData.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    make_csv = csv.writer(archivo_csv)

    for fila in filas:
        celdas = fila.find_all('td')

        datos_fila = [celda.text.strip() for celda in celdas]
        make_csv.writerow(datos_fila)

print('Datos extraidos en archivo PokeData.csv')
