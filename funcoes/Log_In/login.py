from funcoes.database.database import *
import bcrypt


class Sessao:
    def __init__(self, usuario=''):
        self.usuario = usuario
        self.perfil = usuario["perfil"]

    def validar_usuario(self, usuario='', senhad=''):
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
                self.usuario = usuario
                return self.usuario
            else:
                return "Senha incorreta"