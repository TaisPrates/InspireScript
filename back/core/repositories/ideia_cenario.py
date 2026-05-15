import psycopg2
from psycopg2 import Error
from core.config.config_banco import conectar


def vincular_cenario_ideia(id_ideia, id_cenario):
    """Vincula um cenário a uma ideia específica."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO ideia_cenario (id_ideia, id_cenario) VALUES (%s, %s)"
        cursor.execute(sql, (id_ideia, id_cenario))
        conexao.commit()
        print(f"✅ Cenário {id_cenario} vinculado com sucesso à Ideia {id_ideia}!")

    except psycopg2.errors.UniqueViolation:
        print("⚠️ Este cenário já está vinculado a esta ideia.")
    except psycopg2.errors.ForeignKeyViolation:
        print("❌ Erro: O ID da Ideia ou do Cenário não existe no banco.")
    except Error as e:
        print(f"❌ Erro ao vincular: {e}")
    finally:
        cursor.close()
        conexao.close()


def listar_cenarios_da_ideia(id_ideia):
    """Lista todos os nomes e tipos de cenários de uma história."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        # JOIN para buscar os detalhes do cenário através da tabela de ligação
        sql = """
            SELECT c.nome, c.tipo
            FROM cenario c
            JOIN ideia_cenario ic ON c.id_cenario = ic.id_cenario
            WHERE ic.id_ideia = %s
            ORDER BY c.nome
        """
        cursor.execute(sql, (id_ideia,))
        resultados = cursor.fetchall()

        if resultados:
            print(f"\n🌍 LOCAÇÕES DA IDEIA #{id_ideia}:")
            print("-" * 40)
            for r in resultados:
                tipo = f"({r[1]})" if r[1] else ""
                print(f"📍 {r[0]:<20} {tipo}")
            print("-" * 40)
        else:
            print(f"\nℹ️ A Ideia #{id_ideia} ainda não possui cenários vinculados.")
    except Error as e:
        print(f"❌ Erro ao listar cenários: {e}")
    finally:
        cursor.close()
        conexao.close()


def remover_cenario_da_ideia(id_ideia, id_cenario):
    """Remove a ligação entre um cenário e uma ideia."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM ideia_cenario WHERE id_ideia = %s AND id_cenario = %s"
        cursor.execute(sql, (id_ideia, id_cenario))
        conexao.commit()

        if cursor.rowcount > 0:
            print("🗑️ Vínculo de cenário removido.")
        else:
            print("🔍 Vínculo não encontrado.")
    except Error as e:
        print(f"❌ Erro ao remover vínculo: {e}")
    finally:
        cursor.close()
        conexao.close()