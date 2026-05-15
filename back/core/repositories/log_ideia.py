from psycopg2 import Error
from core.config.config_banco import conectar


def listar_historico_alteracoes():
    """Exibe todos os logs de alteração das ideias registrados no sistema."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        # Fazemos um JOIN com a tabela ideia para saber o título da história alterada
        sql = """
            SELECT l.id_log, i.titulo, l.descricao_antiga, l.data_alteracao
            FROM log_alteracao_ideia l
            LEFT JOIN ideia i ON l.id_ideia = i.id_ideia
            ORDER BY l.data_alteracao DESC
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        if resultados:
            print("\n" + "=" * 70)
            print(f"{'ID LOG':<7} | {'IDEIA':<20} | {'DATA':<18} | {'DESCRIÇÃO ANTIGA'}")
            print("=" * 70)
            for r in resultados:
                data_formatada = r[3].strftime('%d/%m/%Y %H:%M')
                titulo = r[1] if r[1] else "Ideia Deletada"
                # Trunca a descrição antiga para não quebrar a tabela do terminal
                desc_curta = (r[2][:30] + '...') if r[2] and len(r[2]) > 30 else (r[2] or "---")

                print(f"{r[0]:<7} | {titulo:<20} | {data_formatada:<18} | {desc_curta}")
            print("=" * 70)
        else:
            print("\n📜 O histórico de alterações está limpo.")
    except Error as e:
        print(f"❌ Erro ao consultar logs: {e}")
    finally:
        cursor.close()
        conexao.close()


def buscar_log_especifico(id_log):
    """Mostra o conteúdo completo de uma alteração específica."""
    conexao = conectar()
    if not conexao: return

    cursor = conexao.cursor()
    try:
        sql = "SELECT descricao_antiga, data_alteracao FROM log_alteracao_ideia WHERE id_log = %s"
        cursor.execute(sql, (id_log,))
        r = cursor.fetchone()

        if r:
            print(f"\n--- DETALHE DO LOG #{id_log} ---")
            print(f"Data do registro: {r[1].strftime('%d/%m/%Y %H:%M:%S')}")
            print("-" * 40)
            print(f"Conteúdo anterior:\n{r[0]}")
            print("-" * 40)
        else:
            print(f"🔍 Log ID {id_log} não encontrado.")
    except Error as e:
        print(f"❌ Erro ao buscar log: {e}")
    finally:
        cursor.close()
        conexao.close()