import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('mangas.db')
cur = conn.cursor()

def verificaCapitulo(link, n):

    mangaKalot = requests.get(f'{link}').content
    soup = BeautifulSoup(mangaKalot, 'html.parser')
    lista = soup.li.a
    chapter = lista.text
    oldCapitulo = cur.execute(f"SELECT cap FROM capitulo WHERE id={n}")
    capitulo = cur.fetchall()
    capitulos = capitulo[0][0]
    if capitulos == chapter:
        pass
    else:
        title = cur.execute(f"SELECT titulo FROM capitulo WHERE id={n}")
        titles = cur.fetchall()
        titulo = titles[0][0]
        print(titulo)