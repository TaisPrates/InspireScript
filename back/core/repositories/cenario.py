import psycopg2
from psycopg2 import Error
from datetime import datetime
from core.config.config_banco import conectar

def inserir_cenario(nome, descricao=None, tipo=None):
    """Cadastra um novo cenário (Ex: Neo-Tóquio, Laboratório 42)."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = """
            INSERT INTO cenario (nome, descricao, tipo)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (nome.strip(), descricao, tipo))
        conexao.commit()
        print(f"🌍 Cenário '{nome}' criado com sucesso!")
    except psycopg2.errors.CheckViolation:
        print("⚠️ Erro: O nome do cenário não pode estar vazio.")
    except Error as e:
        print(f"❌ Erro ao inserir cenário: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_cenarios():
    """Lista todos os cenários cadastrados com seu tipo."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "SELECT id_cenario, nome, tipo FROM cenario ORDER BY nome"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        if resultados:
            print("\n" + "="*50)
            print(f"{'ID':<4} | {'CENÁRIO':<20} | {'TIPO':<15}")
            print("="*50)
            for c in resultados:
                tipo_display = c[2] if c[2] else "---"
                print(f"{c[0]:<4} | {c[1]:<20} | {tipo_display:<15}")
            print("="*50)
        else:
            print("\n📭 Nenhum cenário cadastrado ainda.")
    except Error as e:
        print(f"❌ Erro ao listar cenários: {e}")
    finally:
        cursor.close()
        conexao.close()

def buscar_cenario_detalhado(id_cenario):
    """Mostra a descrição completa e as datas de um cenário."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "SELECT nome, descricao, tipo, data_criacao FROM cenario WHERE id_cenario = %s"
        cursor.execute(sql, (id_cenario,))
        c = cursor.fetchone()

        if c:
            print(f"\n--- EXPLORANDO: {c[0]} ---")
            print(f"Tipo: {c[2] if c[2] else 'Não definido'}")
            print(f"Criado em: {c[3].strftime('%d/%m/%Y %H:%M')}")
            print("-" * 30)
            print(f"Descrição:\n{c[1] if c[1] else 'Sem descrição disponível.'}")
            print("-" * 30)
        else:
            print(f"🔍 Cenário ID {id_cenario} não encontrado.")
    except Error as e:
        print(f"❌ Erro ao buscar cenário: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_cenario(id_cenario, nome, descricao, tipo):
    """Atualiza os dados do cenário e registra a data de atualização."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        # Note que aqui atualizamos também o campo data_atualizacao manualmente via Python
        # (ou poderíamos deixar para uma Trigger no banco, mas aqui garantimos pelo código)
        sql = """
            UPDATE cenario 
            SET nome = %s, descricao = %s, tipo = %s, data_atualizacao = %s
            WHERE id_cenario = %s
        """
        cursor.execute(sql, (nome.strip(), descricao, tipo, datetime.now(), id_cenario))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"✅ Cenário ID {id_cenario} atualizado com sucesso!")
        else:
            print("🔍 Cenário não encontrado.")
    except Error as e:
        print(f"❌ Erro ao atualizar: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_cenario(id_cenario):
    """Deleta um cenário (se não estiver vinculado a nenhuma ideia)."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM cenario WHERE id_cenario = %s"
        cursor.execute(sql, (id_cenario,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"🗑️ Cenário ID {id_cenario} removido.")
        else:
            print("🔍 Cenário não encontrado.")
    except psycopg2.errors.ForeignKeyViolation:
        print("⚠️ Erro: Este cenário está sendo usado em uma ideia e não pode ser removido.")
    except Error as e:
        print(f"❌ Erro ao deletar: {e}")
    finally:
        cursor.close()
        conexao.close()