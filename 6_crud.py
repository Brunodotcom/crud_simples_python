from conexao import nova_conexao

def exibir_produtos():
    sql = 'SELECT * FROM produtos'

    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            print('ID - Descrição - Marca')
            for dado in cursor.fetchall():
                print(f'{dado[2]} - {dado[0]} - {dado[1]}')

        except Exception as e:
            print(f'ERRO: {e}')


def criar_produto(descricao, marca):
    args = (descricao, marca)
    sql = 'INSERT INTO produtos (descricao, marca) VALUES (%s, %s)'

    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit()
            print(f'Produto criado.')

        except Exception as e:
            print(f'ERRO {e}')


def atualizar_produto(id, descricao):
    with nova_conexao() as conexao:

        try:
            cursor = conexao.cursor()
            cursor.execute('UPDATE produtos SET descricao = %s WHERE id = %s', (descricao, id))
            conexao.commit()
            print(f'Produto atualizado.')

        except Exception as e:
            print(f'ERRO: {e}')


def deletar_produto(id):
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute('DELETE FROM produtos WHERE id = %s', (id,))
            conexao.commit()
            linhas_afetadas = cursor.rowcount

            if linhas_afetadas > 0:
                print(f'Produto deletado.')
            else:
                print(f'Nenhum produto encontrado no id {id}')

        except Exception as e:
            print(f'ERRO: {e}')



# criar_produto('ps2', 'sony')
# atualizar_produto(10, 'a20')
# deletar_produto(15)
exibir_produtos()