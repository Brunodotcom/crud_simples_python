from conexao import nova_conexao

sql = '''
    INSERT INTO produtos (descricao, marca) VALUES (%s, %s)
'''

args = (
    ('iphone', 'apple'),
    ('a10', 'samsung'),
    ('redmi', 'xaomi'),
    ('ps5', 'sony')
)

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.executemany(sql, args)
    conexao.commit()