import sqlite3


def conectar():
    return sqlite3.connect("banco.db")


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT,
            endereco TEXT,
            telefone TEXT,
            ativo INTEGER NOT NULL DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fonecedor(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT,
            endereco TEXT,
            telefone TEXT,
            ativo INTEGER NOT NULL DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS otica(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT,
            endereco TEXT,
            telefone TEXT,
            ativo INTEGER NOT NULL DEFAULT 1
        )
    """)
    conexao.commit()
    conexao.close()


def excluir(tabela, id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(f"""
        UPDATE {tabela} SET ativo = 0 WHERE id = ?,
        {id,}
    """)

    conexao.close
    return "Cadastro desativado!"