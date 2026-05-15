import psycopg2
from psycopg2 import Error
from core.config.config_banco import conectar

def inserir_personagem(nome, descricao=None):
    """Cadastra um novo personagem no banco de dados."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO personagem (nome, descricao) VALUES (%s, %s)"
        cursor.execute(sql, (nome.strip(), descricao))
        conexao.commit()
        print(f"👤 Personagem '{nome}' criado com sucesso!")
    except psycopg2.errors.CheckViolation:
        print("⚠️ Erro: O nome do personagem não pode estar vazio.")
    except Error as e:
        print(f"❌ Erro ao inserir personagem: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_personagens():
    """Lista todos os personagens cadastrados."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "SELECT id_personagem, nome, descricao FROM personagem ORDER BY nome"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        if resultados:
            print("\n" + "="*50)
            print(f"{'ID':<4} | {'NOME':<20} | {'DESCRIÇÃO'}")
            print("="*50)
            for p in resultados:
                # Trunca a descrição para não quebrar a visualização da lista
                desc = (p[2][:20] + '...') if p[2] and len(p[2]) > 20 else (p[2] or "---")
                print(f"{p[0]:<4} | {p[1]:<20} | {desc}")
            print("="*50)
        else:
            print("\n📭 Nenhum personagem cadastrado.")
    except Error as e:
        print(f"❌ Erro ao listar personagens: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_personagem_detalhado(id_personagem):
    """Exibe todos os detalhes e a data de criação de um personagem."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "SELECT nome, descricao, data_criacao FROM personagem WHERE id_personagem = %s"
        cursor.execute(sql, (id_personagem,))
        p = cursor.fetchone()

        if p:
            print(f"\n--- PERFIL DE: {p[0]} ---")
            print(f"Criado em: {p[2].strftime('%d/%m/%Y %H:%M')}")
            print(f"Descrição: {p[1] if p[1] else 'Sem descrição definida.'}")
            print("-" * 30)
        else:
            print(f"🔍 Personagem ID {id_personagem} não encontrado.")
    except Error as e:
        print(f"❌ Erro ao buscar personagem: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_personagem(id_personagem, novo_nome, nova_descricao):
    """Atualiza os dados de um personagem existente."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "UPDATE personagem SET nome = %s, descricao = %s WHERE id_personagem = %s"
        cursor.execute(sql, (novo_nome.strip(), nova_descricao, id_personagem))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"✅ Personagem ID {id_personagem} atualizado!")
        else:
            print(f"🔍 Personagem não encontrado.")
    except Error as e:
        print(f"❌ Erro ao atualizar: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_personagem(id_personagem):
    """Remove um personagem (se não houver vínculos impeditivos)."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM personagem WHERE id_personagem = %s"
        cursor.execute(sql, (id_personagem,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"🗑️ Personagem ID {id_personagem} removido.")
        else:
            print(f"🔍 Personagem não encontrado.")
    except psycopg2.errors.ForeignKeyViolation:
        print("⚠️ Erro: Não é possível deletar. Este personagem está vinculado a uma ideia.")
    except Error as e:
        print(f"❌ Erro ao deletar: {e}")
    finally:
        cursor.close()
        conexao.close()