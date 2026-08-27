from funcoes.database.database import *

def alteracao(codigo,nome=None,cpf=None,telefone=None,endereco=None):
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

    if cpf:
        campos.append("cpf = ?")
        valores.append(cpf)

    if endereco:
        campos.append("endereco = ?")
        valores.append(endereco)

    if not campos:
        print("Nenhuma informação foi alterada.")
        conexao.close()
        return

    valores.append(codigo)

    db = f"""
        UPDATE clientes
        SET{",".join(campos)}
        WHERE codigo = ?
"""

    cursor.execute(db, valores)
    conexao.commit()

    conexao.close()