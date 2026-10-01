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
    

def excluir(tabela=None, usuario=None, cpf=None):
    conexao = conectar()
    cursor = conexao.cursor()

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