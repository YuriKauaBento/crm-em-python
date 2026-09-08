from funcoes.database.database import *
import bcrypt

def validar_usuario(usuario='', senhad=''):
    conexao = conectar()
    cursor = conexao.cursor()

    usuario = input("Usuario: ")
    senhad = input("Senha: ")

    cursor.execute(
        "SELECT usuario, senha FROM usuarios WHERE usuario = ?",
        (usuario,)
    )    

    resultado = cursor.fetchone()

    if resultado is None:
        return "Usuario nao encontrado!"
    else:
        usuario, senha_hash, ativo = resultado

        if ativo == 0:
            return "Usuario inativo"

        if bcrypt.checkpw(
            senhad.encode("utf-8"),
            senha_hash.encode("utf-8")
        ):
            return True
        else:
            return False