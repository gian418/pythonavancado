import sqlite3

path = '/home/gian/sqlite/aula'
#path = r'/home/gian/sqlite/aula' #r é pra ser totalmente string

conn = sqlite3.connect(path+'/teste.db')
#conn = sqlite3.connect(path+r'/teste.db') #caso esteja com problemas em reconhecer o path

c = conn.cursor()

"""
def create_table():
    c.execute('CREATE TABLE dados (id integer, valor real, nome text, endereco text, total real)')

#create_table()

def inserirDados():
    c.execute("INSERT INTO dados VALUES(1, 50, 'Giancarlo Albano', 'Rua A', 500)")
    c.execute("INSERT INTO dados VALUES(2, 150, 'Dulce Albano', 'Rua B', 600)")
    c.execute("INSERT INTO dados VALUES(3, 250, 'Ozair Albano', 'Rua C', 700)")
    c.execute("INSERT INTO dados VALUES(4, 350, 'Daiane Backes', 'Rua D', 800)")
    conn.commit()

inserirDados()
"""

sql = 'SELECT * FROM dados WHERE nome = ?'

def ler_dados(vlrbusca):
    for row in c.execute(sql, (vlrbusca,)):
        print(row)

ler_dados('Giancarlo Albano')

