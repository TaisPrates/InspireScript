import psycopg2
from psycopg2 import Error
from core.config.config_banco import conectar

def inserir_genero(nome):
    """Cadastra um novo gênero principal (ex: Fantasia, Terror)."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO genero (nome) VALUES (%s)"
        cursor.execute(sql, (nome.strip(),))
        conexao.commit()
        print(f"✅ Gênero '{nome}' cadastrado com sucesso!")
    except psycopg2.errors.UniqueViolation:
        print(f"⚠️ Erro: O gênero '{nome}' já existe no banco de dados.")
    except Error as e:
        print(f"❌ Erro ao inserir gênero: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_generos():
    """Exibe todos os gêneros cadastrados de forma organizada."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "SELECT id_genero, nome FROM genero ORDER BY id_genero"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        if resultados:
            print("\n" + "="*30)
            print("      LISTA DE GÊNEROS")
            print("="*30)
            for g in resultados:
                print(f"ID: {g[0]:<3} | Nome: {g[1]}")
            print("="*30)
        else:
            print("\n📭 Nenhum gênero cadastrado ainda.")
    except Error as e:
        print(f"❌ Erro ao listar gêneros: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_genero(id_genero, novo_nome):
    """Altera o nome de um gênero existente pelo ID."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "UPDATE genero SET nome = %s WHERE id_genero = %s"
        cursor.execute(sql, (novo_nome.strip(), id_genero))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"✅ Gênero ID {id_genero} atualizado para '{novo_nome}'!")
        else:
            print(f"🔍 Nenhum gênero encontrado com o ID {id_genero}.")
    except Error as e:
        print(f"❌ Erro ao atualizar gênero: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_genero(id_genero):
    """Remove um gênero do banco de dados."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM genero WHERE id_genero = %s"
        cursor.execute(sql, (id_genero,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"🗑️ Gênero ID {id_genero} deletado com sucesso!")
        else:
            print(f"🔍 Nenhum gênero encontrado com o ID {id_genero}.")
    except psycopg2.errors.ForeignKeyViolation:
        print("⚠️ Erro: Não é possível deletar este gênero pois existem histórias vinculadas a ele.")
    except Error as e:
        print(f"❌ Erro ao deletar gênero: {e}")
    finally:
        cursor.close()
        conexao.close()