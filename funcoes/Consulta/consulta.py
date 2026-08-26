from abc import ABC
import sqlite3
from database.database import *

def buscar_codigo(codigo):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE id = ?",
        (codigo,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    return cliente


def buscar_nome(nome):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE nome = ?",
        (nome,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    return cliente


def buscar_cpf(cpf):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE cpf = ?",
        (cpf,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    return cliente


def buscar_telefone(tel):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM cliente WHERE telefone = ?",
        (tel,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    return cliente