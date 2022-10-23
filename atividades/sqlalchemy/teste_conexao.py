import mysql.connector as mc

try:
    conn = mc.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='',
        db='INFINITY'
    )
except Exception as err:
    raise err('Não foi possivel conectar ao bd')
else:
    print('Conectado com sucesso')