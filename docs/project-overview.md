# InspireScript — Visão do Projeto

**Data:** 2026-05-15  
**Tipo:** Backend (API + CLI)  
**Arquitetura:** Camadas (repositórios + acesso a dados)

## Resumo executivo

O **InspireScript** é uma plataforma para organização e desenvolvimento de ideias literárias. O estado atual do repositório é um **backend Python** com:

- **API REST** mínima (FastAPI) — 3 rotas para ideias
- **CLI interativo** — CRUD amplo para ideias, personagens, gêneros e papéis
- **Banco PostgreSQL** — schema relacional com gêneros, subgêneros, personagens, cenários e log de alterações

O front-end descrito no README **ainda não existe** no repositório. A documentação de produto (`visao-geral.md`) está alinhada à proposta; a documentação técnica operacional estava incompleta até esta varredura BMAD.

## Classificação do projeto

| Atributo | Valor |
|----------|--------|
| Tipo de repositório | Monólito |
| Tipo detectado (BMAD) | `backend` |
| Linguagem principal | Python |
| Framework web | FastAPI |
| Banco de dados | PostgreSQL |
| Padrão arquitetural | Repository pattern + SQL direto |

## Stack tecnológica

| Categoria | Tecnologia | Versão (requirements.txt) | Uso |
|-----------|------------|----------------------------|-----|
| Linguagem | Python | 3.x | Todo o backend |
| API | FastAPI | 0.135.1 | `back/core/main.py` |
| Servidor | uvicorn | 0.42.0 | Execução da API |
| Validação | Pydantic | 2.12.5 | Dependência FastAPI |
| Banco | PostgreSQL | — | DDL em `back/database/schema.sql/` |
| Driver BD | psycopg2 | *(ausente no requirements)* | `config_banco.py` e repositórios |
| ORM | SQLAlchemy | 2.0.48 | **Não utilizado** no código atual |

## Funcionalidades principais

- Cadastro e gestão de **ideias** (histórias) com gênero principal
- Hierarquia **gênero → subgênero** e vínculo N:N com ideias
- **Personagens** com papéis narrativos (protagonista, etc.) por ideia
- **Cenários** modelados no banco (repositórios prontos; sem CLI/API ainda)
- **Log automático** de alterações na descrição da ideia (trigger PostgreSQL)

## Destaques de arquitetura

- Separação em `repositories/` (acesso a dados) e `cli/` / `main.py` (interfaces)
- Scripts SQL versionados por número em `back/database/`
- Configuração BMAD em `_bmad/` e skills em `.agents/skills/` para fluxos de planejamento

## Lacunas conhecidas (brownfield)

1. Pasta `front/` ausente  
2. README menciona MySQL; implementação usa PostgreSQL  
3. API expõe só ideias; repositórios cobrem muito mais  
4. `GET /ideias` chama função que só imprime no console (não retorna JSON)  
5. `requirements.txt` sem `psycopg2-binary`  
6. Credenciais do banco em texto claro em `config_banco.py`  
7. Bug no menu CLI: opção 5 chama função inexistente `vincular_subgenero_ideia`  
8. `docs/setup.md` e `docs/roadmap.md` estavam vazios  

## Mapa de documentação

| Documento | Conteúdo |
|-----------|----------|
| [index.md](./index.md) | Índice mestre (entrada para IAs) |
| [architecture.md](./architecture.md) | Arquitetura técnica detalhada |
| [api-contracts.md](./api-contracts.md) | Contratos HTTP atuais |
| [data-models.md](./data-models.md) | Modelo de dados PostgreSQL |
| [development-guide.md](./development-guide.md) | Setup e execução local |
| [source-tree-analysis.md](./source-tree-analysis.md) | Árvore de diretórios anotada |
| [component-inventory.md](./component-inventory.md) | Inventário de módulos/repositórios |

## Documentação legada (pré-BMAD)

- [visao-geral.md](./visao-geral.md) — visão de produto  
- [arquitetura.md](./arquitetura.md) — visão de camadas (parcialmente desatualizada)  

---

_Gerado pelo workflow BMAD `bmad-document-project` (varredura profunda)._
