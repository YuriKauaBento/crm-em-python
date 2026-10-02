from funcoes.database.database import *
import bcrypt


class Cadastro:
    def __init__(self):
        self.nome = ''
        self.cpf = ''
        self.endereco = ''
        self.telefone = ''
        self.tabela = ''


    def cadastrar(self):
        return cadastro_db(self.tabela, self.nome, self.cpf, self.endereco, self.telefone)


    

class Cliente(Cadastro):
    def __init__(self):
        super().__init__()
        self.tabela = 'clientes'

    def cadastrar(self, nome, cpf, endereco='', telefone=''):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        return super().cadastrar()


class Otica(Cadastro):
    def __init__(self):
        super().__init__()
        self.tabela = 'oticas'

    def cadastrar(self, nome, cpf, endereco='', telefone=''):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        return super().cadastrar()


class Fornecedor(Cadastro):
    def __init__(self):
        super().__init__()
        self.tabela = 'fornecedores'

    def cadastrar(self, nome, cpf, endereco='', telefone=''):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        return super().cadastrar()


class Usuario():
    def __init__(self, nome, senha, perfil, sessao):
        self.tabela = 'usuarios'
        self.nome = nome
        self.senha = senha
        self.perfil = perfil
        self.sessao = sessao

    def cadastrar(self):
        if self.sessao != 'admin':
            return 'ACESSO NEGADO!'
        else:
            senhan = self.senha
            self.senha = bcrypt.hashpw(
                senhan.encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")

            cadastro_db(tabela=self.tabela, nome=self.nome, senha=self.senha, perfil=self.perfil)
            return 'USUARIO CADASTRADO COM SUCESSO!'
