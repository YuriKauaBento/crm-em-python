from funcoes.database.database import *

def buscar_codigo(codigo):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE id = ? AND ativo = 1",
        (codigo,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    return cliente


def buscar_nome(nome):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE nome = ? AND ativo = 1",
        (nome,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    return cliente


def buscar_cpf(cpf):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE cpf = ? AND ativo = 1",
        (cpf,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    return cliente


def buscar_telefone(tel):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE telefone = ? AND ativo = 1",
        (tel,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    return cliente