from funcoes.database.database import *

def localizar(codigo, tabela):
    validar_tabela(tabela)

    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(f"SELECT EXISTS(SELECT 1 FROM {tabela} WHERE id = ?",
            (codigo,)
            )
        resultado = cursor.fetchone()[0]
        return bool(resultado)
    
    except sqlite3.OperationalError as e:
        print(f"Erro no SQLite: {e}")
        return False
    finally:
        if conexao:
            conexao.close()

def alteracao(codigo,tabela,nome=None,doc=None,telefone=None,endereco=None):
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
        print("Nenhuma informação foi alterada.")
        conexao.close()
        return

    #valores.append(codigo)

    db = f"""
        UPDATE {tabela}
        SET {",".join(campos)}
        WHERE id = ?,
        {codigo,}
        """

    cursor.execute(db, valores)
    conexao.commit()

    conexao.close()
    

def excluir(tabela=None, id=None, cpf=None):
    conexao = conectar()
    cursor = conexao.cursor()

    if id:
        cursor.execute(f"UPDATE {tabela} SET ativo = 0 WHERE id = ?",
            (id,)
            )

    elif cpf:
        cursor.execute(f"UPDATE {tabela} SET ativo = 0 WHERE cpf = ?",
            (cpf,)
            )

    if cursor.rowcount > 0:
        sucesso = "Cadastro cancelado com sucesso!"
    else:
        sucesso = "Cliente não encontrado."

    conexao.commit()
    conexao.close()
    return sucesso