# InspireScript — Guia de Desenvolvimento

**Data:** 2026-05-15

## Pré-requisitos

| Ferramenta | Versão sugerida |
|------------|-----------------|
| Python | 3.10+ |
| PostgreSQL | 14+ |
| Git | qualquer recente |
| Node.js | opcional (apenas para `npx bmad-method`) |

## Configuração do banco

### 1. Criar o database

```sql
CREATE DATABASE inspire_script
  WITH ENCODING 'UTF8'
  LC_COLLATE = 'Portuguese_Brazil.1252'
  LC_CTYPE = 'Portuguese_Brazil.1252'
  TEMPLATE template0;
```

(Ajuste locale conforme seu sistema.)

### 2. Aplicar schema

No **psql** ou cliente SQL, executar os arquivos em `back/database/schema.sql/` na ordem listada em [data-models.md](./data-models.md).

Exemplo (PowerShell, com `psql` no PATH):

```powershell
cd c:\Inspire_Script\back\database\schema.sql
Get-ChildItem *.sql | Sort-Object Name | ForEach-Object {
  psql -U postgres -d inspire_script -f $_.FullName
}
```

### 3. Seeds (opcional)

```powershell
cd c:\Inspire_Script\back\database\seed.sql
Get-ChildItem *.sql | Sort-Object Name | ForEach-Object {
  psql -U postgres -d inspire_script -f $_.FullName
}
```

### 4. Credenciais

Editar `back/core/config/config_banco.py` ou migrar para `.env`:

| Variável sugerida | Exemplo |
|-------------------|---------|
| `DB_HOST` | `localhost` |
| `DB_NAME` | `inspire_script` |
| `DB_USER` | `postgres` |
| `DB_PASSWORD` | *(seu valor)* |
| `DB_PORT` | `5432` |

**Não commitar senhas.** O arquivo atual contém credenciais em texto claro — tratar como débito técnico.

## Ambiente Python

```powershell
cd c:\Inspire_Script
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install psycopg2-binary
```

> `psycopg2-binary` é obrigatório mas **não está** em `requirements.txt` — adicionar em commit futuro.

## Executar a API

```powershell
cd c:\Inspire_Script\back
uvicorn core.main:app --reload --host 127.0.0.1 --port 8000
```

| URL | Descrição |
|-----|-----------|
| http://127.0.0.1:8000 | Raiz |
| http://127.0.0.1:8000/docs | Swagger UI |
| http://127.0.0.1:8000/ideias | Listar ideias *(ver limitação em api-contracts.md)* |

## Executar o CLI

```powershell
cd c:\Inspire_Script
python back\core\cli\menu.py
```

Menus: ideias, personagens, gêneros/subgêneros, papéis, logs.

**Bug conhecido:** opção 5 em “Gerenciar ideias” chama `subgenero.vincular_subgenero_ideia` — função inexistente. Corrigir para `ideia_subgenero.vincular_subgenero`.

## Testes

Não há suite de testes configurada. Recomendação futura:

```powershell
pip install pytest
# pytest tests/ -v
```

## Estrutura de imports

| Contexto | Import esperado |
|----------|-----------------|
| API (`main.py`, repositórios) | `from core.repositories import ...` (cwd: `back/`) |
| CLI (`menu.py`) | `from back.core.repositories import ...` (cwd: raiz) |

Unificar em refatoração futura (pacote instalável ou `PYTHONPATH` documentado).

## BMAD Method

Workflows e skills em `_bmad/` e `.agents/skills/`.

```powershell
# Reinstalar/atualizar BMAD
npx bmad-method install
```

Próximo passo sugerido após documentação: `bmad-generate-project-context`.

## Checklist antes de PR

- [ ] Schema aplicado e seeds testados
- [ ] API sobe sem erro (`uvicorn`)
- [ ] CLI executa menus principais
- [ ] Sem credenciais novas commitadas
- [ ] `requirements.txt` inclui `psycopg2-binary`

---

_Gerado pelo workflow `bmad-document-project`._
