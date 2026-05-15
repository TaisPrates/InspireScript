# InspireScript — Modelos de Dados

**SGBD:** PostgreSQL  
**Database:** `inspire_script`  
**Scripts:** `back/database/schema.sql/` (executar em ordem numérica)

## Diagrama ER (simplificado)

```
genero ─────┬────< subgenero
            │
            └────< ideia ─────┬────< ideia_subgenero >──── subgenero
                              │
                              ├────< ideia_personagem >──── personagem
                              │              │
                              │              └── papel_personagem
                              │
                              ├────< ideia_cenario >──── cenario
                              │
                              └────< log_alteracao_ideia
```

## Tabelas

### `genero`

| Coluna | Tipo | Notas |
|--------|------|-------|
| `id_genero` | INTEGER IDENTITY PK | |
| `nome` | VARCHAR UNIQUE NOT NULL | |

### `subgenero`

| Coluna | Tipo | Notas |
|--------|------|-------|
| `id_subgenero` | INTEGER IDENTITY PK | |
| `nome` | VARCHAR NOT NULL | |
| `id_genero_pai` | INTEGER FK → `genero` | |

### `ideia`

| Coluna | Tipo | Notas |
|--------|------|-------|
| `id_ideia` | INTEGER IDENTITY PK | |
| `titulo` | VARCHAR(200) NOT NULL | CHECK não vazio |
| `subtitulo` | VARCHAR(200) | |
| `descricao` | TEXT | Histórico via trigger |
| `id_genero_principal` | INTEGER FK → `genero` | |
| `data_criacao` | TIMESTAMP DEFAULT now | |

### `ideia_subgenero`

PK composta: (`id_ideia`, `id_subgenero`)

### `personagem`

| Coluna | Tipo | Notas |
|--------|------|-------|
| `id_personagem` | INTEGER IDENTITY PK | |
| `nome` | VARCHAR NOT NULL | |
| `descricao` | TEXT | |

### `papel_personagem`

Papéis narrativos (ex.: Protagonista, Antagonista). Seed em `seed.sql/01_insert_papel_personagem.sql`.

### `ideia_personagem`

| Coluna | Tipo | Notas |
|--------|------|-------|
| `id_ideia` | FK | |
| `id_personagem` | FK | |
| `id_papel` | FK → `papel_personagem` | |

### `cenario`

Cadastro de ambientações (nome, descrição, tipo).

### `ideia_cenario`

Vínculo N:N ideia ↔ cenário. Migration `11_table_ideia_personagem_alteration.sql` adiciona `papel_cenario`.

### `log_alteracao_ideia`

Armazena versões anteriores da `descricao` quando a ideia é atualizada.

**Trigger:** `14_Função _Trigger_log.sql` — função `salvar_historico_ideia()`, trigger `trg_log_ideia` BEFORE UPDATE em `ideia`.

## Índices

`10_indices.sql` — índices em chaves estrangeiras e colunas de busca frequente.

## Ordem de execução do schema

1. `01_create_tbl_genero_principal.sql`
2. `02_create_tbl_subgenero.sql`
3. `03_create_tbl_ideia.sql`
4. `04_create_tbl_ideia_subgenero.sql`
5. `05_create_tbl_personagem.sql`
6. `06_create_tbl_papel_personagem.sql`
7. `07_crete_tbl_ideia_personagem.sql`
8. `08_create_tbl_cenario.sql`
9. `09_crete_tbl_ideia_cenario.sql`
10. `11_table_ideia_personagem_alteration.sql`
11. `10_indices.sql`
12. `13_create_tabela_log.sql`
13. `14_Função _Trigger_log.sql`

Depois: scripts em `back/database/seed.sql/` (opcional, dados de exemplo).

## Consultas de referência

`back/database/selects.sql/` — joins ideia+gênero, subgêneros, personagens, cenários.

## Inconsistências documentais

- README e `docs/arquitetura.md` mencionam **MySQL**
- DDL e `config_banco.py` usam **PostgreSQL**

---

_Gerado pelo workflow `bmad-document-project`._
