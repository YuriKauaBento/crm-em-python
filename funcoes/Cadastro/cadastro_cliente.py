from abc import ABC
from funcoes.database.database import *



class Cadastro(ABC):
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
            CREATE TABLE IF NOT EXISTS {self.tabela} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT,
                endereco TEXT,
                telefone TEXT
                ativo INTEGER DEFAULT 1
            )
        """)
        
        cursor.execute(f"""
            INSERT INTO {self.tabela} (nome, cpf, endereco, telefone) 
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
        self.tabela = 'otica'

    def cadastrar(self):
        self.nome = input('Razão social: ')
        self.cpf = input('CNPJ: ')
        self.endereco = input('Endereco: ')
        self.telefone = input('telefone: ')
        return super().cadastrar()


class Fornecedor(Cadastro):
    def __init__(self):
        super().__init__()
        self.tabela = 'fornecedor'

    def cadastrar(self):
        self.nome = input('Razao social: ')
        self.cpf = input('CNPJ ')
        self.endereco = input('Endereco: ')
        self.telefone = input('Telefone: ')
        return super().cadastrar()

