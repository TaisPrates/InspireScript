from fastapi import FastAPI
from core.repositories import ideia

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Bem-vinda, Autora! O sistema Inspire Script está online."}

@app.get("/ideias")
def listar_ideias():
    return ideia.listar_ideias()


@app.post("/ideias")
def criar_ideia(titulo: str, genero_id: int, sub: str = "", desc: str = ""):
    ideia.inserir_ideia(titulo, genero_id, sub, desc)
    return {"mensagem": "Ideia criada com sucesso"}