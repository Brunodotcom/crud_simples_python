from conexao import nova_conexao

sql = 'ALTER TABLE produtos ADD CONSTRAINT unique_valor_desc UNIQUE (descricao)'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)