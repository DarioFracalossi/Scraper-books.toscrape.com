"""
Scraper para la web books.toscrape.com

Este script de prueba, funciona para leer los datos del HTML de la pagina web de books.toscrape.com, mostrando en 
consola una tabla de cada libro con su precio. Ademas, el script permite elegir exportar esa tabla a un archivo Excel o
CSV, a elección del usuario, en una ruta tambien elegible.

"""


import requests
import pandas
import os
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

#El .encodig sirve para elegir que codificación se debe usar para leer correctamente los datos del HTML.
respuesta = requests.get(url)
respuesta.encoding = "utf-8"

soup = BeautifulSoup(respuesta.text, "html.parser")

libros = soup.find_all("article", class_="product_pod")

#listas vacias para luego añadirles los nombres de los libros y los precios
nombres = []
precios = []

for libro in libros:
    precio = libro.find("p", class_="price_color")
    nombre = libro.find('h3')
    nombre = nombre.find('a')
    nombres.append(nombre["title"])
    precios.append(precio.text)

datos = {"Titulos": nombres, "Precios": precios}
df = pandas.DataFrame(datos)

print(df.to_string(index=False))

desicion = input("Ingrese la letra E si quiere exportar un archivo Excel o la letra C si quiere exportar un archivo CSV: ")

while desicion != "c" and desicion != "C" and desicion != "E" and desicion != "e":
    desicion = input("Por favor, ingrese una opción valida (E/C): ")
    
listo = False
    
while not listo:
    if desicion == "c" or desicion == "C":
        ruta = input("Ingrese una ruta para guardar el archivo CSV: ")
        while not os.path.isdir(ruta):
            ruta = input("Por favor, ingrese una ruta valida: ")
        else:
            ruta = ruta + r"\libros.csv"
            df.to_csv(ruta, index=False)
            print("¡Archivo exportado exitosamente!")
            listo = True
    elif desicion == "E" or desicion == "e":
        ruta = input("Ingrese una ruta para guardar el archivo Excel: ")
        while not os.path.isdir(ruta):
            ruta = input("Por favor, ingrese una ruta valida: ")
        else:
            ruta = ruta + r"\libros.xlsx"
            df.to_excel(ruta, index=False)
            print("¡Archivo exportado exitosamente!")
            listo = True