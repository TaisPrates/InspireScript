# InspireScript — Contratos de API

**Base URL (dev):** `http://127.0.0.1:8000`  
**Framework:** FastAPI 0.135  
**Arquivo:** `back/core/main.py`  
**OpenAPI:** `/docs` (Swagger UI), `/openapi.json`

## Estado atual

A API está em estágio **inicial**. Apenas operações de **ideias** estão expostas. Demais entidades existem nos repositórios e no CLI, mas **não têm rotas HTTP**.

## Autenticação

Nenhuma. Todas as rotas são públicas (adequado apenas para desenvolvimento local).

## Endpoints

### `GET /`

**Handler:** `home()`

**Resposta 200:**

```json
{
  "mensagem": "Bem-vinda, Autora! O sistema Inspire Script está online."
}
```

---

### `GET /ideias`

**Handler:** `listar_ideias()`

**Comportamento atual:** delega a `ideia.listar_ideias()`, que **imprime** a lista no console do servidor e **não retorna dados estruturados**.

**Resposta HTTP típica:** `null` (corpo vazio)

**Comportamento esperado (recomendado):**

```json
[
  {
    "id_ideia": 1,
    "titulo": "Exemplo",
    "subtitulo": null,
    "genero": "Fantasia",
    "data_criacao": "2026-01-01T12:00:00"
  }
]
```

---

### `POST /ideias`

**Handler:** `criar_ideia(titulo, genero_id, sub="", desc="")`

**Parâmetros (query string):**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `titulo` | string | sim | Título da ideia |
| `genero_id` | int | sim | FK `genero.id_genero` |
| `sub` | string | não | Subtítulo |
| `desc` | string | não | Descrição |

**Exemplo:**

```http
POST /ideias?titulo=Minha%20História&genero_id=1&sub=Um%20começo&desc=Sinopse%20inicial
```

**Resposta 200:**

```json
{
  "mensagem": "Ideia criada com sucesso"
}
```

**Observações:**

- Não retorna `id_ideia` da linha inserida
- Erros de FK (gênero inexistente) são tratados no repositório via `print`, não como HTTP 4xx

## Endpoints planejados (não implementados)

Com base nos repositórios existentes, a API futura poderia incluir:

| Recurso | Operações sugeridas |
|---------|---------------------|
| `/generos` | GET, POST, PUT, DELETE |
| `/subgeneros` | GET, POST, PUT, DELETE |
| `/ideias/{id}/subgeneros` | GET, POST, DELETE |
| `/personagens` | GET, POST, PUT, DELETE |
| `/papeis` | GET, POST |
| `/ideias/{id}/elenco` | GET, POST, PATCH, DELETE |
| `/cenarios` | GET, POST, PUT, DELETE |
| `/ideias/{id}/cenarios` | GET, POST, DELETE |
| `/logs/ideias` | GET |

## Modelos Pydantic

Não definidos. Parâmetros são tipos primitivos na assinatura da rota.

## CORS

Não configurado. Necessário quando o front-end for adicionado.

---

_Gerado pelo workflow `bmad-document-project`._
