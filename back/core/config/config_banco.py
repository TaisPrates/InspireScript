import psycopg2
from psycopg2 import Error

def conectar():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="inspire_script",
            user="postgres",
            password="T@is2404",
            port="5432"
        )
        return conexao
    except Error as e:
        print(f"❌ Erro ao conectar ao PostgreSQL: {e}")
        return None