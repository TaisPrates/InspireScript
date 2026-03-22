from mysql.connector import Error
from app.config.connection import conectar


def inserir_ideia(titulo, subtitulo, id_genero_principal, descricao):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO ideia (titulo, subtitulo, id_genero_principal, descricao)
        VALUES (%s, %s, %s, %s)
        """

        valores = (titulo, subtitulo, id_genero_principal, descricao)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Ideia inserida com sucesso!")

    except Error as erro:
        print(f"Erro ao inserir ideia: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def listar_ideias():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_ideia, titulo, subtitulo, id_genero_principal, descricao, data_criacao
        FROM ideia
        """
        cursor.execute(sql)

        resultados = cursor.fetchall()

        if resultados:
            for ideia in resultados:
                print(ideia)
        else:
            print("Nenhuma ideia cadastrada.")

    except Error as erro:
        print(f"Erro ao listar ideias: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_ideia_por_id(id_ideia):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_ideia, titulo, subtitulo, id_genero_principal, descricao, data_criacao
        FROM ideia
        WHERE id_ideia = %s
        """
        valor = (id_ideia,)

        cursor.execute(sql, valor)
        resultado = cursor.fetchone()

        if resultado:
            print(resultado)
        else:
            print("Ideia não encontrada.")

    except Error as erro:
        print(f"Erro ao buscar ideia: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def atualizar_ideia(id_ideia, titulo, subtitulo, id_genero_principal, descricao):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        UPDATE ideia
        SET titulo = %s,
            subtitulo = %s,
            id_genero_principal = %s,
            descricao = %s
        WHERE id_ideia = %s
        """

        valores = (titulo, subtitulo, id_genero_principal, descricao, id_ideia)

        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Ideia atualizada com sucesso!")
        else:
            print("Nenhuma ideia encontrada com esse id.")

    except Error as erro:
        print(f"Erro ao atualizar ideia: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def deletar_ideia(id_ideia):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM ideia WHERE id_ideia = %s"
        valor = (id_ideia,)

        cursor.execute(sql, valor)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Ideia deletada com sucesso!")
        else:
            print("Nenhuma ideia encontrada com esse id.")

    except Error as erro:
        print(f"Erro ao deletar ideia: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()