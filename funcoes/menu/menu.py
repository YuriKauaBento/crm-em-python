from abc import ABC, abstractmethod
from funcoes.Alterar.alterar import *
from funcoes.Log_In.login import Sessao

class Menu_base(ABC):
    def __init__(self):
            self.msg = ''

    @abstractmethod
    def exibir(self):
        pass
    

class Menu_inicial(Menu_base):
    def exibir(self):
        self.msg = (
            "1. Cadastro\n"
            "2. Consulta\n"
            "3. Emissão de Ordem de Serviço\n"
            "0. Sair\n"
        )
        return self.msg


class Menu_cadastro(Menu_base):
    def exibir(self):
        self.msg = (
            "1. CADASTRO DE CLIENTES\n"
            "2. CADASTRO DE FORNECEDORES\n"
            "3. CaADASTRO DE OTICAS\n"
            "4. ALTERACAO DE CADASTRO\n"
            "5. CADASTRO DE USUARIOS\n"
            "0. VOLTAR\n"
        )
        return self.msg


class Menu_consulta(Menu_base):
    def exibir(self):
        self.msg = (
            "1. CONSULTA DE CLIENTES\n"
            "2. CONSULTA DE FORNECEDORES\n"
            "3. CONSULTA DE OTICAS\n"
            "4. CONSULTA DE ORDENS DE SERVICO\n"
            "0. VOLTAR\n"
        )
        return self.msg

    def menu_consulta(self):
        self.msg = (
            "1. BUSCAR NOME\n"
            "2. BUSCAR TELEFONE\n"
            "3. BUSCAR CPF/CNPJ\n"
            "4. BUSCAR CODIGO\n"
            "0. VOLTAR\n"
        )
        return self.msg

class Menu_alteracao(Menu_base):
    def exibir(self):
        self.msg = ("ALTERACAO DE CADASTRO\n"
                    "INFORME O TIPO DE CADASTRO: \n"
                    "1. CLIENTES\n"
                    "2. FORNECEDORES\n"
                    "3. OTICAS\n"
                    "4. VOLTAR\n")
        return self.msg


class Menu_exclusao(Menu_base):
    def exibir(self):
        self.msg = "DESATIVAR CADASTRO"
        tabela = input("INFORME O TIPO DE CADASTRO\n"
                       "1. CLIENTES\n"
                       "2. FORNECEDORES\n"
                       "3. OTICAS\n"
                       "4. VOLTAR\n")

        while True:
            if tabela == '1':
                tabela = "clientes"
                break
            elif tabela == '2':
                tabela = "fornecedores"
                break
            elif tabela == '3':
                tabela = "oticas"
                break
            elif tabela == '4':
                break
            else:
                print("OPCAO INVALIDA!")

        usuario = None
        cpf = None
        
        while True:
            if tabela == '4':
                break

            op = int(input("1. CANCELAR POR CPF/CNPJ\n"
                        "2. CANCELAR POR CODIGO DE USUARIO\n"))
            
            if op == 1:
                cpf = input("INFORME O CPF/CNPJ: ")
                if cpf == '':
                    cpf = None
                break
            elif op == 2:
                usuario = input("INFORME O CODIGO: ").upper()
                if usuario == '':
                    usuario = None
                break
            else:
                print("OPCAO INVALIDA!")

        return excluir(tabela, usuario, cpf)


class Menu_login(Menu_base):
    def exibir(self):
        self.msg = ("BEM VINDO!\n"
                    "INFORME SEU USUARIO E SENHA\n"
                    )


        return self.msg