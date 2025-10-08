import sqlite3
from contextlib import closing

DB_PATH = "escola.db"


def connect_db():
    conn = sqlite3.connect(DB_PATH)
    return conn


def create_table(conn):
    with conn:
        conn.execute("""CREATE TABLE alunos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR, idade INTEGER ,email VARCHAR )""")


def insert_aluno(conn, nome, idade, email):
    with conn:
        conn.execute("INSERT INTO alunos(nome, idade, email) VALUES (?, ?, ?)",(nome, idade, email),)


def list_alunos(conn):
    with closing(conn.cursor()) as cur:
        cur.execute("SELECT * FROM alunos")
        rows = cur.fetchall()

        print("■ LISTAR TODOS")
        for r in rows:
            print(r)
        if not rows:
            print("(sem registros)")
        print("-" * 50)


def get_aluno_by_id(conn, aluno_id):
    with closing(conn.cursor()) as cur:
        cur.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,))
        row = cur.fetchone()

        print(f"■ BUSCAR POR ID (id={aluno_id}) ->", row)
        print("-" * 50)
        return row


def update_aluno(conn, aluno_id, nome=None, idade=None, email=None):
    campos = []
    valores = []

    if nome is not None:
        campos.append("nome = ?")
        valores.append(nome)
    if idade is not None:
        campos.append("idade = ?")
        valores.append(idade)
    if email is not None:
        campos.append("email = ?")
        valores.append(email)

    if not campos:
        print("Nenhum campo para atualizar.")
        return

    valores.append(aluno_id)
    sql = f"UPDATE alunos SET {"," .join(campos)} WHERE id = ?"  # UPDATE alunos SET ... WHERE id = ?

    with conn:
        conn.execute(sql, tuple(valores))

    print(f"✏■ ATUALIZAR (id={aluno_id})")
    get_aluno_by_id(conn, aluno_id)


def delete_aluno(conn, aluno_id):
    with conn:
        conn.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
    print(f"■■ DELETAR (id={aluno_id}) concluído.")
    print("-" * 50)


def main():
    conn = connect_db()
    print("■ Conexão criada com", DB_PATH)

    create_table(conn)
    print("■ Tabela 'alunos' criada/garantida.")
    print("-" * 50)

    print("■ INSERIR REGISTROS")
    insert_aluno(conn, "Ana Silva", 20, "ana.silva@example.com")
    insert_aluno(conn, "Bruno Souza", 22, "bruno.souza@example.com")
    print("-" * 50)

    list_alunos(conn)
    get_aluno_by_id(conn, 1)
    update_aluno(conn, 2, email="bruno.souza@faculdade.edu.br")
    delete_aluno(conn, 1)
    list_alunos(conn)

    conn.close()
    print("■ Conexão fechada.")


if __name__ == "__main__":
    main()
