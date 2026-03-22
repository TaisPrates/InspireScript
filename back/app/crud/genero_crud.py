from mysql.connector import Error
from app.config.connection import conectar


def listar_generos(conexao):
    cursor = None
    try:
        cursor = conexao.cursor()
        sql = "SELECT id, nome FROM genero ORDER BY nome"
        cursor.execute(sql)
        return cursor.fetchall()

    except Exception as erro:
        print(f"Erro ao listar gêneros: {erro}")
        return []

    finally:
        if cursor is not None:
            cursor.close()


def inserir_genero(nome, tipo, id_genero_pai=None):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO genero (nome, tipo, id_genero_pai)
        VALUES (%s, %s, %s)
        """

        valores = (nome, tipo, id_genero_pai)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Gênero inserido com sucesso!")

    except Error as erro:
        print(f"Erro ao inserir gênero: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def listar_generos():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_genero, nome, tipo, id_genero_pai
        FROM genero
        """
        cursor.execute(sql)

        resultados = cursor.fetchall()

        if resultados:
            for genero in resultados:
                print(genero)
        else:
            print("Nenhum gênero cadastrado.")

    except Error as erro:
        print(f"Erro ao listar gêneros: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_genero_por_id(id_genero):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_genero, nome, tipo, id_genero_pai
        FROM genero
        WHERE id_genero = %s
        """
        valor = (id_genero,)

        cursor.execute(sql, valor)
        resultado = cursor.fetchone()

        if resultado:
            print(resultado)
        else:
            print("Gênero não encontrado.")

    except Error as erro:
        print(f"Erro ao buscar gênero: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def atualizar_genero(id_genero, nome, tipo, id_genero_pai=None):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        UPDATE genero
        SET nome = %s,
            tipo = %s,
            id_genero_pai = %s
        WHERE id_genero = %s
        """

        valores = (nome, tipo, id_genero_pai, id_genero)

        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Gênero atualizado com sucesso!")
        else:
            print("Nenhum gênero encontrado com esse id.")

    except Error as erro:
        print(f"Erro ao atualizar gênero: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def deletar_genero(id_genero):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM genero WHERE id_genero = %s"
        valor = (id_genero,)

        cursor.execute(sql, valor)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Gênero deletado com sucesso!")
        else:
            print("Nenhum gênero encontrado com esse id.")

    except Error as erro:
        print(f"Erro ao deletar gênero: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()