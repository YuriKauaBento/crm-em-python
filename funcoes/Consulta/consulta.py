from funcoes.database.database import *

def buscar_codigo(tabela, usuario):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE usuario = ? AND ativo = 1",
        (usuario,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    return cliente


def buscar_nome(tabela, nome):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE nome LIKE ? AND ativo = 1",
        (f"%{nome}%",)
    )

    cliente = cursor.fetchall()

    conexao.close()

    return cliente


def buscar_cpf(tabela, cpf):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE cpf = ? AND ativo = 1",
        (cpf,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    return cliente


def buscar_telefone(tabela, tel):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE telefone = ? AND ativo = 1",
        (tel,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    return cliente