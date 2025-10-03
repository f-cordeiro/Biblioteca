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

def update_disp():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        id_livro = int(input("Digite o ID do Livro para Alterar a Disponibilidade: "))
        new_disp = input("Digite a nova Disponibilidade, ('S', 'N'): ")

        cursor.execute("""
        UPDATE livros SET disponibilidade = ? WHERE id = ?""", 
        (new_disp, id_livro))

        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Disponibilidade do ID:{id_livro} alterada com sucesso!")

        else:
            print(f"Nenhum livro encontrado com esse ID: {id_livro}")
    
    except sqlite3.error as error:
        print(f"erro ao tentar alterar disponibilidade", {error})

    finally:
        if conexao:
            conexao.close()

update_disp()
print("=" * 50)
listar_livros()

def del_livro(id):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM livros WHERE id =?", (id,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Livro removido com sucesso!")

        else:
            print("Nenhum Livro encontrado com ID fornecido!")
    
    except sqlite3.Error as error:
        print(f"Erro ao tentar deletar o Livro",{error})

    finally:
        if conexao:
            conexao.close()
deletar = int(input("Digite o ID do Livro que deseja deletar: "))
del_livro(deletar)
print("=" * 50)
listar_livros()

def menu():
    while True:
        print("\n Biblioteca Senai")
        print(" 1 - Cadastrar Livros")
        print(" 2 - Listar Livros")
        print(" 3 - Alterar Disponibilidade")
        print(" 4 - Remover Livros")
        print(" 5 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        match opcao:
            case "1": cadastrar_livro()
            case "2": listar_livros()
            case "3": update_disp()
            case "4": del_livro()
            case "5":
                print("Acesso encerrado")
                break

menu()