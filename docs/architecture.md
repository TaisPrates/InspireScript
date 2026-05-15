# InspireScript — Arquitetura Técnica

**Data:** 2026-05-15  
**Versão do código analisado:** 0.1.0 (em desenvolvimento)

## Resumo executivo

Arquitetura em **camadas** com separação entre interfaces (API/CLI), repositórios e PostgreSQL. Não há camada de serviço explícita — os repositórios concentram SQL e efeitos colaterais (`print`). O projeto está preparado para evoluir para API completa e front-end, mas hoje o **CLI é a interface mais completa**.

## Diagrama de contexto

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Usuária    │────►│  CLI (menu.py)   │────►│  Repositories   │
│  (terminal) │     └──────────────────┘     │  (*.py)         │
└─────────────┘              │               └────────┬────────┘
       │                     │                        │
       │              ┌──────▼──────┐                 │
       └─────────────►│ FastAPI     │─────────────────┘
                      │ (main.py)   │
                      └──────┬──────┘
                             │
                      ┌──────▼──────┐
                      │ PostgreSQL  │
                      │ inspire_    │
                      │ script      │
                      └─────────────┘
```

## Camadas

### 1. Interfaces

| Interface | Local | Responsabilidade |
|-----------|-------|------------------|
| HTTP/REST | `back/core/main.py` | 3 rotas; integração futura com web |
| CLI | `back/core/cli/menu.py` | Menus aninhados; fluxo principal de uso |

**Problema atual:** imports inconsistentes — API usa `from core.repositories`; CLI usa `from back.core.repositories`. Exige `PYTHONPATH` ou cwd específico.

### 2. Repositórios

Padrão **Repository** simplificado: uma função por operação, SQL parametrizado, conexão aberta/fechada por chamada.

| Módulo | Entidade(ies) |
|--------|----------------|
| `ideia.py` | `ideia` |
| `genero.py` | `genero` |
| `subgenero.py` | `subgenero` |
| `ideia_subgenero.py` | vínculo ideia ↔ subgênero |
| `personagem.py` | `personagem` |
| `papel_personagem.py` | `papel_personagem` |
| `ideia_personagem.py` | elenco (ideia + personagem + papel) |
| `cenario.py` | `cenario` |
| `ideia_cenario.py` | vínculo ideia ↔ cenário |
| `log_ideia.py` | `log_alteracao_ideia` |

**Comportamento comum:** em falha de conexão, retorna cedo; sucesso/erro comunicados via `print()` — inadequado para API JSON sem refatoração.

### 3. Configuração

`back/core/config/config_banco.py` — função `conectar()` retorna conexão `psycopg2` ou `None`.

**Risco:** credenciais fixas no código. Recomendação: migrar para variáveis de ambiente (`.env` + `python-dotenv`).

### 4. Persistência

- Scripts DDL em `back/database/schema.sql/` (ordem numérica)
- Seeds em `back/database/seed.sql/`
- Trigger `trg_log_ideia` grava histórico ao alterar `ideia.descricao`

## Padrões e decisões

| Decisão | Escolha | Implicação |
|---------|---------|------------|
| ORM | Não usado (SQLAlchemy no requirements mas idle) | Controle total do SQL; mais verboso |
| API framework | FastAPI | OpenAPI automático em `/docs` |
| Autenticação | Ausente | OK para dev local; obrigatório antes de produção |
| Front-end | Planejado, ausente | README desatualizado na estrutura de pastas |
| Testes | Ausentes | Nenhum `test_*.py` encontrado |

## Fluxo de dados — criar ideia (CLI)

1. `menu_ideias()` → opção 1  
2. `ideia.inserir_ideia(titulo, id_genero, subtitulo, descricao)`  
3. `conectar()` → `INSERT INTO ideia ...`  
4. `commit` / mensagem no terminal  

## Fluxo de dados — criar ideia (API)

1. `POST /ideias?titulo=...&genero_id=...`  
2. `criar_ideia()` → `ideia.inserir_ideia(...)`  
3. Retorna `{"mensagem": "Ideia criada com sucesso"}` (sem ID da ideia criada)

## Evolução recomendada

1. **Unificar imports** (`back.core` ou pacote instalável)  
2. **Camada de serviço** — repositórios retornam dict/list; interfaces só formatam  
3. **Completar API** — espelhar operações do CLI  
4. **Variáveis de ambiente** — remover segredos do código  
5. **Front-end** — consumir API REST  
6. **Testes** — pytest sobre repositórios com BD de teste  

## Relação com documentação legada

`docs/arquitetura.md` descreve três camadas (front, back, BD) corretamente no conceito, mas cita **MySQL** — o código e DDL usam **PostgreSQL**. Este documento prevalece para decisões técnicas atuais.

---

_Gerado pelo workflow `bmad-document-project`._
