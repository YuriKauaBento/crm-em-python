from funcoes.database.database import *

def alteracao(codigo,nome='',cpf='',telefone='',endereco=''):
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


def excluir(codigo=None, cpf=None):
    conexao = conectar()
    cursor = conexao.cursor()

    if codigo:
        cursor.execute(
            "UPDATE clientes SET ativo = 0 WHERE codigo = ?",
            (codigo,)
        )

    elif cpf:
        cursor.execute(
            "UPDATE clientes SET ativo = 0 WHERE cpf = ?",
            (cpf,)
        )

    else:
        print("Nenhum codigo ou cpf foi informado.")
        conexao.close()

    conexao.commit()

    if cursor.rowcount > 0:
        sucesso = "Cadastro cancelado com sucesso!"
    else:
        sucesso = "Cliente não encontrado."

    conexao.close()
    return sucesso