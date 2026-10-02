from funcoes.Cadastro.cadastro_cliente import *
from funcoes.menu.menu import *
from funcoes.Consulta.consulta import *
from funcoes.Alterar.alterar import *
from funcoes.Log_In.login import *

def main():
    criar_tabelas()
    perfil = None

    while True:
        menu = Menu_login()
        print(menu.exibir())
        usuario = input("USUARIO: ").upper()
        senha = input("SENHA: ")
        login = Sessao(usuario)
        resultado = login.validar_usuario(usuario, senha)
        if isinstance(resultado, tuple):
            perfil = resultado[1]
            print("lOGIN EFETUADO COM SUCESSO!")
            break
        else:
            print(resultado)
    
    while True:
        valid0 = False
        menu = Menu_inicial()
        print(menu.exibir())
        op = int(input())
        if op == 1:
            while valid0 == False:
                menu = Menu_cadastro()
                print(menu.exibir())
                op = int(input())
                if op == 1:
                    nome = input("NOME:\n").upper()
                    cpf = input("CPF:\n").upper()
                    cpf = f'{cliente[:3]}.{cliente[3:6]}.{cliente[6:9]}-{cliente[9:]}'
                    endereco = input("ENDERECO:\n").upper()
                    telefone = input("TELEFONE:\n").upper()

                    cliente = Cliente()
                    codigo = cliente.cadastrar(nome, cpf, endereco, telefone)
                    print(f"CLIENTE CADASTRADO COM SUCESSO! CODIGO: {codigo}")
                    valid0 = True
                elif op == 2:
                    nome = input("RAZAO SOCIAL:\n").upper()
                    cpf = input("CNPJ:\n").upper()
                    cpf = f'{cliente[:2]}.{cliente[2:5]}.{cliente[5:8]}/{cliente[8:12]}-{cliente[12:]}'
                    endereco = input("ENDERECO:\n").upper()
                    telefone = input("TELEFONE:\n").upper()

                    fornecedor = Fornecedor()
                    fornecedor.cadastrar(nome, cpf, endereco, telefone)
                    print(f"FORNECEDOR CADASTRADO COM SUCESSO! CODIGO: {fornecedor}")
                    valid0 = True
                elif op == 3:
                    nome = input("RAZAO SOCIAL:\n").upper()
                    cpf = input("CNPJ:\n").upper()
                    cpf = f'{cliente[:2]}.{cliente[2:5]}.{cliente[5:8]}/{cliente[8:12]}-{cliente[12:]}'
                    endereco = input("ENDERECO:\n").upper()
                    telefone = input("TELEFONE:\n").upper()

                    otica = Otica()
                    otica.cadastrar(nome, cpf, endereco, telefone)
                    print(f"OTICA CADASTRADA COM SUCESSO! CODIGO: {otica}")
                    valid0 = True
                elif op == 4:
                    valid1 = False
                    while valid1 == False:
                        menu = Menu_alteracao()
                        print(menu.exibir())
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
                            break

                        usuario = input("INFORME O USUARIO QUE DESEJA ALTERAR:\n")
                        loc = localizar(usuario, tabela)
                        if loc == False:
                            print("O USUARIO NAO EXISTE!")
                        else:
                            print("INFORME APENAS AS INFORMACOES ALTERADAS: ")
                            
                            nome = input("INFORME O NOME SE FOI ALTERADO: \n").upper()
                            cpf = input("INFORME O CPF/CNPJ SE FOI ALTERADO: \n").upper()
                            telefone = input("INFORME O TELEFONE SE FOI ALTERADO: \n").upper()
                            endereco = input("INFORME O ENDERECO SE FOI ALTERADO: \n").upper()
                            alteracao(usuario, tabela, nome, cpf, telefone, endereco)
                            print("ALTEARACAO CONCLUIDA!")
                            valid1 = True
                elif op == 5:
                    nome = input(("INFORME O NOME DO USUARIO: ")).upper()
                    senha = input(("INFORME A SENHA: ")).upper()
                    novo_perfil = input(("IFORME O NIVEL DE USUARIO: ")).lower()
                    usuario = Usuario(nome, senha, novo_perfil, perfil)
                    print(usuario.cadastrar())
                elif op == 0:
                    valid0 = True
        elif op == 2:
            while valid0 == False:
                menu = Menu_consulta()
                print(menu.exibir())
                valid1 = False
                op = int(input())
                while valid1 == False:
                    if op == 1:
                        print(menu.menu_consulta())
                        valid2 = False
                        op = int(input())
                        tabela = 'clientes'
                        while valid2 == False:
                            if op == 1:
                                nome = input("INFORME O NOME DO CLIENTE:\n").upper()
                                print(buscar_nome(tabela, nome))
                                valid2 = True
                            elif op == 2:
                                telefone = input("INFORME O TELEFONE DO CLIENTE:\n").upper()
                                print(buscar_telefone(tabela, telefone))
                                valid2 = True
                            elif op == 3:
                                cpf = input("INFORME O CPF DO CLIENTE:\n").upper()
                                print(buscar_cpf(tabela, cpf))
                                valid2 = True
                            elif op == 4:
                                codigo = input("INFORME O CODIGO DO CLIENTE:\n").upper()
                                print(buscar_codigo(tabela, codigo))
                                valid2 = True
                            elif op == 0:
                                valid2 = True
                        valid1 = True
                    elif op == 2:
                        print(menu.menu_consulta())
                        valid2 = False
                        op = int(input())
                        tabela = 'fornecedores'
                        while valid2 == False:
                            if op == 1:
                                nome = input("INFORME O NOME DO FORNECEDOR:\n").upper()
                                print(buscar_nome(tabela, nome))
                                valid2 = True
                            elif op == 2:
                                telefone = input("INFORME O TELEFONE DO FORNECEDOR:\n").upper()
                                print(buscar_telefone(tabela, telefone))
                                valid2 = True
                            elif op == 3:
                                cpf = input("INFORME O CNPJ DO FORNECEDOR:\n").upper()
                                print(buscar_cpf(tabela, cpf))
                                valid2 = True
                            elif op == 4:
                                codigo = input("INFORME O CODIGO DO FORNECEDOR:\n").upper()
                                print(buscar_codigo(tabela, codigo))
                                valid2 = True
                            elif op == 0:
                                valid2 = True
                        valid1 = True
                    elif op == 3:
                        print(menu.menu_consulta())
                        valid2 = False
                        op = int(input())
                        tabela = 'oticas'
                        while valid2 == False:
                            if op == 1:
                                nome = input("INFORME O NOME DA OTICA:\n")
                                print(buscar_nome(tabela, nome))
                                valid2 = True
                            elif op == 2:
                                telefone = input("INFORME O TELEFONE DA OTICA:\n")
                                print(buscar_telefone(tabela, telefone))
                                valid2 = True
                            elif op == 3:
                                cpf = input("INFORME O CNPJ DA OTICA:\n")
                                print(buscar_cpf(tabela, cpf))
                                valid2 = True
                            elif op == 4:
                                codigo = input("INFORME O CODIGO DA OTICA:\n")
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
            