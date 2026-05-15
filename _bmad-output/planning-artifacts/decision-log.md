# Decision Log — InspireScript PRD

Registro de decisões tomadas durante a criação do PRD (2026-05-15).

| ID | Decisão | Rationale | Alternativas consideradas |
|----|---------|-----------|-------------------------|
| D1 | PostgreSQL como SGBD único | DDL e código já usam PostgreSQL | MySQL (citado em docs legados) |
| D2 | MVP inclui front-end web | README e visão definem app web; API sozinha insuficiente | CLI-only como produto final |
| D3 | Manter padrão repositório + SQL cru no MVP | Código existente; menor risco | Adotar SQLAlchemy já no MVP |
| D4 | IA apenas na fase Vision | Reduz escopo; base estável primeiro | Agente criativo no MVP |
| D5 | Domínio baixa complexidade — sem seção compliance pesada | Produto pessoal/creativo | N/A |
| D6 | API deve espelhar CLI antes de features novas | Paridade brownfield | Novas features só na UI |
| D7 | Autenticação adiada para Growth | Uso pessoal inicial | Auth no MVP |
| D8 | Busca simples por título no MVP | Baixo custo; alto valor para retomar ideias | Busca full-text complexa |
| D9 | Camada de serviços entre API e repositórios | Separa JSON/HTTP de SQL e print | Lógica só em routers |
| D10 | Front-end Vite + JS vanilla | Alinha README; menor curva no MVP | React/Vue |
| D11 | API prefix `/api/v1` + routers por agregado | Versionamento e modularidade | Rotas monolíticas em main.py |
| D12 | Imports unificados `back.core.*` | Elimina split de PYTHONPATH | Manter dual import |
| D13 | Formato JSON `{ data, meta }` / `{ error }` | Consistência para UI e agentes | Respostas ad hoc |

---

_Vinculado a: `planning-artifacts/prd.md`, `planning-artifacts/architecture.md`_
