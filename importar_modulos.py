#### Importacion de modulos

# import math
# print(math.sqrt(15))

# #### Importacion de funciones desde otro modulo / documemto
# from modulos.helper import greeting # Esta importacion es si solo voy a importar una funcion 
# import modulos.helper # Esta es si voy a importar mas funciones
# print(modulos.helper.greeting("Caty"))

#### Instalar NUMPY usando PIP
# import numpy as np 
# num_range = np.arange(16)
# reshape = num_range.reshape(4,4)
# print(reshape)

#### Api conectada usando Request package: 
# https://jsonplaceholder.typicode.com/
# https://jsonplaceholder.typicode.com/posts

# import pprint
# api_data = requests.get("https://jsonplaceholder.typicode.com/posts")
# pprint.pprint(api_data.json()[0]["title"])

#### Construir una web scrapper usando varias librerias

import requests
import inflection
from bs4 import BeautifulSoup
# 1. Descargar la página web
# 2. Seleccionar y extraer enlaces
# 3. Convertir enlaces en títulos

# pip install requests
# pip install inflection
# pip install beautifulsoup4

def scrapper_web(url):
  api_data = requests.get(url)
  titles = []

  html_data = api_data.text
  soup_data = BeautifulSoup(html_data, "html.parser")
  for link in soup_data.find_all("a"):
    href = link.get("href")
    if href and href.startswith("/servicios/"):
      slug = href.split("/servicios/")[-1].strip("/")
      if slug:
        title = inflection.titleize(slug.replace("-", " "))
        titles.append(title)

  return titles

print(scrapper_web("https://blancodent.com/servicios/servicios"))