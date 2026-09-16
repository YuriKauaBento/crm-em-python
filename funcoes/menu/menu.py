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
            "1. Cadastro de clientes\n"
            "2. Cadastro de fornecedores\n"
            "3. Cadastro de oticas\n"
            "4. Alteracao de cadastro\n"
            "0. Voltar\n"
        )
        return self.msg


class Menu_consulta(Menu_base):
    def exibir(self):
        self.msg = (
            "1. Consulta de clientes\n"
            "2. Consulta de fornecedores\n"
            "3. Consulta de oticas\n"
            "4. Consulta de ordens de servico\n"
            "0. Voltar\n"
        )
        return self.msg

    def menu_consulta(self):
        self.msg = (
            "1. Buscar nome\n"
            "2. Buscar telefone\n"
            "3. Buscar CPF/CNPJ\n"
            "4. Buscar codigo\n"
            "0. Voltar\n"
        )
        return self.msg

class Menu_alteracao(Menu_base):
    def exibir(self):
        self.msg = "ALTERACAO DE CADASTRO"

        tabela = input("Informe o tipo de cliente: \n"
                       "1. clientes\n"
                       "2. fornecedores\n"
                       "3. oticas\n")

        if tabela == '1':
            tabela = "clientes"
        elif tabela == '2':
            tabela = "fornecedores"
        elif tabela == '3':
            tabela = "oticas"
        else:
            print("opcao invalida!")

        usuario = input("Informe o usuario do cliente: ")

        if localizar(usuario, tabela) == 0:
            return f'Usuário não existe'
        else:
            print("Informe apenas as informações a serem alteradas: ")

            nome = input("Informe o nome se foi alterado: ")
            cpf = input("Informe o cpf/cnpj se foi alterado: ")
            tel = input("Informe o telefone se foi alterado: ")
            end = input("Informe o endereco se foi alterado: ")

            return alteracao(usuario, tabela, nome, cpf, tel, end)


class Menu_exclusao(Menu_base):
    def exibir(self):
        self.msg = "DESATIVAR CADASTRO"
        tabela = input("Informe o tipo de cadastro\n"
                       "1. clientes\n"
                       "2. fornecedores\n"
                       "3. oticas\n")
        if tabela == '1':
            tabela = "clientes"
        elif tabela == '2':
            tabela = "fornecedores"
        elif tabela == '3':
            tabela = "oticas"
        else:
            print("opcao invalida!")

        op = int(input("1. Cancelar por cpf/cnpj\n"
                    "2. Cancelar por codigo de usuario\n"))
        if op == 1:
            cpf = input("Informe o cpf")
            if cpf == '':
                cpf = None
        elif op == 2:
            usuario = input("Informe o codigo: ")
            if usuario == '':
                usuario = None
        else:
            print("opcao invalida!")

        return excluir(tabela, usuario, cpf)


class Menu_login(Menu_base):
    def exibir(self):
        self.msg = ("Bem vindo!\n"
                    "Informe seu usuario e senha"
                    )
        usuario = input("usuario: ")
        senha = input("senha: ")

        sessao = Sessao(usuario)

        return sessao.validar_usuario(usuario, senha)