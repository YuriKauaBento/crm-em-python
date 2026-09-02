from funcoes.Cadastro.cadastro_cliente import *
from funcoes.menu.menu import *
from funcoes.Consulta.consulta import *
from funcoes.Alterar.alterar import *

def main():
    while True:
        try:
            op = int(input(Menu_inicial().exibir()))

            if op == 1:
                op_cadastro = int(input(Menu_cadastro().exibir()))
                if op_cadastro == 1:
                    cliente = Cliente()
                    cliente.cadastrar()
                    print('Cliente cadastrado com sucesso!')
                elif op_cadastro == 2:
                    fornecedor = Fornecedor()
                    fornecedor.cadastrar()
                    print('Fornecedor cadastrado com sucesso!')
                elif op_cadastro == 3:
                    otica = Otica()
                    otica.cadastrar()
                    print('Otica cadastrada com sucesso!')
                elif op_cadastro == 4:
                    op_alteracao = int(input(Menu_alteracao().exibir()))
                elif op_cadastro == 0:
                    continue
                else:
                    print("Opcao invalida!")

            elif op == 0:
                break
            
            elif op == 2:
                op_consulta = None
                while op_consulta not in (0,1,2,3,4):
                    try:
                        op_consulta = int(input(Menu_consulta().exibir()))
                        if op_consulta not in (0,1,2,3,4):
                            print('Opcao invalida!')
                    except ValueError:
                        print('Digite apenas numeros!')

                if op_consulta == 1:
                    consulta = int(input(Menu_consulta().menu_consulta()))
                    if consulta == 1:
                        a = input("DIgite o nome: ")
                        print(buscar_nome(a))
                    elif consulta == 2:
                        a = input("Digite o telefone:")
                        print(buscar_telefone(a))
                    elif consulta == 3:
                        a = input("Digite o CPF/CNPJ: ")
                        print(buscar_cpf(a))
                    elif consulta == 4:
                        a = input("Digite o codigo: ")
                        print(buscar_codigo(a))

            #elif op == 3:

        except sqlite3.OperationalError as e:
            print(f"Erro no SQLite: {e}")


if __name__ == '__main__':
    main()
            