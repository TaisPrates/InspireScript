# Story 1.1: Configuração por variáveis de ambiente

Status: ready-for-dev

<!-- Validation: opcional — validate-create-story antes de dev-story -->

## Story

As a **desenvolvedora**,
I want **credenciais e parâmetros de BD em `.env`**,
so that **segredos não sejam commitados**.

## Acceptance Criteria

1. **Given** o projeto clonado  
   **When** copio `.env.example` para `.env` e preencho `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_PORT`  
   **Then** `back/core/config/settings.py` (pydantic-settings) carrega os valores  

2. **And** `config_banco.conectar()` usa settings, **sem senha hardcoded** no código-fonte  

3. **And** `.env` permanece no `.gitignore` (já listado — validar, não remover)  

4. **And** conexão PostgreSQL continua funcionando para repositórios existentes após a mudança  

**Refs:** NFR3, ADR-006, Epic 1 Story 1.1

## Tasks / Subtasks

- [ ] **Task 1: Dependência pydantic-settings** (AC: 1)
  - [ ] Adicionar `pydantic-settings` em `requirements.txt` (versão compatível com Pydantic 2.12.x)
  - [ ] Documentar no comentário da story/dev notes — Story 1.4 revisará lista completa

- [ ] **Task 2: Criar `settings.py`** (AC: 1)
  - [ ] Criar `back/core/config/settings.py` com classe `Settings(BaseSettings)`
  - [ ] Campos: `db_host`, `db_name`, `db_user`, `db_password`, `db_port` (mapear de env `DB_HOST`, etc.)
  - [ ] `model_config`: `env_file=".env"`, `env_file_encoding="utf-8"`, `extra="ignore"`
  - [ ] Singleton ou `get_settings()` com `@lru_cache` para uma instância por processo
  - [ ] Defaults seguros para dev local (host localhost, port 5432, database inspire_script) **sem** senha default no código

- [ ] **Task 3: `.env.example` na raiz do repositório** (AC: 1)
  - [ ] Criar `.env.example` com placeholders (sem valores reais):
    ```
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=inspire_script
    DB_USER=postgres
    DB_PASSWORD=altere_aqui
    ```
  - [ ] Commitar `.env.example`; nunca commitar `.env`

- [ ] **Task 4: Refatorar `config_banco.py`** (AC: 2, 4)
  - [ ] Remover literais `host`, `database`, `user`, `password`, `port` hardcoded
  - [ ] Importar settings e passar para `psycopg2.connect(...)`
  - [ ] Manter assinatura `conectar() -> connection | None` e tratamento `Error` com `print` (refatoração de retorno fica para Epic 2)
  - [ ] Garantir que `.env` é encontrado ao rodar de `back/` (uvicorn) **e** da raiz (CLI futuro) — ver nota de path abaixo

- [ ] **Task 5: Verificação manual** (AC: 4)
  - [ ] Com PostgreSQL rodando e `.env` preenchido: `python -c` ou script mínimo que chama `conectar()` e executa `SELECT 1`
  - [ ] Confirmar que repositório existente (ex. `ideia.listar_ideias()`) ainda conecta quando cwd = `back/`

## Dev Notes

### Estado atual (ler antes de editar)

**Arquivo:** `back/core/config/config_banco.py`

- Credenciais **hardcoded** em `psycopg2.connect(...)` — **remover completamente** no PR
- Função `conectar()` retorna conexão ou `None`; usada por **todos** os repositórios em `back/core/repositories/*.py` via `from core.config.config_banco import conectar`
- **Não alterar** assinatura de `conectar()` nesta story — evita diff em 10 repositórios

**`.gitignore`:** já contém `.env` — apenas confirmar.

**`requirements.txt`:** tem Pydantic 2.12.5; **falta** `pydantic-settings` e `psycopg2-binary` (psycopg2 pode já estar instalado localmente — Story 1.4 cobre requirements completo).

### Padrão obrigatório (architecture + project-context)

| Regra | Ação |
|-------|------|
| ADR-006 | Config via pydantic-settings + `.env` |
| NFR3 | Zero segredos no git |
| NFR4 | SQL continua parametrizado (sem mudança nesta story) |
| Não usar SQLAlchemy | Não adicionar ORM |
| Imports atuais | Manter `from core.config...` até Story 1.2 |

### Resolução do caminho do `.env`

Problema brownfield: `uvicorn` roda com `cwd=back/`, CLI pode rodar da raiz.

**Abordagem recomendada** em `settings.py`:

1. Procurar `.env` subindo diretórios a partir de `Path(__file__).resolve()` até achar `Inspire_Script/.env`, **ou**
2. Usar `env_file` com caminho absoluto para `{repo_root}/.env`

Documentar no README ou `docs/development-guide.md` (opcional nesta story; Story 8.2 cobre docs formalmente): copiar `.env.example` → `.env` na **raiz** do repo.

### O que NÃO fazer nesta story

- Não criar routers API (Story 1.5)
- Não unificar imports `back.core` (Story 1.2)
- Não refatorar repositórios para retornar dict (Story 2.1)
- Não commitar `.env` ou qualquer senha real
- Não remover `print` de erro de conexão ainda

### Project Structure Notes

```
Inspire_Script/
├── .env                 # gitignored — criado localmente pela autora
├── .env.example         # NEW — commitar
├── requirements.txt     # UPDATE — pydantic-settings
└── back/core/config/
    ├── config_banco.py  # UPDATE — usar settings
    └── settings.py      # NEW
```

### Testing Requirements

- Teste manual mínimo obrigatório (sem pytest nesta story)
- Opcional: teste unitário de `Settings` com `monkeypatch` env vars — não bloqueante para MVP

### References

- [Source: _bmad-output/planning-artifacts/epics.md — Story 1.1]
- [Source: _bmad-output/planning-artifacts/architecture.md — ADR-006]
- [Source: _bmad-output/project-context.md — Security / config]
- [Source: back/core/config/config_banco.py — estado atual]
- [Source: docs/development-guide.md — setup BD]

## Dev Agent Record

### Agent Model Used

_(preencher no dev-story)_

### Debug Log References

### Completion Notes List

### File List
