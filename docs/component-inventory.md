# InspireScript — Inventário de Componentes

**Tipo de projeto:** Backend (sem componentes UI)

Este inventário lista **módulos Python** e **artefatos SQL** em vez de componentes visuais.

## Interfaces

| Componente | Arquivo | Funções principais |
|------------|---------|-------------------|
| API FastAPI | `back/core/main.py` | `home`, `listar_ideias`, `criar_ideia` |
| CLI Menu | `back/core/cli/menu.py` | `menu_principal`, `menu_ideias`, `menu_personagens`, `menu_generos`, `menu_papeis` |

## Configuração

| Componente | Arquivo | Exporta |
|------------|---------|---------|
| Conexão BD | `back/core/config/config_banco.py` | `conectar()` |

## Repositórios (camada de dados)

| Módulo | Funções | Tabelas |
|--------|---------|---------|
| `ideia.py` | `inserir_ideia`, `listar_ideias`, `buscar_ideia_detalhada`, `atualizar_ideia`, `deletar_ideia` | `ideia` |
| `genero.py` | `inserir_genero`, `listar_generos`, `atualizar_genero`, `deletar_genero` | `genero` |
| `subgenero.py` | `inserir_subgenero`, `listar_subgeneros`, `atualizar_subgenero`, `deletar_subgenero` | `subgenero` |
| `ideia_subgenero.py` | `vincular_subgenero`, `listar_subgeneros_por_ideia`, `remover_vinculo_subgenero` | `ideia_subgenero` |
| `personagem.py` | `inserir_personagem`, `listar_personagens`, `buscar_personagem_detalhado`, `atualizar_personagem`, `deletar_personagem` | `personagem` |
| `papel_personagem.py` | `inserir_papel`, `listar_papeis`, `atualizar_papel`, `deletar_papel` | `papel_personagem` |
| `ideia_personagem.py` | `vincular_personagem_ideia`, `listar_elenco_da_ideia`, `mudar_papel_personagem`, `remover_personagem_da_ideia` | `ideia_personagem` |
| `cenario.py` | `inserir_cenario`, `listar_cenarios`, `buscar_cenario_detalhado`, `atualizar_cenario`, `deletar_cenario` | `cenario` |
| `ideia_cenario.py` | `vincular_cenario_ideia`, `listar_cenarios_da_ideia`, `remover_cenario_da_ideia` | `ideia_cenario` |
| `log_ideia.py` | `listar_historico_alteracoes`, `buscar_log_especifico` | `log_alteracao_ideia` |

## Cobertura CLI vs API

| Módulo | CLI | API HTTP |
|--------|-----|----------|
| ideia | ✅ | ✅ (parcial) |
| genero | ✅ | ❌ |
| subgenero | ✅ | ❌ |
| ideia_subgenero | ⚠️ (bug no menu) | ❌ |
| personagem | ✅ | ❌ |
| papel_personagem | ✅ parcial | ❌ |
| ideia_personagem | ✅ | ❌ |
| cenario | ❌ | ❌ |
| ideia_cenario | ❌ | ❌ |
| log_ideia | ✅ | ❌ |

## Artefatos de banco

| Pasta | Conteúdo |
|-------|----------|
| `back/database/schema.sql/` | 13+ scripts DDL, índices, trigger |
| `back/database/seed.sql/` | 10 scripts de carga inicial |
| `back/database/selects.sql/` | 4 consultas de exemplo |

## Componentes ausentes (planejados)

| Componente | Status |
|------------|--------|
| `front/` (HTML/CSS/JS) | Não existe |
| Camada de serviço | Não existe |
| Testes automatizados | Não existe |
| Autenticação | Não existe |
| Migrations automatizadas (Alembic) | Não existe |

---

_Gerado pelo workflow `bmad-document-project`._
