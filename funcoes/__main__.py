from funcoes.Cadastro.cadastro_cliente import *
from funcoes.menu.menu import *
from funcoes.Consulta.consulta import *
from funcoes.Alterar.alterar import *
from funcoes.Log_In.login import *

def main():
    criar_tabelas()

    while True:
        usuario = input("Usuario: ")
        senha = input("Senha: ")
        login = Sessao(usuario)
        resultado = login.validar_usuario(usuario, senha)
        if isinstance(resultado, tuple):
            perfil = resultado[1]
            print("login efetuado com sucesso!")
            break
    
    while True:
        valid0 = False
        menu = Menu_inicial()
        menu.exibir()
        op = int(input())
        if op == 1:
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
                elif op == 0:
                    valid0 = True
        elif op == 2:
            while valid0 == False:
                menu = Menu_consulta()
                menu.exibir()
                valid1 = False
                op = int(input())
                while valid1 == False:
                    if op == 1:
                        menu.menu_consulta()
                        valid2 = False
                        op = int(input())
                        tabela = 'clientes'
                        while valid2 == False:
                            if op == 1:
                                nome = input("Informe o nome do cliente:\n")
                                print(buscar_nome(tabela, nome))
                                valid2 = True
                            elif op == 2:
                                telefone = input("Informe o telefone do cliente:\n")
                                print(buscar_telefone(tabela, telefone))
                                valid2 = True
                            elif op == 3:
                                cpf = input("Informe o CPF do cliente:\n")
                                print(buscar_cpf(tabela, telefone))
                                valid2 = True
                            elif op == 4:
                                codigo = input("Informe o codigo do cliente:\n")
                                print(buscar_codigo(tabela, codigo))
                                valid2 = True
                            elif op == 0:
                                valid2 = True
                        valid1 = True
                    elif op == 2:
                        menu.menu_consulta()
                        valid2 = False
                        op = int(input())
                        tabela = 'fornecedores'
                        while valid2 == False:
                            if op == 1:
                                nome = input("Informe o nome do fornecedor:\n")
                                print(buscar_nome(tabela, nome))
                                valid2 = True
                            elif op == 2:
                                telefone = input("Informe o telefone do fornecedor:\n")
                                print(buscar_telefone(tabela, telefone))
                                valid2 = True
                            elif op == 3:
                                cpf = input("Informe o CNPJ do fornecedor:\n")
                                print(buscar_cpf(tabela, cpf))
                                valid2 = True
                            elif op == 4:
                                codigo = input("Informe o codigo do fornecor:\n")
                                print(buscar_codigo(tabela, cpf))
                                valid2 = True
                            elif op == 0:
                                valid2 = True
                        valid1 = True
                    elif op == 3:
                        menu.menu_consulta()
                        valid2 = False
                        op = int(input())
                        tabela = otica
                        while valid2 == False:
                            if op == 1:
                                nome = input("Informe o nome da otica:\n")
                                print(buscar_nome(tabela, nome))
                                valid2 = True
                            elif op == 2:
                                telefone = input("Informe o telefone da otica:\n")
                                print(buscar_telefone(tabela, telefone))
                                valid2 = True
                            elif op == 3:
                                cpf = input("Informe o CNPJ da otica:\n")
                                print(buscar_cpf(tabela, cpf))
                                valid2 = True
                            elif op == 4:
                                codigo = input("Informe o codigo da otica:\n")
                                print(buscar_codigo(tabela, codigo))
                                valid2 = True
                            elif op == 0:
                                valid2 = True
                        valid1 = True
                    elif op == 4:
                        pass
                    elif op == 0:
                        valid0 = True
        elif op == 4:
            pass
        elif op == 0:
            break


                            

                                

if __name__ == '__main__':
    main()
            