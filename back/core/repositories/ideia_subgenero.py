import psycopg2
from psycopg2 import Error
from core.config.config_banco import conectar


def vincular_subgenero(id_ideia, id_subgenero):
    """Vincula um subgênero a uma ideia específica."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO ideia_subgenero (id_ideia, id_subgenero) VALUES (%s, %s)"
        cursor.execute(sql, (id_ideia, id_subgenero))
        conexao.commit()
        print(f"✅ Subgênero {id_subgenero} vinculado à Ideia {id_ideia}!")

    except psycopg2.errors.UniqueViolation:
        print("⚠️ Esta ideia já possui este subgênero vinculado.")
    except psycopg2.errors.ForeignKeyViolation:
        print("❌ Erro: Verifique se o ID da Ideia ou do Subgênero realmente existem.")
    except Error as e:
        print(f"❌ Erro ao vincular: {e}")
    finally:
        cursor.close()
        conexao.close()


def listar_subgeneros_por_ideia(id_ideia):
    """Lista todos os subgêneros de uma história específica, com nomes."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        # Aqui fazemos um JOIN triplo: Ideia -> Ligação -> Subgênero
        sql = """
            SELECT s.nome 
            FROM subgenero s
            JOIN ideia_subgenero ids ON s.id_subgenero = ids.id_subgenero
            WHERE ids.id_ideia = %s
            ORDER BY s.nome
        """
        cursor.execute(sql, (id_ideia,))
        resultados = cursor.fetchall()

        if resultados:
            print(f"\n🏷️ Subgêneros da Ideia #{id_ideia}:")
            # Usa list comprehension para criar uma linha bonita separada por vírgulas
            nomes = ", ".join([r[0] for r in resultados])
            print(f" > {nomes}")
        else:
            print(f"\nℹ️ A Ideia #{id_ideia} ainda não possui subgêneros vinculados.")
    except Error as e:
        print(f"❌ Erro ao listar: {e}")
    finally:
        cursor.close()
        conexao.close()


def remover_vinculo_subgenero(id_ideia, id_subgenero):
    """Remove um subgênero específico de uma ideia."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM ideia_subgenero WHERE id_ideia = %s AND id_subgenero = %s"
        cursor.execute(sql, (id_ideia, id_subgenero))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"🗑️ Vínculo removido com sucesso!")
        else:
            print(f"🔍 Vínculo não encontrado.")
    except Error as e:
        print(f"❌ Erro ao remover vínculo: {e}")
    finally:
        cursor.close()
        conexao.close()