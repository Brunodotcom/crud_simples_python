from conexao import nova_conexao

sql = 'CREATE TABLE produtos (descricao VARCHAR(30), marca VARCHAR(15), id INT AUTO_INCREMENT PRIMARY KEY)'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)