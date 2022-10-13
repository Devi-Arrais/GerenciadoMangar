import requests
from bs4 import BeautifulSoup
import sqlite3


def verificaCapitulo(link, n):
    conn = sqlite3.connect('mangas.db')
    cur = conn.cursor()

    try:
        mangaKalot = requests.get(f'{link}').content
        soup = BeautifulSoup(mangaKalot, 'html.parser')
        lista = soup.li.a
        chapter = lista.text
    except:
        print("não foi possivel conectar ao site")
    oldCapitulo = cur.execute(f"SELECT cap FROM capitulo WHERE id={n};")
    capitulo = cur.fetchall()
    capitulos = capitulo[0][0]
    if capitulos == chapter:
        pass
    else:
        title = cur.execute(f"SELECT titulo FROM capitulo WHERE id={n};")
        titles = cur.fetchall()
        titulo = titles[0][0]
        cur.execute(f"UPDATE capitulo SET cap = '{chapter}' WHERE id={n};")
        conn.commit()
        print(titulo)