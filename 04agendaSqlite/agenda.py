import sqlite3, time

conectar = sqlite3.connect('agenda.db')
c = conectar.cursor()

def criar_db():
    c.execute('create table if not exists cadastro (nome text, telefone varchar, email text, data text)')

'''
try:
    criar_db()
except:
    print('Erro ao criar o banco de dados')
else:
    print('Banco de dados criado com sucesso')
'''

def inserir(n, t, e):
    d = time.strftime('%d/%m/%Y')
    c.execute('insert into cadastro values(?, ?, ?, ?)', (n, t, e, d))
    conectar.commit()

def pesquisar(p):
    sql = 'select * from cadastro where nome = ?'
    for row in c.execute(sql, (p,)):
        print(row)

fc = int(input('1 - Cadastrar\n2 - Pesquisar\nO que você deseja fazer? '))

if fc == 1:
    try:
        print('Cadastro da Agenda')
        time.sleep(2)
        n = str(input('Digite um nome: '))
        t = str(input('Digite um telefone: '))
        e = str(input('Digite um email: '))
        inserir(n, t, e)
    except:
        print('Não foi possivel salvar as informações.')
    else:
        print('Informações salvas com sucesso.')
elif fc == 2:
    print('Buscando...')
    time.sleep(1)
    p = str(input('Digite o nome a ser buscado: '))
    pesquisar(p)
else:
    print('...')