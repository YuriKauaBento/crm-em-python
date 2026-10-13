from funcoes.database.database import *

def validacao(cliente, conexao, tabela):
    conexao.close()
    for i in enumerate(cliente):
        if tabela == 'usuarios':
            return ('--- PERFIL DO USUARIO ---\n'
                    f'COD: {cliente[i][1]}\n'
                    f'NOME: {cliente[i][2]}\n'
                    )
        elif tabela != 'usuarios':
            doc = cliente[i][3]
            tel = cliente[i][5]
            if tel > 10:
                tel_format = f'({tel[:2]}) {tel[2:7]}-{tel[7:]}'
            else:
                tel_format = f'({tel[:2]}) {tel[2:6]}-{tel[6:]}'
            
            if len(doc) > 11:
                doc_format = f'{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[12:]}'
            else:
                doc_format = f'{doc[:3]}.{doc[3:6]}.{doc[6:9]}-{doc[9:]}'
            return ('--- PERFIL DO USUARIO ---\n'
                    f'NOME/RAZAO SOCIAL: {cliente[i][2]}\n'
                    f'COD: {cliente[i][1]}\n'
                    f'CPF/CNPJ: {doc_format}\n'
                    f'ENDERECO: {cliente[i][4]}\n'
                    f'TELEFONE: {tel_format}\n'
                    )
    if not cliente:
        return "CADASTRO NÃO ENCONTRADO!"
        

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