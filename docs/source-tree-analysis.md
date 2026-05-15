# InspireScript — Análise da árvore de fontes

**Data:** 2026-05-15

## Estrutura anotada

```
Inspire_Script/
├── README.md                 # Visão do produto (parcialmente desatualizado)
├── requirements.txt          # Dependências Python (falta psycopg2)
├── LICENSE
│
├── back/                     # ★ Backend principal
│   ├── __init__.py
│   ├── core/
│   │   ├── main.py           # ★ Entrada FastAPI (app)
│   │   ├── cli/
│   │   │   └── menu.py       # ★ Entrada CLI interativo
│   │   ├── config/
│   │   │   └── config_banco.py   # Conexão PostgreSQL
│   │   └── repositories/     # ★ Camada de acesso a dados (SQL cru)
│   │       ├── ideia.py
│   │       ├── genero.py
│   │       ├── subgenero.py
│   │       ├── ideia_subgenero.py
│   │       ├── personagem.py
│   │       ├── papel_personagem.py
│   │       ├── ideia_personagem.py
│   │       ├── cenario.py
│   │       ├── ideia_cenario.py
│   │       └── log_ideia.py
│   └── database/
│       ├── schema.sql/       # DDL ordenado (01–14)
│       ├── seed.sql/         # Dados iniciais
│       └── selects.sql/      # Consultas de exemplo
│
├── docs/                     # ★ Conhecimento do projeto (project_knowledge BMAD)
│   ├── index.md              # Índice mestre (este workflow)
│   ├── project-overview.md
│   ├── architecture.md
│   ├── api-contracts.md
│   ├── data-models.md
│   ├── development-guide.md
│   ├── visao-geral.md        # Produto (legado)
│   ├── arquitetura.md        # Camadas (legado)
│   ├── roadmap.md            # Vazio
│   └── setup.md              # Vazio
│
├── _bmad/                    # Configuração BMAD Method (não alterar manualmente)
│   ├── config.toml
│   ├── bmm/
│   └── scripts/
│
└── .agents/skills/           # Skills Cursor geradas pelo instalador BMAD
    └── bmad-*/               # Workflows e agentes (42 skills)
```

## Pastas críticas

| Pasta | Propósito |
|-------|-----------|
| `back/core/repositories/` | Toda lógica de persistência; funções chamadas por CLI e (parcialmente) API |
| `back/core/cli/` | Interface de terminal para operação completa do sistema |
| `back/core/main.py` | Superfície HTTP para integração futura com front-end |
| `back/database/schema.sql/` | Fonte da verdade do modelo relacional |
| `docs/` | Documentação humana e contexto para IAs (BMAD `project_knowledge`) |

## Pontos de entrada

| Entrada | Arquivo | Comando típico |
|---------|---------|----------------|
| API | `back/core/main.py` | `uvicorn core.main:app --reload` (cwd: `back/`) |
| CLI | `back/core/cli/menu.py` | `python back/core/cli/menu.py` (cwd: raiz) |

## Integrações futuras

```
[ front/ ]  ──HTTP──►  [ back/core/main.py ]  ──psycopg2──►  [ PostgreSQL ]
     ▲                         │
     │                         └── hoje: CLI em menu.py usa mesmos repositórios
     └── pasta ausente no repo
```

## Exclusões da varredura

- `.git/`, `__pycache__/`, `.idea/`, `venv/`, `node_modules/`
- Conteúdo gerado em `_bmad-output/` (ainda vazio)

---

_Gerado pelo workflow `bmad-document-project`._
