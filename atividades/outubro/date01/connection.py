import mysql.connector
#from getpass import getpass #//camada de seguraça para senha
from dotenv import load_dotenv
import os

load_dotenv('./env') #Pegando

try:
    conn = mysql.connector.connect(
        host=os.getenv('HOST'),#Pode ser localhost
        port=os.getenv('PORT'),
        user=os.getenv('USER'),
        passwd=os.getenv('PASSWD'),
        db=os.getenv('DB')
    )
except Exception as err:
    raise err('Deu ruim')
else:
    cursor = conn.cursor()


query = 'select login from users'
cursor.execute(query)
logins = [login[0] for login in cursor.fetchall()]

print('Qual número deseja atualizar? ')
for pos, login in enumerate(logins, start=1):
    print(pos, login, sep=' : ')

opcao = int(input('Opcao: '))
query = f'select * from users where login="{logins[opcao - 1]}"'
cursor.execute(query)
print('='*20)
for login, nome in cursor.fetchall():
    print(f'{login}: {nome}')
print('='*20)
nome = input('Novo nome: ')
query = f'update users set full_name="{nome}" where login="{logins[opcao - 1]}"'
cursor.execute(query)
conn.commit()

query = f'select * from users where login="{logins[opcao - 1]}"'
cursor.execute(query)
print('='*20)
for login, nome in cursor.fetchall():
    print(f'{login}: {nome}')
# login = input('Login: ').lower()

# while login in logins:
#     print('Já existe')
#     login = input('Login: ').lower()
# else:
#     nome = input('Nome: ').title()

# query = f'insert into users values ("{login}", "{nome}")'
# cursor.execute(query)
# conn.commit()


#retorno = cursor.fetchall()

#for login, nome in retorno:
#    print(login, nome, sep='-------')