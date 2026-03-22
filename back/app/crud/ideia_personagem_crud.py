from mysql.connector import Error
from app.config.connection import conectar


def inserir_ideia_personagem(id_ideia, id_personagem):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO ideia_personagem (id_ideia, id_personagem)
        VALUES (%s, %s)
        """

        valores = (id_ideia, id_personagem)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Personagem vinculado à ideia com sucesso!")

    except Error as erro:
        print(f"Erro ao inserir vínculo entre ideia e personagem: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def listar_ideia_personagem():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_ideia, id_personagem
        FROM ideia_personagem
        """
        cursor.execute(sql)

        resultados = cursor.fetchall()

        if resultados:
            for registro in resultados:
                print(registro)
        else:
            print("Nenhum vínculo entre ideia e personagem foi encontrado.")

    except Error as erro:
        print(f"Erro ao listar vínculos entre ideia e personagem: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_personagens_por_ideia(id_ideia):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_ideia, id_personagem
        FROM ideia_personagem
        WHERE id_ideia = %s
        """

        valor = (id_ideia,)

        cursor.execute(sql, valor)
        resultados = cursor.fetchall()

        if resultados:
            for registro in resultados:
                print(registro)
        else:
            print("Nenhum personagem encontrado para essa ideia.")

    except Error as erro:
        print(f"Erro ao buscar personagens da ideia: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_ideias_por_personagem(id_personagem):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_ideia, id_personagem
        FROM ideia_personagem
        WHERE id_personagem = %s
        """

        valor = (id_personagem,)

        cursor.execute(sql, valor)
        resultados = cursor.fetchall()

        if resultados:
            for registro in resultados:
                print(registro)
        else:
            print("Nenhuma ideia encontrada para esse personagem.")

    except Error as erro:
        print(f"Erro ao buscar ideias por personagem: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def deletar_ideia_personagem(id_ideia, id_personagem):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        DELETE FROM ideia_personagem
        WHERE id_ideia = %s AND id_personagem = %s
        """

        valores = (id_ideia, id_personagem)

        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Vínculo entre ideia e personagem deletado com sucesso!")
        else:
            print("Nenhum vínculo encontrado com esses valores.")

    except Error as erro:
        print(f"Erro ao deletar vínculo entre ideia e personagem: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()