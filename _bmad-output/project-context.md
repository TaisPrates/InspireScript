---
project_name: InspireScript
user_name: Autora
date: '2026-05-15'
sections_completed:
  - technology_stack
  - language_rules
  - framework_rules
  - testing_rules
  - quality_rules
  - workflow_rules
  - anti_patterns
status: complete
rule_count: 42
optimized_for_llm: true
---

# Project Context for AI Agents

_Regras críticas para implementação no InspireScript. Foco em detalhes não óbvios — leia antes de escrever código._

**Documentação de referência:** `docs/index.md`, `docs/architecture.md`, `docs/api-contracts.md`, `docs/data-models.md`

---

## Technology Stack & Versions

| Camada | Tecnologia | Versão (requirements.txt) |
|--------|------------|---------------------------|
| Linguagem | Python | 3.10+ |
| API | FastAPI | 0.135.1 |
| ASGI | uvicorn | 0.42.0 |
| Validação | Pydantic | 2.12.5 |
| Banco | **PostgreSQL** | 14+ (não MySQL) |
| Driver BD | psycopg2 | **adicionar `psycopg2-binary`** (ausente no requirements) |
| ORM | SQLAlchemy | 2.0.48 — **não usar**; código usa SQL cru |

**Não usar:** Flask, MySQL, ORM para novas features (a menos que haja decisão explícita de migração).

---

## Critical Implementation Rules

### Language-Specific Rules (Python)

- Repositórios em `back/core/repositories/` — **um arquivo por agregado** (`ideia.py`, `genero.py`, etc.).
- Cada função de repositório: `conectar()` → cursor → SQL parametrizado (`%s`) → `commit`/`rollback` → `close` em `finally`.
- **Nunca** interpolar valores em strings SQL; sempre tuplas no `execute`.
- Docstrings curtas em português nas funções públicas dos repositórios.
- Mensagens ao usuário via `print()` no CLI; **rotas FastAPI devem retornar `dict`/`list`**, não depender de `print`.
- Novos pacotes Python: usar `__init__.py` (não copiar o padrão incorreto `__init.py__` existente).
- Imports da API (rodando de `back/`): `from core.repositories import X`, `from core.config.config_banco import conectar`.
- Imports do CLI (rodando da raiz): `from back.core.repositories import X` — **não misturar** estilos no mesmo módulo sem refatorar ambos.

### Framework-Specific Rules (FastAPI)

- App único em `back/core/main.py`; instância `app = FastAPI()`.
- Novas rotas: preferir `APIRouter` com prefixo (`/ideias`, `/personagens`) quando houver mais de 2 endpoints por recurso.
- Usar modelos Pydantic (`BaseModel`) para request/response em endpoints novos — não query params soltos para POST bodies complexos.
- Documentação OpenAPI automática em `/docs` — manter nomes de parâmetros em português ou inglês consistente (hoje: misto aceitável, preferir português em `summary`/`description`).
- Configurar **CORS** antes de adicionar `front/`.
- Tratar erros de FK/constraint como `HTTPException(400/404)`, não apenas `print` no repositório.

### Testing Rules

- Ainda **sem suite** — ao introduzir testes: `tests/` na raiz ou `back/tests/`, arquivos `test_*.py`, pytest.
- Testes de repositório: BD de teste separado ou fixtures transacionais; nunca rodar contra produção.
- Mockar `conectar()` apenas em testes unitários de rotas; preferir testes de integração para SQL.

### Code Quality & Style Rules

- Alterações mínimas e focadas — sem refatoração ampla não solicitada.
- Schema SQL: apenas em `back/database/schema.sql/` com numeração sequencial; não editar tabelas só no Python.
- Seeds em `back/database/seed.sql/`; consultas de exemplo em `selects.sql/`.
- Credenciais: **nunca** commitar senhas; usar variáveis de ambiente em `config_banco.py` (`.env` no `.gitignore`).
- Comentários: só onde a regra de negócio não é óbvia (ex.: trigger de log, FK composta).
- Documentação de produto em português em `docs/`; artefatos BMAD em `_bmad-output/`.

### Development Workflow Rules

- API: `cd back && uvicorn core.main:app --reload`
- CLI: `python back/core/cli/menu.py` (raiz do repo)
- Ordem do schema: ver `docs/data-models.md` antes de criar migrations manuais.
- Commits: só quando o usuário pedir explicitamente.
- README desatualizado (Flask/MySQL/`database/` na raiz) — preferir `docs/` como fonte da verdade.

### Critical Don't-Miss Rules

| ❌ Não fazer | ✅ Fazer |
|-------------|----------|
| Assumir MySQL | PostgreSQL + sintaxe `IDENTITY`, `plpgsql` |
| Usar `subgenero.vincular_subgenero_ideia` | `ideia_subgenero.vincular_subgenero` |
| `GET /ideias` retornando `null` | Refatorar `listar_ideias()` para retornar lista de dicts |
| Criar `front/` com stack não definida | Alinhar com PRD/arquitetura antes |
| Adicionar SQLAlchemy em repositórios | Manter psycopg2 + SQL até decisão de migração |
| Expor credenciais em PR | `.env` + exemplo `.env.example` sem segredos |
| Duplicar lógica SQL na rota | Chamar repositório; lógica SQL só no repositório |
| Ignorar trigger `trg_log_ideia` | Updates em `ideia.descricao` geram histórico automaticamente |

**Cenários:** repositórios `cenario.py` e `ideia_cenario.py` existem mas **sem CLI/API** — ao implementar, espelhar padrão de `ideia_personagem.py`.

**Estrutura de pastas real:**

```
back/core/{main.py, cli/, config/, repositories/}
back/database/{schema.sql/, seed.sql/, selects.sql/}
docs/          ← project_knowledge BMAD
_bmad-output/  ← artefatos de planejamento (este arquivo)
```

---

## Usage Guidelines

**Para agentes de IA:**

1. Ler este arquivo + `docs/index.md` antes de implementar.
2. Em dúvida, preferir a opção mais restritiva e compatível com repositórios existentes.
3. Novos endpoints devem espelhar funções já existentes no CLI/repositório.
4. Atualizar `docs/api-contracts.md` ao alterar contratos HTTP.

**Para humanos:**

- Manter o arquivo enxuto (< ~200 linhas); remover regras que ficarem óbvias.
- Revisar quando mudar stack, ORM ou estrutura de imports.
- Regenerar após mudanças grandes: skill `bmad-generate-project-context`.

**Última atualização:** 2026-05-15
