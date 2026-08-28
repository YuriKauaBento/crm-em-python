from abc import ABC, abstractmethod

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
            "5. Voltar\n"
        )

