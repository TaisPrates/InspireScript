# InspireScript — Índice de Documentação

**Tipo:** Monólito backend  
**Linguagem principal:** Python  
**Arquitetura:** API REST + CLI + camada de repositórios  
**Última atualização:** 2026-05-15

## Visão geral

Plataforma para organização de ideias literárias (ideias, personagens, gêneros, cenários). O código atual é backend-only; front-end planejado mas não presente no repositório.

## Referência rápida

| Item | Valor |
|------|--------|
| **Stack** | FastAPI, uvicorn, psycopg2, PostgreSQL |
| **API** | `back/core/main.py` |
| **CLI** | `back/core/cli/menu.py` |
| **Banco** | `inspire_script` (PostgreSQL) |
| **Scripts SQL** | `back/database/schema.sql/`, `seed.sql/`, `selects.sql/` |

## Documentação gerada (BMAD)

### Núcleo

- [Visão do projeto](./project-overview.md) — Resumo executivo e classificação
- [Análise da árvore de fontes](./source-tree-analysis.md) — Estrutura de pastas anotada
- [Arquitetura](./architecture.md) — Decisões técnicas e fluxos
- [Inventário de componentes](./component-inventory.md) — Repositórios e módulos Python

### API e dados

- [Contratos de API](./api-contracts.md) — Endpoints FastAPI atuais
- [Modelos de dados](./data-models.md) — Schema PostgreSQL e relacionamentos

### Desenvolvimento

- [Guia de desenvolvimento](./development-guide.md) — Pré-requisitos, setup, execução

### Metadados

- [Partes do projeto (JSON)](./project-parts.json) — Estrutura machine-readable
- [Relatório de varredura](./project-scan-report.json) — Estado do workflow BMAD

## Documentação existente (pré-BMAD)

- [Visão geral do produto](./visao-geral.md) — Problema, solução, escopo
- [Arquitetura (legado)](./arquitetura.md) — Camadas de alto nível *(parcialmente desatualizado: cita MySQL)*
- [Roadmap](./roadmap.md) — *(vazio — preencher)*
- [Setup (legado)](./setup.md) — *(vazio — ver [development-guide.md](./development-guide.md))*

## Como começar

### Pré-requisitos

- Python 3.10+
- PostgreSQL 14+ (recomendado; trigger usa sintaxe moderna)
- Node.js *(apenas para ferramentas BMAD via `npx`, não para o app)*

### Setup rápido

```powershell
cd c:\Inspire_Script
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install psycopg2-binary
```

Aplicar schema e seeds — ver [development-guide.md](./development-guide.md).

### Executar API

```powershell
cd c:\Inspire_Script\back
uvicorn core.main:app --reload
```

- API: http://127.0.0.1:8000  
- Swagger: http://127.0.0.1:8000/docs  

### Executar CLI

```powershell
cd c:\Inspire_Script
python back\core\cli\menu.py
```

## Para desenvolvimento assistido por IA

Este índice é o **ponto de entrada** para agentes e workflows BMAD.

| Tarefa | Documentos de referência |
|--------|-------------------------|
| Nova feature de API | `architecture.md`, `api-contracts.md`, `data-models.md` |
| Alteração de schema | `data-models.md`, scripts em `back/database/schema.sql/` |
| Feature full-stack (futuro) | Todos acima + recriar `front/` |
| PRD brownfield | Fornecer este `index.md` ao workflow `bmad-create-prd` |
| Contexto enxuto para agentes | [_bmad-output/project-context.md](../_bmad-output/project-context.md) |
| PRD (requisitos do produto) | [_bmad-output/planning-artifacts/prd.md](../_bmad-output/planning-artifacts/prd.md) |
| Arquitetura (decisões BMAD) | [_bmad-output/planning-artifacts/architecture.md](../_bmad-output/planning-artifacts/architecture.md) |
| Épicos e histórias | [_bmad-output/planning-artifacts/epics.md](../_bmad-output/planning-artifacts/epics.md) |
| Status do sprint | [_bmad-output/implementation-artifacts/sprint-status.yaml](../_bmad-output/implementation-artifacts/sprint-status.yaml) |

---

_Documentação gerada pelo BMAD Method — workflow `bmad-document-project`._
