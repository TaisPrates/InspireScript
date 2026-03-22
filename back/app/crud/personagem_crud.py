from mysql.connector import Error
from app.config.connection import conectar


def inserir_personagem(nome, descricao=None, papel="coadjuvante"):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO personagem (nome, descricao, papel)
        VALUES (%s, %s, %s)
        """

        valores = (nome, descricao, papel)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Personagem inserido com sucesso!")

    except Error as erro:
        print(f"Erro ao inserir personagem: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def listar_personagens():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_personagem, nome, descricao, papel, data_criacao
        FROM personagem
        """
        cursor.execute(sql)

        resultados = cursor.fetchall()

        if resultados:
            for personagem in resultados:
                print(personagem)
        else:
            print("Nenhum personagem cadastrado.")

    except Error as erro:
        print(f"Erro ao listar personagens: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_personagem_por_id(id_personagem):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT id_personagem, nome, descricao, papel, data_criacao
        FROM personagem
        WHERE id_personagem = %s
        """

        valor = (id_personagem,)

        cursor.execute(sql, valor)
        resultado = cursor.fetchone()

        if resultado:
            print(resultado)
        else:
            print("Personagem não encontrado.")

    except Error as erro:
        print(f"Erro ao buscar personagem: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def atualizar_personagem(id_personagem, nome, descricao, papel):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        UPDATE personagem
        SET nome = %s,
            descricao = %s,
            papel = %s
        WHERE id_personagem = %s
        """

        valores = (nome, descricao, papel, id_personagem)

        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Personagem atualizado com sucesso!")
        else:
            print("Nenhum personagem encontrado com esse id.")

    except Error as erro:
        print(f"Erro ao atualizar personagem: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def deletar_personagem(id_personagem):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM personagem WHERE id_personagem = %s"
        valor = (id_personagem,)

        cursor.execute(sql, valor)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Personagem deletado com sucesso!")
        else:
            print("Nenhum personagem encontrado com esse id.")

    except Error as erro:
        print(f"Erro ao deletar personagem: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()