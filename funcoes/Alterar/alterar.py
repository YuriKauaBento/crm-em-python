from funcoes.database.database import *

def localizar(usuario, tabela):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(f"SELECT EXISTS(SELECT 1 FROM {tabela} WHERE usuario = ? AND ativo = 1)",
            (usuario,)
            )
        resultado = cursor.fetchone()[0]
        return bool(resultado)
    
    except sqlite3.OperationalError as e:
        print(f"ERRO NO SQLITE: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def alteracao(usuario,tabela,nome=None,doc=None,telefone=None,endereco=None):
    conexao = conectar()
    cursor = conexao.cursor()

    campos = []
    valores = []

    if nome:
        campos.append("nome = ?")
        valores.append(nome)

    if telefone:
        campos.append("telefone = ?")
        valores.append(telefone)

    if doc:
        campos.append("doc = ?")
        valores.append(doc)

    if endereco:
        campos.append("endereco = ?")
        valores.append(endereco)

    if not campos:
        print("NENHUMA INFORMACAO FOI ALTERADA.")
        conexao.close()
        return

    valores.append(usuario)

    db = f"""
        UPDATE {tabela}
        SET {",".join(campos)}
        WHERE usuario = ?
        """

    cursor.execute(db, valores)
    conexao.commit()

    conexao.close()
    

def excluir(tabela):
    conexao = conectar()
    cursor = conexao.cursor()

    if tabela == '1':
        tabela = "clientes"
    elif tabela == '2':
        tabela = "fornecedores"
    elif tabela == '3':
        tabela = "oticas"
    elif tabela == '4':
        return
    else:
        return "OPCAO INVALIDA!"

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

    if usuario:
        cursor.execute(f"UPDATE {tabela} SET ativo = 0 WHERE usuario = ?",
            (usuario,)
            )

    elif cpf:
        cursor.execute(f"UPDATE {tabela} SET ativo = 0 WHERE doc = ?",
            (cpf,)
            )

    if cursor.rowcount > 0:
        sucesso = "CADASTRO CANCELADO COM SUCESSO!"
    else:
        sucesso = "CLIENTE NAO ENCONTRADO."

    conexao.commit()
    conexao.close()
    return sucesso