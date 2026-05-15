---
stepsCompleted:
  - step-01-init
  - step-02-discovery
  - step-02b-vision
  - step-02c-executive-summary
  - step-03-success
  - step-04-journeys
  - step-05-domain
  - step-06-innovation
  - step-07-project-type
  - step-08-scoping
  - step-09-functional
  - step-10-nonfunctional
  - step-11-polish
  - step-12-complete
inputDocuments:
  - docs/index.md
  - docs/project-overview.md
  - docs/architecture.md
  - docs/api-contracts.md
  - docs/data-models.md
  - docs/development-guide.md
  - docs/visao-geral.md
  - docs/arquitetura.md
  - _bmad-output/project-context.md
  - README.md
documentCounts:
  briefCount: 0
  researchCount: 0
  brainstormingCount: 0
  projectDocsCount: 9
workflowType: prd
classification:
  projectType: web_app
  secondaryType: api_backend
  domain: escrita_criativa
  complexity: low
  projectContext: brownfield
---

# Product Requirements Document — InspireScript

**Autora:** Autora  
**Data:** 2026-05-15  
**Versão:** 1.0  
**Status:** Rascunho completo (brownfield)

---

## Executive Summary

O **InspireScript** é uma plataforma para escritores organizarem ideias literárias — histórias, personagens, gêneros, subgêneros e cenários — em um único lugar estruturado. O produto reduz o atrito entre **ter uma ideia** e **desenvolvê-la**, evitando perda de contexto em cadernos ou ferramentas genéricas não orientadas a narrativa.

**Estado atual (brownfield):** backend Python com PostgreSQL, CLI funcional para a maior parte do domínio, API REST mínima (3 rotas de ideias), schema relacional maduro, **sem interface web** no repositório.

**Objetivo deste PRD:** definir o produto completo (MVP → crescimento → visão), alinhando o que já existe com o que falta implementar — especialmente API completa, front-end e integração entre camadas.

### What Makes This Special

- **Estrutura narrativa nativa:** gênero principal, subgêneros, elenco com papéis, cenários — não pastas genéricas.
- **Evolução incremental:** começar pela organização; expandir para escrita e assistência inteligente sem quebrar a base.
- **Histórico de ideias:** trigger de log preserva versões anteriores da descrição ao editar.
- **Arquitetura em camadas:** preparada para API + UI + extensões futuras (agentes de escrita).

## Project Classification

| Atributo | Valor |
|----------|--------|
| **Tipo principal** | Aplicação web (SPA ou MPA + API) |
| **Tipo secundário** | API backend (estado atual) |
| **Domínio** | Escrita criativa / produtividade para autores |
| **Complexidade de domínio** | Baixa (sem regulamentação pesada) |
| **Contexto** | Brownfield — código e banco parcialmente implementados |

---

## Success Criteria

### User Success

| Critério | Métrica |
|----------|---------|
| Registrar ideia completa | Autora cadastra título, gênero, subtítulo e descrição em menos de 2 minutos |
| Retomar projeto antigo | Autora localiza ideia por listagem/busca e vê personagens e cenários vinculados |
| Organizar elenco | Autora associa personagens com papéis a uma ideia sem perder vínculos |
| Confiança no histórico | Autora consulta log de alterações da descrição após edições |

### Business Success

| Horizonte | Indicador |
|-----------|-----------|
| MVP (3 meses) | Uso pessoal diário pela autora; 100% das operações do CLI disponíveis na API + UI |
| Crescimento (6–12 meses) | Base estável para convidar beta de escritores; feedback qualitativo positivo em organização |
| Visão (12+ meses) | Extensões de IA opcionais sem comprometer fluxo manual |

### Technical Success

| Critério | Meta |
|----------|------|
| API REST | CRUD completo para todas as entidades do schema |
| Respostas HTTP | Endpoints retornam JSON estruturado (não `print` no servidor) |
| Persistência | PostgreSQL como única fonte de verdade; migrations versionadas |
| Segurança local | Credenciais fora do código (variáveis de ambiente) |
| Documentação | `docs/` e OpenAPI (`/docs`) alinhados ao comportamento real |

---

## Product Scope

### MVP (Fase 1 — alinhar ao roadmap atual)

**Já existe (manter e corrigir):**

- Schema PostgreSQL (gêneros, ideias, personagens, papéis, cenários, vínculos, logs)
- Repositórios Python e CLI para ideias, personagens, gêneros, papéis, logs
- API básica FastAPI (`/`, `GET/POST /ideias`)

**Entregar no MVP:**

1. API REST completa espelhando repositórios (incluindo cenários e vínculos)
2. Repositórios retornam dados estruturados (refatoração para API)
3. Front-end web mínimo: listar/criar/editar ideias, personagens, gêneros
4. Configuração via `.env`; `psycopg2-binary` no `requirements.txt`
5. Correções: bug menu subgênero; alinhamento README/docs (PostgreSQL, paths)
6. Busca simples de ideias por título

### Growth (Fase 2)

- Dashboard da ideia (visão unificada: elenco, subgêneros, cenários)
- UX polida (design system, responsivo, acessibilidade WCAG 2.1 AA básico)
- Autenticação de usuária (conta única ou multi-usuário)
- Exportação (Markdown/JSON da ideia completa)
- Testes automatizados (pytest + API)

### Vision (Fase 3)

- Escrita estruturada de capítulos e arcos narrativos
- Sugestões assistidas por IA (personagens, plot, cenários) — opt-in
- Colaboração (compartilhar ideia com leitor beta)
- Sincronização/backup na nuvem

---

## User Journeys

### Jornada 1 — Autora: capturar faísca de ideia (happy path)

**Cena inicial:** Surgiu uma ideia de fantasia urbana no meio do dia; risco de esquecer se não registrar agora.

1. Abre InspireScript (web ou CLI)
2. Cria ideia com título, gênero principal, subtítulo opcional
3. Adiciona descrição (sinopse em 2–3 parágrafos)
4. Vincula 1–2 subgêneros
5. Sistema confirma salvamento e exibe ideia na listagem

**Clímax:** Ideia aparece na lista com gênero e data — sensação de “não vou perder isso”.

**Resolução:** Pode fechar o app; ao voltar dias depois, retoma pelo mesmo registro.

**Requisitos revelados:** CRUD ideia, vínculo subgênero, listagem ordenada, persistência.

---

### Jornada 2 — Autora: montar elenco (happy path)

**Cena inicial:** A ideia já existe; personagens começam a surgir sem ordem.

1. Abre detalhe da ideia
2. Cadastra personagem (nome, descrição) ou escolhe existente
3. Associa personagem à ideia com papel (protagonista, antagonista, etc.)
4. Visualiza elenco da ideia

**Clímax:** Vê tabela/lista personagem ↔ papel — clareza narrativa.

**Resolução:** Elenco coerente para desenvolver cenas futuras.

**Requisitos revelados:** CRUD personagem, CRUD papel, vínculo ideia–personagem, listagem de elenco.

---

### Jornada 3 — Autora: ambientar a história

**Cena inicial:** Precisa fixar onde/quando a cena principal ocorre.

1. Na ideia, acessa cenários
2. Cadastra cenário (nome, descrição, tipo: tempo/espaço)
3. Vincula cenário à ideia
4. Lista cenários da ideia

**Requisitos revelados:** CRUD cenário, vínculo ideia–cenário (hoje só em repositório/BD).

---

### Jornada 4 — Autora: retomar e evoluir (edge case)

**Cena inicial:** Voltou a um projeto de 3 meses atrás; mudou a sinopse.

1. Busca ideia pelo título
2. Abre detalhe completo (gênero, subgêneros, elenco, cenários)
3. Edita descrição
4. Sistema grava log da descrição anterior (trigger)
5. Consulta histórico de alterações

**Requisitos revelados:** Busca, detalhe agregado, update ideia, visualização de log.

---

### Jornada 5 — Autora via API/ferramenta externa (futuro)

Consumidor HTTP autenticado lista ideias e exporta JSON para backup local.

**Requisitos revelados:** API documentada (OpenAPI), autenticação (Growth), formatos estáveis.

---

## Domain-Specific Requirements

Domínio de **baixa complexidade regulatória**. Requisitos específicos:

| Área | Requisito |
|------|-----------|
| Privacidade | Dados criativos são pessoais; sem compartilhamento público no MVP |
| Propriedade | Conteúdo pertence à autora; sem treinamento de modelo com dados sem consentimento (Vision) |
| Integridade narrativa | FKs impedem gênero/personagem órfão em vínculos |
| Idioma | UI e mensagens em português (pt-BR) |

*Nenhuma conformidade HIPAA/PCI aplicável no escopo atual.*

---

## Innovation & Future Capabilities

| Inovação | Fase | Notas |
|----------|------|-------|
| Assistente de brainstorming | Vision | Sugestões de plot/personagem baseadas na ideia |
| Detecção de lacunas narrativas | Vision | “Ideia sem antagonista”, “sem cenário” |
| PRFAQ / validação de conceito | Planejamento BMAD | Opcional antes de escalar |

*MVP não depende de IA.*

---

## Web Application Specific Requirements

| Tópico | Decisão MVP |
|--------|-------------|
| Formato | MPA ou SPA leve consumindo API REST |
| Browsers | Últimas 2 versões Chrome, Firefox, Edge |
| Responsivo | Sim — uso em desktop e tablet |
| SEO | Baixa prioridade (app autenticada / uso pessoal) |
| Tempo real | Não no MVP |
| Offline | Não no MVP |

---

## Functional Requirements

### Gestão de Ideias

- **FR1:** Autora pode criar uma ideia com título, gênero principal, subtítulo e descrição opcionais
- **FR2:** Autora pode listar todas as suas ideias com gênero e data de criação
- **FR3:** Autora pode visualizar detalhes completos de uma ideia
- **FR4:** Autora pode atualizar título, gênero, subtítulo e descrição de uma ideia
- **FR5:** Autora pode excluir uma ideia (com regras de integridade do banco)
- **FR6:** Autora pode buscar ideias por título (correspondência parcial)
- **FR7:** Sistema preserva histórico da descrição anterior ao atualizar uma ideia

### Gêneros e Subgêneros

- **FR8:** Autora pode criar, listar, atualizar e excluir gêneros principais
- **FR9:** Autora pode criar subgênero vinculado a um gênero pai
- **FR10:** Autora pode listar subgêneros (com gênero pai)
- **FR11:** Autora pode associar subgêneros a uma ideia
- **FR12:** Autora pode remover associação ideia–subgênero
- **FR13:** Sistema impede subgênero sem gênero pai válido

### Personagens e Elenco

- **FR14:** Autora pode criar, listar, atualizar e excluir personagens
- **FR15:** Autora pode visualizar detalhes de um personagem
- **FR16:** Autora pode criar e listar papéis narrativos (protagonista, etc.)
- **FR17:** Autora pode associar personagem a uma ideia com um papel
- **FR18:** Autora pode listar elenco (personagens e papéis) de uma ideia
- **FR19:** Autora pode alterar o papel de um personagem em uma ideia
- **FR20:** Autora pode remover personagem do elenco de uma ideia

### Cenários

- **FR21:** Autora pode criar, listar, atualizar e excluir cenários
- **FR22:** Autora pode visualizar detalhes de um cenário
- **FR23:** Autora pode associar cenário a uma ideia
- **FR24:** Autora pode listar cenários vinculados a uma ideia
- **FR25:** Autora pode remover vínculo ideia–cenário

### Histórico e Auditoria

- **FR26:** Autora pode listar histórico de alterações de descrição das ideias
- **FR27:** Autora pode consultar um registro específico de log

### API e Integração

- **FR28:** Consumidor da API pode invocar todas as capacidades FR1–FR27 via HTTP JSON
- **FR29:** Consumidor da API pode descobrir contratos via documentação OpenAPI
- **FR30:** Sistema retorna erros de validação e integridade em formato estruturado (código + mensagem)

### Interface Web (MVP)

- **FR31:** Autora pode acessar interface web para executar FR1–FR6 sem CLI
- **FR32:** Autora pode gerenciar gêneros e subgêneros pela interface web
- **FR33:** Autora pode gerenciar personagens, papéis e elenco pela interface web
- **FR34:** Autora pode gerenciar cenários e vínculos pela interface web
- **FR35:** Autora pode consultar histórico de alterações pela interface web

### Operação (CLI — manutenção)

- **FR36:** Autora pode executar operações equivalentes via CLI enquanto a interface web não cobrir 100%

---

## Non-Functional Requirements

### Performance

- **NFR1:** Listagem de até 500 ideias retorna em menos de 2 segundos em ambiente local
- **NFR2:** Operações de escrita (create/update) completam em menos de 1 segundo em ambiente local

### Security

- **NFR3:** Credenciais de banco não residem em arquivos versionados
- **NFR4:** Entradas de texto são parametrizadas no SQL (sem concatenação)
- **NFR5:** (Growth) Sessões autenticadas para acesso à API e UI

### Reliability

- **NFR6:** Falha de conexão com banco exibe mensagem clara sem corromper dados
- **NFR7:** Transações de escrita fazem commit ou rollback explícito

### Maintainability

- **NFR8:** Novas entidades seguem padrão repositório em `back/core/repositories/`
- **NFR9:** Alterações de schema via scripts numerados em `back/database/schema.sql/`
- **NFR10:** Documentação em `docs/` atualizada quando contratos HTTP mudam

### Accessibility (Growth)

- **NFR11:** Interface web atende contraste e navegação por teclado (WCAG 2.1 AA alvo)

### Compatibility

- **NFR12:** Backend compatível com PostgreSQL 14+
- **NFR13:** API segue convenções REST com corpos JSON UTF-8

---

## Traceability Matrix (resumo)

| Jornada | FRs principais |
|---------|----------------|
| Capturar ideia | FR1–FR7, FR28, FR31 |
| Montar elenco | FR14–FR20, FR33 |
| Ambientar | FR21–FR25, FR34 |
| Retomar/evoluir | FR3–FR7, FR6, FR26–FR27, FR35 |
| API externa | FR28–FR30 |

---

## Out of Scope (este PRD v1)

- Multi-tenant / equipes
- Pagamentos ou assinatura
- App mobile nativo
- IA generativa em produção (apenas Vision)
- Migração para ORM/SQLAlchemy (sem decisão explícita)

---

## Appendix: Brownfield Inventory

| Componente | Status |
|------------|--------|
| PostgreSQL schema | ✅ Completo |
| Repositórios | ✅ 10 módulos |
| CLI | ✅ Parcial (sem cenários; bug subgênero) |
| API FastAPI | ⚠️ 3 rotas |
| Front-end | ❌ Ausente |
| Testes | ❌ Ausente |
| `.env` / secrets | ❌ Hardcoded |

**Referências:** `docs/index.md`, `_bmad-output/project-context.md`

---

_PRD gerado pelo workflow BMAD `bmad-create-prd` — modo brownfield, documentação de entrada carregada._
