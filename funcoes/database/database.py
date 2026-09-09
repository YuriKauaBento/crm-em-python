import sqlite3

def validar_tabela(tabela):
    tabelas_validas = {
        "cliente",
        "fornecedor"
        "otica"
    }
    if tabela not in tabelas_validas:
        raise ValueError("Tabela invalida")



def conectar():
    return sqlite3.connect("banco.db")


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT GENERATED ALWAYS AS ('C' || id) STORED,
            nome TEXT NOT NULL,
            doc TEXT,
            endereco TEXT,
            telefone TEXT,
            ativo INTEGER NOT NULL DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fornecedor(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT GENERATED ALWAYS AS ('F' || id) STORED,
            nome TEXT NOT NULL,
            doc TEXT,
            endereco TEXT,
            telefone TEXT,
            ativo INTEGER NOT NULL DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS otica(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT GENERATED ALWAYS AS ('O' || id) STORED,
            nome TEXT NOT NULL,
            doc TEXT,
            endereco TEXT,
            telefone TEXT,
            ativo INTEGER NOT NULL DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        usuario TEXT GENERATED ALWAYS AS ('U' || id) STORED,
        senha_hash TEXT NOT NULL,
        perfil NOT NULL,
        ativo INTEGER NOT NULL DEFAULT 1
        )
""")
    
    conexao.commit()
    conexao.close()


