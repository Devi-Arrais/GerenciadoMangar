import sqlite3
from request import *


conn = sqlite3.connect('mangas.db')
cur = conn.cursor()

def Criandobanco():
    cur.execute('CREATE TABLE IF NOT EXISTS capitulo(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, link TEXT NOT NULL, cap TEXT NOT NULL);')

def adicinarmanga(title, links, chapter):
    cur.execute('INSERT INTO capitulo(titulo, link, cap) VALUES(?, ?, ?);', (title, links, chapter))
    conn.commit()

def verifica():
    n = 1
    ids = cur.execute("SELECT MAX(id) FROM capitulo")
    ident = cur.fetchone()
    id = ident[0]
    while n <= id: 
        try:
            link = cur.execute(f"SELECT link FROM capitulo WHERE id={n}")
            links = cur.fetchall()
            verificaCapitulo(links[0][0], n)
        except:
            pass
        n += 1
 
def listarmangas():
    mangas = cur.execute("SELECT titulo FROM capitulo")
    for i in mangas:
        print(i[0])

def excluindomanga(nome):
    try:
        cur.execute(f"DELETE FROM capitulo WHERE titulo = '{nome}';")
        print(f"Manga {nome} removido")
        conn.commit()
    except:
        print(f"Manga {nome} não esta na sua lista tente novamente")