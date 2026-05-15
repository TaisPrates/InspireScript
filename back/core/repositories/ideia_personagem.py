import psycopg2
from psycopg2 import Error
from core.config.config_banco import conectar


def vincular_personagem_ideia(id_ideia, id_personagem, id_papel):
    """Vincula um personagem a uma ideia com um papel específico."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = """
            INSERT INTO ideia_personagem (id_ideia, id_personagem, id_papel)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (id_ideia, id_personagem, id_papel))
        conexao.commit()
        print(f"✅ Personagem {id_personagem} agora faz parte da Ideia {id_ideia}!")

    except psycopg2.errors.UniqueViolation:
        print("⚠️ Este personagem já está vinculado a esta ideia.")
    except psycopg2.errors.ForeignKeyViolation:
        print("❌ Erro: Verifique se os IDs da Ideia, Personagem e Papel existem.")
    except Error as e:
        print(f"❌ Erro ao vincular: {e}")
    finally:
        cursor.close()
        conexao.close()


def listar_elenco_da_ideia(id_ideia):
    """Lista todos os personagens de uma ideia e seus respectivos papéis."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        # JOIN Triplo para pegar os nomes em vez de apenas IDs
        sql = """
            SELECT p.nome, pap.nome
            FROM ideia_personagem ip
            JOIN personagem p ON ip.id_personagem = p.id_personagem
            JOIN papel_personagem pap ON ip.id_papel = pap.id_papel
            WHERE ip.id_ideia = %s
            ORDER BY pap.nome
        """
        cursor.execute(sql, (id_ideia,))
        resultados = cursor.fetchall()

        if resultados:
            print(f"\n🎭 ELENCO DA IDEIA #{id_ideia}:")
            print("-" * 40)
            for r in resultados:
                print(f"👤 {r[0]:<20} | Papel: {r[1]}")
            print("-" * 40)
        else:
            print(f"\nℹ️ A Ideia #{id_ideia} ainda não possui personagens vinculados.")
    except Error as e:
        print(f"❌ Erro ao listar elenco: {e}")
    finally:
        cursor.close()
        conexao.close()


def mudar_papel_personagem(id_ideia, id_personagem, novo_id_papel):
    """Altera o papel de um personagem dentro de uma ideia específica."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = """
            UPDATE ideia_personagem 
            SET id_papel = %s 
            WHERE id_ideia = %s AND id_personagem = %s
        """
        cursor.execute(sql, (novo_id_papel, id_ideia, id_personagem))
        conexao.commit()

        if cursor.rowcount > 0:
            print("✅ Papel do personagem atualizado com sucesso!")
        else:
            print("🔍 Vínculo não encontrado.")
    except Error as e:
        print(f"❌ Erro ao atualizar papel: {e}")
    finally:
        cursor.close()
        conexao.close()


def remover_personagem_da_ideia(id_ideia, id_personagem):
    """Remove um personagem de uma ideia específica."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM ideia_personagem WHERE id_ideia = %s AND id_personagem = %s"
        cursor.execute(sql, (id_ideia, id_personagem))
        conexao.commit()

        if cursor.rowcount > 0:
            print("🗑️ Personagem removido da ideia.")
        else:
            print("🔍 Vínculo não encontrado.")
    except Error as e:
        print(f"❌ Erro ao remover: {e}")
    finally:
        cursor.close()
        conexao.close()