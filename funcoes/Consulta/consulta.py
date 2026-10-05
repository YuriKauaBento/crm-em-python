from funcoes.database.database import *

def validacao(cliente, conexao):
    conexao.close()
    if cliente:
        return cliente
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

    return validacao(cliente, conexao)



def buscar_nome(tabela, nome):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE nome LIKE ? AND ativo = 1",
        (f"%{nome}%",)
    )

    cliente = cursor.fetchall()

    return validacao(cliente, conexao)


def buscar_cpf(tabela, cpf):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE doc = ? AND ativo = 1",
        (cpf,)
    )

    cliente = cursor.fetchone()

    return validacao(cliente, conexao)


def buscar_telefone(tabela, tel):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE telefone = ? AND ativo = 1",
        (tel,)
    )

    cliente = cursor.fetchone()

    return validacao(cliente, conexao)