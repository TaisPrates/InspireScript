from mysql.connector import Error
from app.config.connection import conectar


def inserir_ideia_cenario(id_ideia, id_cenario):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO ideia_cenario (id_ideia, id_cenario)
        VALUES (%s, %s)
        """

        valores = (id_ideia, id_cenario)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Cenário vinculado à ideia com sucesso!")

    except Error as erro:
        print(f"Erro ao inserir vínculo entre ideia e cenário: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def listar_ideia_cenario():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_ideia, id_cenario
        FROM ideia_cenario
        """
        cursor.execute(sql)

        resultados = cursor.fetchall()

        if resultados:
            for registro in resultados:
                print(registro)
        else:
            print("Nenhum vínculo entre ideia e cenário foi encontrado.")

    except Error as erro:
        print(f"Erro ao listar vínculos entre ideia e cenário: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_cenarios_por_ideia(id_ideia):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_ideia, id_cenario
        FROM ideia_cenario
        WHERE id_ideia = %s
        """

        valor = (id_ideia,)

        cursor.execute(sql, valor)
        resultados = cursor.fetchall()

        if resultados:
            for registro in resultados:
                print(registro)
        else:
            print("Nenhum cenário encontrado para essa ideia.")

    except Error as erro:
        print(f"Erro ao buscar cenários da ideia: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_ideias_por_cenario(id_cenario):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_ideia, id_cenario
        FROM ideia_cenario
        WHERE id_cenario = %s
        """

        valor = (id_cenario,)

        cursor.execute(sql, valor)
        resultados = cursor.fetchall()

        if resultados:
            for registro in resultados:
                print(registro)
        else:
            print("Nenhuma ideia encontrada para esse cenário.")

    except Error as erro:
        print(f"Erro ao buscar ideias por cenário: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def deletar_ideia_cenario(id_ideia, id_cenario):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        DELETE FROM ideia_cenario
        WHERE id_ideia = %s AND id_cenario = %s
        """

        valores = (id_ideia, id_cenario)

        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Vínculo entre ideia e cenário deletado com sucesso!")
        else:
            print("Nenhum vínculo encontrado com esses valores.")

    except Error as erro:
        print(f"Erro ao deletar vínculo entre ideia e cenário: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()