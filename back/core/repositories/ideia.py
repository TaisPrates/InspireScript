import psycopg2
from psycopg2 import Error
from core.config.config_banco import conectar


def inserir_ideia(titulo, id_genero_principal, subtitulo=None, descricao=None):
    """Cadastra uma nova ideia literária vinculada a um gênero principal."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = """
            INSERT INTO ideia (titulo, subtitulo, descricao, id_genero_principal)
            VALUES (%s, %s, %s, %s)
        """
        # O subtitulo e a descricao podem ser None (null no banco)
        valores = (titulo.strip(), subtitulo, descricao, id_genero_principal)

        cursor.execute(sql, valores)
        conexao.commit()
        print(f"✨ Ideia '{titulo}' criada com sucesso!")

    except psycopg2.errors.ForeignKeyViolation:
        print(f"❌ Erro: O Gênero Principal (ID {id_genero_principal}) não existe.")
    except psycopg2.errors.CheckViolation:
        print("⚠️ Erro: O título não pode estar vazio.")
    except Error as e:
        print(f"❌ Erro ao inserir ideia: {e}")
    finally:
        cursor.close()
        conexao.close()


def listar_ideias():
    """Lista todas as ideias com seus respectivos gêneros principais."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = """
            SELECT i.id_ideia, i.titulo, i.subtitulo, g.nome, i.data_criacao
            FROM ideia i
            JOIN genero g ON i.id_genero_principal = g.id_genero
            ORDER BY i.data_criacao DESC
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        if resultados:
            print("\n" + "=" * 60)
            print(f"{'ID':<4} | {'TÍTULO':<25} | {'GÊNERO':<15}")
            print("=" * 60)
            for r in resultados:
                # Se houver subtítulo, exibe "Título: Subtítulo"
                titulo_completo = f"{r[1]}: {r[2]}" if r[2] else r[1]
                # Trunca o título se for muito longo para não quebrar a tabela
                titulo_display = (titulo_completo[:22] + '..') if len(titulo_completo) > 24 else titulo_completo

                print(f"{r[0]:<4} | {titulo_display:<25} | {r[3]:<15}")
            print("=" * 60)
        else:
            print("\n📭 Nenhuma ideia de história cadastrada ainda.")
    except Error as e:
        print(f"❌ Erro ao listar ideias: {e}")
    finally:
        cursor.close()
        conexao.close()


def buscar_ideia_detalhada(id_ideia):
    """Busca todos os detalhes de uma ideia específica."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = """
            SELECT i.titulo, i.subtitulo, i.descricao, g.nome, i.data_criacao
            FROM ideia i
            JOIN genero g ON i.id_genero_principal = g.id_genero
            WHERE i.id_ideia = %s
        """
        cursor.execute(sql, (id_ideia,))
        r = cursor.fetchone()

        if r:
            print("\n--- DETALHES DA IDEIA ---")
            print(f"Título: {r[0]}")
            if r[1]: print(f"Subtítulo: {r[1]}")
            print(f"Gênero Principal: {r[3]}")
            print(f"Criada em: {r[4].strftime('%d/%m/%Y %H:%M')}")
            print("-" * 25)
            print(f"Descrição:\n{r[2] if r[2] else 'Sem descrição.'}")
            print("-" * 25)
        else:
            print(f"🔍 Ideia ID {id_ideia} não encontrada.")
    except Error as e:
        print(f"❌ Erro ao buscar ideia: {e}")
    finally:
        cursor.close()
        conexao.close()


def atualizar_ideia(id_ideia, titulo, id_genero_principal, subtitulo=None, descricao=None):
    """Atualiza os dados de uma ideia existente."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = """
            UPDATE ideia 
            SET titulo = %s, subtitulo = %s, descricao = %s, id_genero_principal = %s
            WHERE id_ideia = %s
        """
        cursor.execute(sql, (titulo.strip(), subtitulo, descricao, id_genero_principal, id_ideia))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"✅ Ideia ID {id_ideia} atualizada!")
        else:
            print(f"🔍 Nenhuma ideia encontrada com o ID {id_ideia}.")
    except Error as e:
        print(f"❌ Erro ao atualizar ideia: {e}")
    finally:
        cursor.close()
        conexao.close()


def deletar_ideia(id_ideia):
    """Remove uma ideia do banco."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM ideia WHERE id_ideia = %s"
        cursor.execute(sql, (id_ideia,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"🗑️ Ideia ID {id_ideia} deletada com sucesso!")
        else:
            print(f"🔍 Ideia não encontrada.")
    except Error as e:
        print(f"❌ Erro ao deletar: {e}")
    finally:
        cursor.close()
        conexao.close()