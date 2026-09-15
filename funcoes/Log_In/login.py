from funcoes.database.database import *
import bcrypt


class Sessao:
    def __init__(self, usuario, perfil=None):
        self.usuario = usuario
        self.perfil = perfil

    def validar_usuario(self, usuario, senhad):
        conexao = conectar()
        cursor = conexao.cursor()

        #usuario = input("Usuario: ")
        #senhad = input("Senha: ")

        cursor.execute(
            """SELECT usuario, senha_hash, perfil, ativo
              FROM usuarios 
              WHERE usuario = ?""",
            (usuario,)
        )    

        resultado = cursor.fetchone()

        if resultado is None:
            return "Usuario nao encontrado!"
        else:
            usuario, senha_hash, perfil, ativo = resultado

            if ativo == 0:
                return "Usuario inativo"

            if bcrypt.checkpw(
                senhad.encode("utf-8"),
                senha_hash.encode("utf-8")
            ):
                self.perfil = perfil
                self.usuario = usuario
                return self.usuario, self.perfil
            else:
                return "Senha incorreta"