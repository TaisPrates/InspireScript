import psycopg2
from psycopg2 import Error
from core.config.config_banco import conectar

def inserir_subgenero(nome, id_genero_pai):
    """Cadastra um subgênero vinculado a um gênero pai."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO subgenero (nome, id_genero_pai) VALUES (%s, %s)"
        cursor.execute(sql, (nome.strip(), id_genero_pai))
        conexao.commit()
        print(f"✅ Subgênero '{nome}' vinculado com sucesso!")
    except psycopg2.errors.ForeignKeyViolation:
        print(f"❌ Erro: O Gênero Pai com ID {id_genero_pai} não existe.")
    except psycopg2.errors.UniqueViolation:
        print(f"⚠️ Erro: Este subgênero já está cadastrado para este gênero pai.")
    except Error as e:
        print(f"❌ Erro ao inserir subgênero: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_subgeneros():
    """Lista subgêneros mostrando o nome do gênero pai (usando JOIN)."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        # Aqui fazemos um JOIN para o terminal não mostrar apenas números, mas nomes!
        sql = """
            SELECT s.id_subgenero, s.nome, g.nome 
            FROM subgenero s
            JOIN genero g ON s.id_genero_pai = g.id_genero
            ORDER BY g.nome, s.nome
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        if resultados:
            print("\n" + "="*45)
            print(f"{'ID':<4} | {'SUBGÊNERO':<18} | {'GÊNERO PAI':<15}")
            print("="*45)
            for s in resultados:
                print(f"{s[0]:<4} | {s[1]:<18} | {s[2]:<15}")
            print("="*45)
        else:
            print("\n📭 Nenhum subgênero cadastrado.")
    except Error as e:
        print(f"❌ Erro ao listar subgêneros: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_subgenero(id_subgenero, novo_nome):
    """Atualiza o nome do subgênero."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "UPDATE subgenero SET nome = %s WHERE id_subgenero = %s"
        cursor.execute(sql, (novo_nome.strip(), id_subgenero))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"✅ Subgênero ID {id_subgenero} atualizado para '{novo_nome}'!")
        else:
            print(f"🔍 Subgênero ID {id_subgenero} não encontrado.")
    except Error as e:
        print(f"❌ Erro ao atualizar: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_subgenero(id_subgenero):
    """Deleta um subgênero (respeitando a restrição de integridade)."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM subgenero WHERE id_subgenero = %s"
        cursor.execute(sql, (id_subgenero,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"🗑️ Subgênero ID {id_subgenero} deletado.")
        else:
            print(f"🔍 Subgênero não encontrado.")
    except psycopg2.errors.ForeignKeyViolation:
        print("⚠️ Não é possível deletar: este subgênero está sendo usado em alguma ideia.")
    except Error as e:
        print(f"❌ Erro ao deletar: {e}")
    finally:
        cursor.close()
        conexao.close()