from funcoes.database.database import *

def validacao(cliente, conexao, tabela):
    conexao.close()
    if cliente and tabela == 'usuarios':
        return ('--- PERFIL DO USUARIO ---\n'
                f'COD: {cliente['usuario']}\n'
                f'NOME: {cliente['nome']}\n'
                ).center()
    elif cliente and tabela != 'usuarios':
        doc = cliente['doc']
        if len(doc) > 11:
            doc_format = f'{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[12:]}'
        else:
            doc_format = f'{doc[:3]}.{doc[3:6]}.{doc[6:9]}-{doc[9:]}'
        return ('--- PERFIL DO USUARIO ---\n'
                f'NOME/RAZAO SOCIAL: {cliente['nome']}\n'
                f'COD: {cliente['usuario']}\n'
                f'CPF/CNPJ: {doc_format}\n'
                f'ENDERECO: {cliente['endereco']}\n'
                f'TELEFONE: '
                )
    else:
        return "CADASTRO NÃO ENCONTRADO!"
        

def buscar_codigo(tabela, usuario):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE usuario = ? AND ativo = 1",
        (usuario,)
    )

    cliente = cursor.fetchone()

    return validacao(cliente, conexao, tabela)



def buscar_nome(tabela, nome):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE nome LIKE ? AND ativo = 1",
        (f"%{nome}%",)
    )

    cliente = cursor.fetchall()

    return validacao(cliente, conexao, tabela)


def buscar_cpf(tabela, cpf):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE doc = ? AND ativo = 1",
        (cpf,)
    )

    cliente = cursor.fetchone()

    return validacao(cliente, conexao, tabela)


def buscar_telefone(tabela, tel):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE telefone = ? AND ativo = 1",
        (tel,)
    )

    cliente = cursor.fetchone()

    return validacao(cliente, conexao, tabela)