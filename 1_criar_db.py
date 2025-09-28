from conexao import nova_conexao

sql = 'CREATE DATABASE loja'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)