from funcoes.Cadastro.cadastro_cliente import *
from funcoes.menu.menu import *
from funcoes.Consulta.consulta import *
from funcoes.Alterar.alterar import *
from funcoes.Log_In.login import *

def main():
    criar_tabelas()
    
    while True:
        menu = Menu_inicial()
        menu.exibir()
        op = int(input())
        if op == 1:
            valid0 = False
            while valid0 == False:
                menu = Menu_cadastro()
                menu.exibir()
                op = int(input())
                if op == 1:
                    nome = input("Nome do cliente:\n")
                    cpf = input("CPF do cliente:\n")
                    endereco = input("Endereco do cliente:\n")
                    telefone = input("Telefone do cliente:\n")

                    cliente = Cliente()
                    cliente.cadastrar(nome, cpf, endereco, telefone)
                    print(f"Cliente cadastrado com sucesso! Codigo: {cliente}")
                    valid0 = True
                elif op == 2:
                    nome = input("Razao social:\n")
                    cpf = input("CNPJ:\n")
                    endereco = input("Endereco:\n")
                    telefone = input("Telefone:\n")

                    fornecedor = Fornecedor()
                    fornecedor.cadastrar(nome, cpf, endereco, telefone)
                    print(f"Fornecedor cadastrado com sucesso! Codigo {fornecedor}")
                    valid0 = True
                elif op == 3:
                    nome = input("Razao social:\n")
                    cpf = input("CNPJ:\n")
                    endereco = input("Endereco:\n")
                    telefone = input("Telefone:\n")

                    otica = Otica()
                    otica.cadastrar(nome, cpf, endereco, telefone)
                    print(f"Otica cadastrada com sucesso! Codigo{otica}")
                    valid0 = True
                elif op == 4:
                    valid1 = False
                    while valid1 == False:
                        menu = Menu_alteracao()
                        menu.exibir()
                        op = int(input())
                        tabela = ''

                        if op == 1:
                            tabela = 'clientes'
                        elif op == 2:
                            tabela = 'fornecedores'
                        elif op == 3:
                            tabela = 'oticas'
                        elif op == 4:
                            valid1 = True

                        usuario = input("Informe o usuario que deseja alterar:\n")
                        loc = localizar(usuario, tabela)
                        if loc == False:
                            print("O usuario nao existe!")
                        else:
                            print("Informe apenas as informações a serem alteradas: ")
                            
                            nome = input("Informe o nome se foi alterado: \n")
                            cpf = input("Informe o cpf/cnpj se foi alterado: \n")
                            telefone = input("Informe o telefone se foi alterado: \n")
                            endereco = input("Informe o endereco se foi alterado: \n")
                            alteracao(usuario, tabela, nome, cpf, telefone, endereco)
                            print("Alteracao concluida!")
                            valid1 = True

if __name__ == '__main__':
    main()
            