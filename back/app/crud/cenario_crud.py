from mysql.connector import Error
from app.config.connection import conectar


def inserir_cenario(nome, descricao=None, tipo="outro"):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO cenario (nome, descricao, tipo)
        VALUES (%s, %s, %s)
        """

        valores = (nome, descricao, tipo)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Cenário inserido com sucesso!")

    except Error as erro:
        print(f"Erro ao inserir cenário: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def listar_cenarios():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_cenario, nome, descricao, tipo, data_criacao
        FROM cenario
        """
        cursor.execute(sql)

        resultados = cursor.fetchall()

        if resultados:
            for cenario in resultados:
                print(cenario)
        else:
            print("Nenhum cenário cadastrado.")

    except Error as erro:
        print(f"Erro ao listar cenários: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_cenario_por_id(id_cenario):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_cenario, nome, descricao, tipo, data_criacao
        FROM cenario
        WHERE id_cenario = %s
        """

        valor = (id_cenario,)

        cursor.execute(sql, valor)
        resultado = cursor.fetchone()

        if resultado:
            print(resultado)
        else:
            print("Cenário não encontrado.")

    except Error as erro:
        print(f"Erro ao buscar cenário: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def atualizar_cenario(id_cenario, nome, descricao, tipo):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        UPDATE cenario
        SET nome = %s,
            descricao = %s,
            tipo = %s
        WHERE id_cenario = %s
        """

        valores = (nome, descricao, tipo, id_cenario)

        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Cenário atualizado com sucesso!")
        else:
            print("Nenhum cenário encontrado com esse id.")

    except Error as erro:
        print(f"Erro ao atualizar cenário: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def deletar_cenario(id_cenario):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM cenario WHERE id_cenario = %s"
        valor = (id_cenario,)

        cursor.execute(sql, valor)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Cenário deletado com sucesso!")
        else:
            print("Nenhum cenário encontrado com esse id.")

    except Error as erro:
        print(f"Erro ao deletar cenário: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()