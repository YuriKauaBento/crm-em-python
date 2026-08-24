from funcoes.Cadastro.cadastro_cliente import *
from funcoes.menu.menu import *

def main():
    while True:
        op = input(Menu_inicial())
        try:
            if op == 1:
                op_cadastro = input(Menu_cadastro())
                if op_cadastro == 1:
                    cliente = Cliente()
                    cliente.cadastrar()
                    print('Cliente cadastrado com sucesso!')
                elif op == 2:
                    fornecedor = Fornecedor()
                    fornecedor.cadastrar()
                    print('Fornecedor cadastrado com sucesso!')
                elif op == 3:
                    otica = Otica()
                    otica.cadastrar()
                    print('Otica cadastrada com sucesso!')
                elif op == 0:
                    break
        except sqlite3.OperationalError as e:
            print(f"Erro operacional ou de conexao com o SQLite")
            