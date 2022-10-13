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
    while True: 
        try:
            link = cur.execute(f"SELECT link FROM capitulo WHERE id={n}")
            links = cur.fetchall()
            verificaCapitulo(links[0][0], n)
        except:
            print("acabou!!")
            break
        n += 1
 


def excluindomanga():
    print("excluindo manga")