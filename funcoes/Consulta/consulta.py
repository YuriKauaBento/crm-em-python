from funcoes.database.database import *

def validacao(cliente, conexao, tabela):
    try:
        if not cliente:
            return "CADASTRO NÃO ENCONTRADO!"

        if isinstance(cliente, tuple):
            registros = [cliente]

        resultado = []

        for registro in registros:
            if tabela == 'usuarios':
                codigo = registro[2]
                nome = registro[1]

                resultado.append(
                    "---PERFIL DO USUARIO---\n"
                    f"CODIGO: {codigo}"
                    f"NOME: {registro}"
                )
            else:
                nome = registro[2]
                codigo = registro[1]
                doc = registro[3]
                end = registro[4]
                tel = registro[5]

                if len(doc) == 11:
                    doc = f'{doc[:3]}.{doc[3:6]}.{doc[6:9]}-{doc[9:]}'
                elif len(doc)== 14:
                    doc = f'{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[12:]}'

                if len(tel) == 11:
                    tel = f'({tel[:2]}) {tel[2:7]}-{tel[7:]}'
                elif len(tel) == 10:
                    tel = f'({tel[:2]}) {tel[2:6]}-{tel[6:]}'

                resultado.append(
                    "---DADOS DO CADASTRO---\n"
                    f"CODIGO: {codigo}\n"
                    f"NOME/RAZAO SOCIAL: {nome}\n"
                    f"CPF/CNPJ: {doc}\n"
                    f"ENDERECO: {end}\n"
                    f"TELEFONE: {tel}\n"
                )

        return "\n".join(resultado)
    finally:
        conexao.close()

        

def buscar_codigo(tabela, usuario):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE usuario = ? AND ativo = 1",
        (usuario,)
    )

    cliente = cursor.fetchone()

    return validacao(cliente, conexao, tabela)



def buscar_nome(tabela, nome):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE nome LIKE ? AND ativo = 1",
        (f"%{nome}%",)
    )

    cliente = cursor.fetchall()

    return validacao(cliente, conexao, tabela)


def buscar_cpf(tabela, cpf):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE doc = ? AND ativo = 1",
        (cpf,)
    )

    cliente = cursor.fetchone()

    return validacao(cliente, conexao, tabela)


def buscar_telefone(tabela, tel):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        f"SELECT * FROM {tabela} WHERE telefone = ? AND ativo = 1",
        (tel,)
    )

    cliente = cursor.fetchone()

    return validacao(cliente, conexao, tabela)