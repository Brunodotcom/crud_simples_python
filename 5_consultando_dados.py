from conexao import nova_conexao

sql = '''
    SELECT * FROM produtos
'''


with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    for dado in cursor.fetchall():
        print(f'{dado[2]} - {dado[0]} - {dado[1]}')