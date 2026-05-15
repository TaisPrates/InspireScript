---
stepsCompleted:
  - step-01-validate-prerequisites
  - step-02-design-epics
  - step-03-create-stories
  - step-04-final-validation
inputDocuments:
  - _bmad-output/planning-artifacts/prd.md
  - _bmad-output/planning-artifacts/architecture.md
  - _bmad-output/planning-artifacts/decision-log.md
  - _bmad-output/project-context.md
  - docs/index.md
workflowType: epics-and-stories
project_name: InspireScript
status: complete
completedAt: '2026-05-15'
---

# InspireScript — Epic Breakdown

## Overview

Decomposição do PRD v1.0 e da arquitetura v1.0 em épicos e histórias implementáveis para o MVP. Projeto **brownfield**: schema PostgreSQL e repositórios existem; foco em serviços, API completa, front-end e correções técnicas.

**Referências:** [`prd.md`](./prd.md) · [`architecture.md`](./architecture.md)

---

## Requirements Inventory

### Functional Requirements

```
FR1: Autora pode criar uma ideia com título, gênero principal, subtítulo e descrição opcionais
FR2: Autora pode listar todas as suas ideias com gênero e data de criação
FR3: Autora pode visualizar detalhes completos de uma ideia
FR4: Autora pode atualizar título, gênero, subtítulo e descrição de uma ideia
FR5: Autora pode excluir uma ideia (com regras de integridade do banco)
FR6: Autora pode buscar ideias por título (correspondência parcial)
FR7: Sistema preserva histórico da descrição anterior ao atualizar uma ideia
FR8: Autora pode criar, listar, atualizar e excluir gêneros principais
FR9: Autora pode criar subgênero vinculado a um gênero pai
FR10: Autora pode listar subgêneros (com gênero pai)
FR11: Autora pode associar subgêneros a uma ideia
FR12: Autora pode remover associação ideia–subgênero
FR13: Sistema impede subgênero sem gênero pai válido
FR14: Autora pode criar, listar, atualizar e excluir personagens
FR15: Autora pode visualizar detalhes de um personagem
FR16: Autora pode criar e listar papéis narrativos
FR17: Autora pode associar personagem a uma ideia com um papel
FR18: Autora pode listar elenco (personagens e papéis) de uma ideia
FR19: Autora pode alterar o papel de um personagem em uma ideia
FR20: Autora pode remover personagem do elenco de uma ideia
FR21: Autora pode criar, listar, atualizar e excluir cenários
FR22: Autora pode visualizar detalhes de um cenário
FR23: Autora pode associar cenário a uma ideia
FR24: Autora pode listar cenários vinculados a uma ideia
FR25: Autora pode remover vínculo ideia–cenário
FR26: Autora pode listar histórico de alterações de descrição das ideias
FR27: Autora pode consultar um registro específico de log
FR28: Consumidor da API pode invocar FR1–FR27 via HTTP JSON
FR29: Consumidor da API pode descobrir contratos via OpenAPI
FR30: Sistema retorna erros estruturados (código + mensagem)
FR31: Autora pode usar interface web para FR1–FR6
FR32: Autora pode gerenciar gêneros/subgêneros pela interface web
FR33: Autora pode gerenciar personagens, papéis e elenco pela interface web
FR34: Autora pode gerenciar cenários e vínculos pela interface web
FR35: Autora pode consultar histórico pela interface web
FR36: Autora pode executar operações equivalentes via CLI
```

### NonFunctional Requirements

```
NFR1: Listagem de até 500 ideias < 2s (ambiente local)
NFR2: Escritas (create/update) < 1s (ambiente local)
NFR3: Credenciais de banco não versionadas
NFR4: SQL parametrizado (sem concatenação)
NFR5: (Growth) Sessões autenticadas
NFR6: Falha de conexão com mensagem clara, sem corrupção de dados
NFR7: Transações com commit/rollback explícito
NFR8: Novas entidades seguem padrão repositório
NFR9: Schema via scripts numerados em back/database/schema.sql/
NFR10: docs/ atualizado quando contratos HTTP mudam
NFR11: (Growth) WCAG 2.1 AA na UI
NFR12: PostgreSQL 14+
NFR13: API REST JSON UTF-8
```

### Additional Requirements (Architecture)

```
- Camada de serviços entre API/CLI e repositórios (ADR-004)
- API prefix /api/v1 com APIRouter por agregado (ADR-003)
- Repositórios retornam dict/list, sem print (refatoração)
- Imports unificados back.core.* (ADR-008)
- Config pydantic-settings + .env (ADR-006)
- Formato JSON { data, meta } e { error: { code, message } }
- Front-end Vite + JS vanilla em front/ (ADR-005)
- CORS localhost:5173
- Endpoint agregado GET /api/v1/ideias/{id}/completo
- Manter trigger trg_log_ideia (não duplicar em serviço)
- pytest + TestClient para API
- Corrigir menu CLI: ideia_subgenero.vincular_subgenero
- Remover ou marcar SQLAlchemy não usado no requirements
```

### UX Design Requirements

```
UX-DR1: Interface em português (pt-BR) — labels, botões, mensagens de erro
UX-DR2: Layout responsivo desktop e tablet (PRD Web App)
UX-DR3: Feedback visual de sucesso/erro após ações de formulário
UX-DR4: Listagens com estado vazio amigável (“Nenhuma ideia cadastrada”)
UX-DR5: Navegação simples entre áreas: Ideias, Gêneros, Personagens, Cenários, Histórico
UX-DR6: Formulários com validação client-side básica (campos obrigatórios)
```

### FR Coverage Map

| FR | Epic | Descrição |
|----|------|-----------|
| FR1–FR7 | Epic 2 | CRUD e busca de ideias + log |
| FR8–FR13 | Epic 3 | Gêneros e subgêneros |
| FR14–FR20 | Epic 4 | Personagens, papéis, elenco |
| FR21–FR25 | Epic 5 | Cenários e vínculos |
| FR26–FR27 | Epic 6 | Histórico de alterações |
| FR28–FR30 | Epics 2–6 | Endpoints API por domínio |
| FR29 | Epic 1 | OpenAPI montada |
| FR31 | Epic 2 | UI ideias |
| FR32 | Epic 3 | UI gêneros |
| FR33 | Epic 4 | UI personagens |
| FR34 | Epic 5 | UI cenários |
| FR35 | Epic 6 | UI histórico |
| FR36 | Epic 7 | CLI via serviços |
| NFR1–NFR13 | Epics 1, 8 | Fundação e qualidade |

---

## Epic List

### Epic 1: Fundação técnica do InspireScript

Estabelecer configuração segura, padrões de API e estrutura de pacotes para evolução brownfield sem retrabalho.

**FRs covered:** FR29 (parcial), FR30 (base)  
**NFRs covered:** NFR3, NFR4, NFR8, NFR13

### Epic 2: Registrar e desenvolver ideias de história

Autora captura, busca, edita e exclui ideias com gênero e histórico de descrição — via API e interface web.

**FRs covered:** FR1–FR7, FR28 (ideias), FR31

### Epic 3: Organizar gêneros e subgêneros

Autora mantém taxonomia narrativa e vincula subgêneros às ideias.

**FRs covered:** FR8–FR13, FR28 (gêneros), FR32

### Epic 4: Construir elenco de personagens

Autora cadastra personagens, papéis e monta elenco por ideia.

**FRs covered:** FR14–FR20, FR28 (personagens), FR33

### Epic 5: Mapear cenários das narrativas

Autora define ambientações e associa cenários às ideias (hoje só em repositório/BD).

**FRs covered:** FR21–FR25, FR28 (cenários), FR34

### Epic 6: Consultar histórico criativo

Autora revisa versões anteriores das descrições das ideias.

**FRs covered:** FR26–FR27, FR28 (logs), FR35

### Epic 7: Operar pelo terminal (CLI)

CLI usa mesma lógica de negócio que a API; paridade e correções.

**FRs covered:** FR36

### Epic 8: Garantir qualidade e documentação

Testes, performance local e docs alinhados ao produto implementado.

**FRs covered:** —  
**NFRs covered:** NFR1, NFR2, NFR6, NFR7, NFR10

---

## Epic 1: Fundação técnica do InspireScript

Estabelecer base segura e padrões para todas as features seguintes.

### Story 1.1: Configuração por variáveis de ambiente

As a **desenvolvedora**,
I want **credenciais e parâmetros de BD em `.env`**,
So that **segredos não sejam commitados**.

**Acceptance Criteria:**

**Given** o projeto clonado  
**When** copio `.env.example` para `.env` e preencho `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_PORT`  
**Then** `back/core/config/settings.py` (pydantic-settings) carrega os valores  
**And** `config_banco.conectar()` usa settings, sem senha hardcoded no código  
**And** `.env` está no `.gitignore`

**Refs:** NFR3, ADR-006

---

### Story 1.2: Unificar pacote Python `back.core`

As a **desenvolvedora**,
I want **imports consistentes `from back.core...`**,
So that **API e CLI rodem do mesmo jeito**.

**Acceptance Criteria:**

**Given** estrutura atual com imports mistos  
**When** configuro `pyproject.toml` ou `PYTHONPATH` na raiz  
**Then** `uvicorn back.core.main:app` funciona da raiz do repositório  
**And** CLI importa `back.core.services` e `back.core.repositories`  
**And** documentação em `development-guide.md` atualizada

**Refs:** ADR-008

---

### Story 1.3: Padrão global de erros e CORS na API

As a **desenvolvedora**,
I want **respostas de erro JSON padronizadas e CORS para o front**,
So that **a UI Vite consome a API sem surpresas**.

**Acceptance Criteria:**

**Given** app FastAPI em `back/core/main.py`  
**When** ocorre `HTTPException` ou erro de validação  
**Then** corpo segue `{ "error": { "code", "message", "field?" } }`  
**And** `CORSMiddleware` permite `http://localhost:5173`  
**And** FR30 atendido para erros de validação

**Refs:** FR30, ADR-003

---

### Story 1.4: Dependências e requirements alinhados

As a **desenvolvedora**,
I want **`requirements.txt` completo e preciso**,
So that **`pip install` basta para rodar o projeto**.

**Acceptance Criteria:**

**Given** `requirements.txt` atual  
**When** adiciono `psycopg2-binary` e `pydantic-settings`  
**Then** API e repositórios conectam ao PostgreSQL  
**And** SQLAlchemy removido ou comentado como não usado no MVP  
**And** README lista dependências corretas

**Refs:** NFR12, project-context

---

### Story 1.5: Scaffold da API v1 com routers montados

As a **desenvolvedora**,
I want **estrutura `back/core/api/routers/` criada**,
So that **features adicionem endpoints sem inflar `main.py`**.

**Acceptance Criteria:**

**Given** Epic 1 concluído até 1.4  
**When** crio routers vazios: `ideias`, `generos`, `personagens`, `cenarios`, `logs` com prefix `/api/v1`  
**Then** `GET /docs` lista todos os tags/grupos  
**And** `GET /` mantém mensagem de boas-vindas  
**And** FR29 satisfeito (OpenAPI descoberta)

**Refs:** FR29, ADR-003

---

## Epic 2: Registrar e desenvolver ideias de história

### Story 2.1: Repositório de ideias retorna dados estruturados

As a **desenvolvedora**,
I want **`ideia.py` retornando dict/list sem print**,
So that **API e serviços consumam dados**.

**Acceptance Criteria:**

**Given** PostgreSQL com tabela `ideia` populada  
**When** chamo `listar_ideias()`, `inserir_ideia(...)`, `buscar_ideia_detalhada(id)`, `atualizar_ideia(...)`, `deletar_ideia(id)`  
**Then** cada função retorna estrutura Python (dict ou list[dict]) ou levanta exceção clara  
**And** nenhum `print` permanece nessas funções  
**And** SQL permanece parametrizado (NFR4)

**Refs:** FR1–FR5 (persistência), NFR4, NFR7

---

### Story 2.2: Serviço de ideias com regras de negócio

As a **desenvolvedora**,
I want **`IdeiaService` orquestrando o repositório**,
So that **validações fiquem fora da rota HTTP**.

**Acceptance Criteria:**

**Given** repositório refatorado (Story 2.1)  
**When** título vazio ou `id_genero_principal` inválido  
**Then** serviço retorna erro de domínio tratável  
**When** crio ideia válida  
**Then** retorno inclui `id_ideia` gerado  
**And** busca por título parcial funciona (FR6)

**Refs:** FR1, FR6

---

### Story 2.3: API REST CRUD de ideias

As a **autora**,
I want **endpoints REST para ideias**,
So that **qualquer cliente HTTP gerencie minhas histórias**.

**Acceptance Criteria:**

**Given** API v1 scaffold  
**When** uso `POST/GET/PUT/DELETE /api/v1/ideias` e `GET /api/v1/ideias?titulo=`  
**Then** respostas usam `{ "data": ... }`  
**And** códigos HTTP corretos (201, 200, 204, 404, 400)  
**And** schemas Pydantic documentados no OpenAPI  
**And** FR28 satisfeito para ideias

**Refs:** FR1–FR6, FR28, FR30

---

### Story 2.4: Detalhe agregado da ideia (completo)

As a **autora**,
I want **ver ideia com gênero, subgêneros, elenco e cenários em uma chamada**,
So that **retome o projeto com contexto total**.

**Acceptance Criteria:**

**Given** ideia com vínculos opcionais  
**When** `GET /api/v1/ideias/{id}/completo`  
**Then** JSON inclui ideia, genero, subgeneros[], elenco[], cenarios[]  
**And** FR3 satisfeito de forma agregada

**Refs:** FR3, architecture §7

---

### Story 2.5: Histórico automático ao editar descrição

As a **autora**,
I want **versões anteriores da descrição preservadas**,
So that **eu confie em editar a sinopse**.

**Acceptance Criteria:**

**Given** trigger `trg_log_ideia` aplicado no BD  
**When** atualizo apenas `descricao` via API ou serviço  
**Then** nova linha em `log_alteracao_ideia` com texto anterior  
**And** FR7 satisfeito sem lógica duplicada no Python

**Refs:** FR7, ADR-009

---

### Story 2.6: Interface web — ideias (listar, criar, editar, buscar)

As a **autora**,
I want **páginas web para minhas ideias**,
So that **não dependa do terminal no dia a dia**.

**Acceptance Criteria:**

**Given** `front/` com Vite configurado e `client.js` apontando para API  
**When** acesso listagem de ideias  
**Then** vejo título, gênero, data (FR2)  
**When** crio/edito/busco ideia  
**Then** formulários funcionam (FR1, FR4, FR6)  
**And** mensagens de erro da API exibidas em pt-BR (UX-DR1, UX-DR3)  
**And** estado vazio amigável (UX-DR4)  
**And** FR31 satisfeito

**Refs:** FR1–FR6, FR31, UX-DR1–DR4

---

## Epic 3: Organizar gêneros e subgêneros

### Story 3.1: Repositórios de gênero e subgênero retornam dados

As a **desenvolvedora**,
I want **genero.py e subgenero.py sem print**,
So that **serviços possam compor respostas**.

**Acceptance Criteria:**

**Given** tabelas `genero` e `subgenero`  
**When** executo CRUD em ambos repositórios  
**Then** retornos são dict/list  
**And** FK inválida em subgênero falha de forma tratável (FR13)

**Refs:** FR8–FR10, FR13, NFR4

---

### Story 3.2: Serviço e API de gêneros e subgêneros

As a **autora**,
I want **API para gêneros e subgêneros**,
So that **eu organize a taxonomia das histórias**.

**Acceptance Criteria:**

**Given** Story 3.1  
**When** uso endpoints `/api/v1/generos` e `/api/v1/subgeneros`  
**Then** CRUD completo funciona  
**And** FR8–FR10 cobertos

**Refs:** FR8–FR10, FR28

---

### Story 3.3: Vínculo ideia–subgênero na API

As a **autora**,
I want **associar e remover subgêneros de uma ideia**,
So that **classifique cada história com nuance**.

**Acceptance Criteria:**

**Given** ideia e subgênero existentes  
**When** `POST/DELETE /api/v1/ideias/{id}/subgeneros`  
**Then** vínculos refletem em `ideia_subgenero`  
**And** FR11 e FR12 satisfeitos

**Refs:** FR11, FR12, FR28

---

### Story 3.4: Interface web — gêneros e subgêneros

As a **autora**,
I want **telas para gêneros e vínculos**,
So that **eu gerencie taxonomia visualmente**.

**Acceptance Criteria:**

**Given** API Stories 3.2–3.3  
**When** navego à área Gêneros  
**Then** CRUD de gêneros e subgêneros funciona  
**When** na tela da ideia, adiciono subgênero  
**Then** vínculo aparece na listagem  
**And** FR32 e UX-DR5 satisfeitos

**Refs:** FR32, UX-DR5

---

## Epic 4: Construir elenco de personagens

### Story 4.1: Repositórios personagem, papel e elenco

As a **desenvolvedora**,
I want **personagem, papel_personagem, ideia_personagem retornando dados**,
So that **elenco seja composável na API**.

**Acceptance Criteria:**

**Given** tabelas existentes  
**When** CRUD e vínculos são chamados  
**Then** sem print; retornos estruturados  
**And** `mudar_papel_personagem` funciona (FR19)

**Refs:** FR14–FR20 (persistência)

---

### Story 4.2: Serviço e API de personagens e papéis

As a **autora**,
I want **cadastrar personagens e papéis via API**,
So that **eu reutilize personagens entre ideias**.

**Acceptance Criteria:**

**Given** Story 4.1  
**When** uso `/api/v1/personagens` e `/api/v1/papeis`  
**Then** FR14–FR16 cobertos com JSON padronizado

**Refs:** FR14–FR16, FR28

---

### Story 4.3: API de elenco por ideia

As a **autora**,
I want **gerenciar elenco de cada ideia**,
So that **eu veja quem é protagonista de qual história**.

**Acceptance Criteria:**

**Given** personagem, papel e ideia existentes  
**When** `POST/GET/PATCH/DELETE /api/v1/ideias/{id}/elenco`  
**Then** FR17–FR20 satisfeitos  
**And** listagem mostra nome do personagem e nome do papel

**Refs:** FR17–FR20, FR28

---

### Story 4.4: Interface web — personagens e elenco

As a **autora**,
I want **UI para personagens e elenco**,
So that **monte o elenco sem CLI**.

**Acceptance Criteria:**

**Given** APIs 4.2–4.3  
**When** cadastro personagem e associo à ideia com papel  
**Then** elenco visível na página da ideia  
**And** FR33 e UX-DR5 satisfeitos

**Refs:** FR33, UX-DR5, UX-DR6

---

## Epic 5: Mapear cenários das narrativas

### Story 5.1: Repositórios de cenário e vínculo

As a **desenvolvedora**,
I want **cenario.py e ideia_cenario.py retornando dados**,
So that **cenários entrem no produto**.

**Acceptance Criteria:**

**Given** repositórios existentes hoje sem UI  
**When** refatoro para dict/list sem print  
**Then** CRUD cenário e vínculo ideia–cenário funcionam

**Refs:** FR21–FR25 (persistência)

---

### Story 5.2: Serviço e API de cenários

As a **autora**,
I want **API de cenários e vínculos**,
So that **eu defina ambientação por história**.

**Acceptance Criteria:**

**Given** Story 5.1  
**When** uso `/api/v1/cenarios` e `/api/v1/ideias/{id}/cenarios`  
**Then** FR21–FR25 cobertos

**Refs:** FR21–FR25, FR28

---

### Story 5.3: Interface web — cenários

As a **autora**,
I want **UI para cenários**,
So that **complete a visão da ideia na web**.

**Acceptance Criteria:**

**Given** API Story 5.2  
**When** gerencio cenários e vínculos na página da ideia  
**Then** FR34 satisfeito  
**And** detalhe `/completo` mostra cenários (integração com Story 2.4)

**Refs:** FR34, UX-DR5

---

## Epic 6: Consultar histórico criativo

### Story 6.1: Repositório e serviço de logs

As a **desenvolvedora**,
I want **log_ideia.py integrado à camada de serviço**,
So that **histórico seja consultável**.

**Acceptance Criteria:**

**Given** logs gerados por trigger  
**When** `listar_historico_alteracoes` e `buscar_log_especifico`  
**Then** retornam dict/list sem print

**Refs:** FR26, FR27

---

### Story 6.2: API e UI de histórico

As a **autora**,
I want **ver histórico de edições da descrição**,
So that **eu recupere trechos antigos da sinopse**.

**Acceptance Criteria:**

**Given** ideia com edições de descrição  
**When** `GET /api/v1/logs/ideias` e `GET /api/v1/logs/ideias/{id}`  
**Then** FR26–FR27 satisfeitos  
**When** abro área Histórico na UI  
**Then** FR35 satisfeito com UX-DR1

**Refs:** FR26, FR27, FR28, FR35

---

## Epic 7: Operar pelo terminal (CLI)

### Story 7.1: CLI usa camada de serviços

As a **autora**,
I want **menu CLI chamando serviços**,
So that **terminal e web compartilhem regras**.

**Acceptance Criteria:**

**Given** serviços dos Epics 2–6  
**When** executo `python -m back.core.cli.menu` da raiz  
**Then** fluxos de ideias, gêneros, personagens funcionam  
**And** FR36 parcialmente satisfeito

**Refs:** FR36

---

### Story 7.2: Corrigir vínculo de subgênero no menu

As a **autora**,
I want **opção 5 do menu de ideias funcionando**,
So that **eu vincule subgêneros pelo terminal**.

**Acceptance Criteria:**

**Given** menu_ideias opção 5  
**When** informo id ideia e id subgênero  
**Then** chama `ideia_subgenero.vincular_subgenero` (não função inexistente)  
**And** vínculo persiste no BD

**Refs:** project-context anti-pattern fix

---

### Story 7.3: CLI para cenários e logs

As a **autora**,
I want **menus de cenários e histórico no CLI**,
So that **tenha paridade com a API**.

**Acceptance Criteria:**

**Given** serviços de cenário e log  
**When** adiciono entradas no menu principal  
**Then** CRUD cenário e consulta log funcionam  
**And** FR36 totalmente satisfeito

**Refs:** FR36, FR21–FR27

---

## Epic 8: Garantir qualidade e documentação

### Story 8.1: Testes de integração da API (smoke)

As a **desenvolvedora**,
I want **pytest com TestClient**,
So that **regressões sejam detectadas cedo**.

**Acceptance Criteria:**

**Given** BD de teste ou fixtures transacionais  
**When** `pytest tests/integration/api/`  
**Then** smoke tests passam para ideias, generos, personagens (mínimo happy path)  
**And** NFR7 validado em teste de falha simulada

**Refs:** NFR7, architecture §5.7

---

### Story 8.2: Atualizar documentação técnica

As a **desenvolvedora**,
I want **docs alinhados ao implementado**,
So that **agentes e humanos não se percam**.

**Acceptance Criteria:**

**Given** API v1 implementada  
**When** reviso `docs/api-contracts.md`, `README.md`, `docs/roadmap.md`  
**Then** rotas, PostgreSQL e estrutura `back/` corretos  
**And** NFR10 satisfeito

**Refs:** NFR10

---

### Story 8.3: Verificação de performance local

As a **desenvolvedora**,
I want **validar NFR1 e NFR2**,
So that **a UX local permaneça fluida**.

**Acceptance Criteria:**

**Given** seed com volume moderado (ex.: 100 ideias)  
**When** medio listagem e create via API  
**Then** listagem < 2s e escrita < 1s em máquina dev de referência  
**Or** documento desvio com justificativa

**Refs:** NFR1, NFR2

---

## Validação final (Step 4)

| Verificação | Status |
|-------------|--------|
| Todos FR1–FR36 em ≥1 história | ✅ |
| NFRs endereçados (Epics 1, 8; Growth NFR5/11 notados) | ✅ |
| UX-DR1–DR6 em histórias de UI | ✅ |
| Sem “criar todas tabelas” upfront | ✅ (schema brownfield) |
| Dependências entre histórias sequenciais | ✅ |
| Starter greenfield | N/A — brownfield |
| Histórias tamanho dev agent | ✅ |

**Total:** 8 épicos · 28 histórias

---

_Próximo passo BMAD: `bmad-check-implementation-readiness` ou `bmad-sprint-planning`._
