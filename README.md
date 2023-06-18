# PokeScrap
Python web scraping

### CODE

```python
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

```

### Output
#, Nombre, Tipo, Total, HP, Attack, Defence, Sp. Atk, Sp.Def, Speed  


0001,Bulbasaur,Grass Poison,318,45,49,49,65,65,45  
0002,Ivysaur,Grass Poison,405,60,62,63,80,80,60  
0003,Venusaur,Grass Poison,525,80,82,83,100,100,80  
0003,Venusaur Mega Venusaur,Grass Poison,625,80,100,123,122,120,80  
0004,Charmander,Fire,309,39,52,43,60,50,65  
0005,Charmeleon,Fire,405,58,64,58,80,65,80  
0006,Charizard,Fire Flying,534,78,84,78,109,85,100  
0006,Charizard Mega Charizard X,Fire Dragon,634,78,130,111,130,85,100  
0006,Charizard Mega Charizard Y,Fire Flying,634,78,104,78,159,115,100  
0007,Squirtle,Water,314,44,48,65,50,64,43  
0008,Wartortle,Water,405,59,63,80,65,80,58  
0009,Blastoise,Water,530,79,83,100,85,105,78  
.
.
.




