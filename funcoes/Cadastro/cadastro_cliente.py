from funcoes.database.database import *
import bcrypt


class Cadastro():
    def __init__(self):
        self.nome = ''
        self.cpf = ''
        self.endereco = ''
        self.telefone = ''
        self.tabela = ''


    def cadastrar(self):
        conexao = conectar()
        cursor = conexao.cursor()
                
        cursor.execute(f"""
            INSERT INTO {self.tabela} (nome, doc, endereco, telefone) 
            VALUES (?, ?, ?, ?)
        """, (self.nome, self.cpf, self.endereco, self.telefone))

        conexao.commit()
        codigo = cursor.lastrowid
        conexao.close()
        
        return codigo


    

class Cliente(Cadastro):
    def __init__(self):
        super().__init__()
        self.tabela = 'clientes'

    def cadastrar(self):
        self.nome = input('Nome do cliente: ')
        self.cpf = input('CPF: ')
        self.endereco = input('Endereco: ')
        self.telefone = input('Telefone: ')
        return super().cadastrar()


class Otica(Cadastro):
    def __init__(self):
        super().__init__()
        self.tabela = 'oticas'

    def cadastrar(self):
        self.nome = input('Razão social: ')
        self.cpf = input('CNPJ: ')
        self.endereco = input('Endereco: ')
        self.telefone = input('telefone: ')
        return super().cadastrar()


class Fornecedor(Cadastro):
    def __init__(self):
        super().__init__()
        self.tabela = 'fornecedores'

    def cadastrar(self):
        self.nome = input('Razao social: ')
        self.cpf = input('CNPJ ')
        self.endereco = input('Endereco: ')
        self.telefone = input('Telefone: ')
        return super().cadastrar()


class Usuario():
    def __init__(self, nome='', senha='', perfil=''):
        self.nome = nome
        self.senha = senha
        self.perfil = perfil

    def cadastrar(self, logado):
        if logado.perfil != "admin":
            return "Acesso negado"

        else:
            self.nome = input("Informe o nome do usuario: ")
            senhan = input("Defina a senha: ")
            self.senha = bcrypt.hashpw(
                senhan.encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")
            self.perfil = input("Defina o nivel de acesso: ")

            conexao = conectar()
            cursor = conexao.cursor()

            cursor.execute("""
                INSERT INTO usuarios (nome, senha_hash, perfil)
                VALUES (?,?,?)
            """, (self.nome, self.senha, self.perfil))

            conexao.commit()
            conexao.close()
