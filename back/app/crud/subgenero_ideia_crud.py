from mysql.connector import Error
from app.config.connection import conectar


def inserir_subgenero_ideia(id_ideia, id_genero):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO subgenero_ideia (id_ideia, id_genero)
        VALUES (%s, %s)
        """

        valores = (id_ideia, id_genero)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Subgênero vinculado à ideia com sucesso!")

    except Error as erro:
        print(f"Erro ao inserir subgênero da ideia: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def listar_subgeneros_ideia():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_ideia, id_genero
        FROM subgenero_ideia
        """
        cursor.execute(sql)

        resultados = cursor.fetchall()

        if resultados:
            for registro in resultados:
                print(registro)
        else:
            print("Nenhum vínculo entre ideia e subgênero foi encontrado.")

    except Error as erro:
        print(f"Erro ao listar subgêneros da ideia: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_subgeneros_por_ideia(id_ideia):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_ideia, id_genero
        FROM subgenero_ideia
        WHERE id_ideia = %s
        """

        valor = (id_ideia,)

        cursor.execute(sql, valor)
        resultados = cursor.fetchall()

        if resultados:
            for registro in resultados:
                print(registro)
        else:
            print("Nenhum subgênero encontrado para essa ideia.")

    except Error as erro:
        print(f"Erro ao buscar subgêneros da ideia: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_ideias_por_subgenero(id_genero):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_ideia, id_genero
        FROM subgenero_ideia
        WHERE id_genero = %s
        """

        valor = (id_genero,)

        cursor.execute(sql, valor)
        resultados = cursor.fetchall()

        if resultados:
            for registro in resultados:
                print(registro)
        else:
            print("Nenhuma ideia encontrada para esse subgênero.")

    except Error as erro:
        print(f"Erro ao buscar ideias por subgênero: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def deletar_subgenero_ideia(id_ideia, id_genero):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        DELETE FROM subgenero_ideia
        WHERE id_ideia = %s AND id_genero = %s
        """

        valores = (id_ideia, id_genero)

        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Vínculo entre ideia e subgênero deletado com sucesso!")
        else:
            print("Nenhum vínculo encontrado com esses valores.")

    except Error as erro:
        print(f"Erro ao deletar subgênero da ideia: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()