import sqlite3

conexao = sqlite3.connect("biblioteca.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponibilidade CHAR(1) CHECK(disponibilidade IN('S','N'))
    )              
""")

def cadastrar_livro(titulo, autor, ano):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, disponibilidade)
        VALUES (?,?,?,?)""", (titulo, autor, ano, "S"))

        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Livro {titulo} Adicionado com Sucesso!")
        else:
            print(f"Erro ao cadastrar o Livro {titulo}")

    except sqlite3.Error as error:
        print("Erro ao cadastrar o Livro {error}")

    finally:
        if conexao:
            conexao.close()

titulo = input("Digite o Título do Livro: ").lower().strip()
autor = input("Digite o Nome do Autor: ").lower().strip()
ano = int(input(f"Digite o Ano de Publicação de {titulo}: "))
cadastrar_livro(titulo, autor, ano)

def listar_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros")
        for linha in cursor.fetchall():
            print(f"ID: {linha[0]}\nTítulo:{linha[1]}\nAutor:{linha[2]}\nAno:{linha[3]}\nDisponibilidade:{linha[4]}")

    except sqlite3.error as error:
        print("Erro ao listar o Livro {error}")

    finally:
        if conexao:
            conexao.close
listar_livros()