import psycopg2
from psycopg2 import Error
from core.config.config_banco import conectar

def inserir_papel(nome):
    """Cadastra um novo tipo de papel (ex: Protagonista, Antagonista)."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO papel_personagem (nome) VALUES (%s)"
        cursor.execute(sql, (nome.strip(),))
        conexao.commit()
        print(f"🎭 Papel '{nome}' cadastrado com sucesso!")
    except psycopg2.errors.UniqueViolation:
        print(f"⚠️ Erro: O papel '{nome}' já existe.")
    except Error as e:
        print(f"❌ Erro ao inserir papel: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_papeis():
    """Lista todos os papéis disponíveis para personagens."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "SELECT id_papel, nome FROM papel_personagem ORDER BY id_papel"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        if resultados:
            print("\n" + "="*25)
            print(f"{'ID':<4} | {'PAPEL':<15}")
            print("="*25)
            for r in resultados:
                print(f"{r[0]:<4} | {r[1]:<15}")
            print("="*25)
        else:
            print("\n📭 Nenhum papel cadastrado.")
    except Error as e:
        print(f"❌ Erro ao listar papéis: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_papel(id_papel, novo_nome):
    """Atualiza o nome de um papel existente."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "UPDATE papel_personagem SET nome = %s WHERE id_papel = %s"
        cursor.execute(sql, (novo_nome.strip(), id_papel))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"✅ Papel ID {id_papel} atualizado para '{novo_nome}'!")
        else:
            print(f"🔍 Papel ID {id_papel} não encontrado.")
    except Error as e:
        print(f"❌ Erro ao atualizar: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_papel(id_papel):
    """Remove um papel (se não estiver em uso)."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM papel_personagem WHERE id_papel = %s"
        cursor.execute(sql, (id_papel,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"🗑️ Papel ID {id_papel} removido.")
        else:
            print(f"🔍 Papel não encontrado.")
    except psycopg2.errors.ForeignKeyViolation:
        print("⚠️ Não é possível deletar: existem personagens vinculados a este papel.")
    except Error as e:
        print(f"❌ Erro ao deletar: {e}")
    finally:
        cursor.close()
        conexao.close()