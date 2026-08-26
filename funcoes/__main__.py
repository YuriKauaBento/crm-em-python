from funcoes.Cadastro.cadastro_cliente import *
from funcoes.menu.menu import *
from funcoes.Consulta.consulta import *

def main():
    while True:
        op = input(Menu_inicial())
        try:
            if op == 1:
                op_cadastro = input(Menu_cadastro.menu1())
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
            elif op == 2:
                op_consulta = input(Menu_consulta.menu2())
                if op_consulta == 1:
                    consulta_cliente = input(Menu_consulta.menu_consulta())
                    if consulta_cliente == 1:
                        a = input("DIgite o nome: ")
                        buscar_nome(a)
                    elif consulta_cliente == 2:
                        a = input("Digite o telefone:")
                        buscar_telefone(a)
        except sqlite3.OperationalError as e:
            print(f"Erro operacional ou de conexao com o SQLite")
            