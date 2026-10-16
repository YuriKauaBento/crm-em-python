import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "banco.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def cadastro_db(tabela, nome=None, cpf=None, endereco=None, telefone=None, senha=None, perfil=None):
    conexao = conectar()
    cursor = conexao.cursor()
    perfis_validos = ['admin', 'chefe', 'comum']

    if tabela == 'usuarios':
        if perfil not in perfis_validos:
            return "PERFIL INVALIDO!"
        cursor.execute(f"""
            INSERT INTO {tabela} (nome, senha_hash, perfil)
            VALUES (?, ?, ?)
        """, (nome, senha, perfil))
    else:            
        cursor.execute(f"""
            INSERT INTO {tabela} (nome, doc, endereco, telefone) 
            VALUES (?, ?, ?, ?)
        """, (nome, cpf, endereco, telefone))
    
    conexao.commit()
    id_gerado = cursor.lastrowid

    cursor.execute(
        f"SELECT usuario FROM {tabela} WHERE id = ?", (id_gerado,)
    )

    codigo = cursor.fetchone()[0]
    conexao.close()
            
    return f'USUARIO CADASTRADO COM SUCESSO! CODIGO: {codigo}'


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
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
        CREATE TABLE IF NOT EXISTS fornecedores(
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
        CREATE TABLE IF NOT EXISTS oticas(
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


