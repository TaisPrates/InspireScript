# 🧩 Arquitetura

## 📌 Visão geral

O InspireScript é estruturado como uma aplicação web com separação entre interface, camada de aplicação e persistência de dados.

A arquitetura segue um modelo em camadas, permitindo organização, escalabilidade e facilidade de manutenção.

---

## 🧱 Componentes

### Front-end
Responsável pela interação com o usuário.

- HTML
- CSS
- JavaScript (interatividade)

---

### Back-end
Responsável pelas regras de negócio e exposição da API.

- Python
- FastAPI

---

### Banco de dados
Responsável pela persistência das informações.

- MySQL (atual)
- PostgreSQL (evolução futura)

---

## 🔄 Fluxo da aplicação

```mermaid
flowchart TD
    A[Usuario] --> B[Front-end]
    B --> C[Interface HTML e CSS]
    B --> D[Interacoes JavaScript]
    D --> E[API FastAPI]
    E --> F[Rotas]
    E --> G[Regras de negocio]
    E --> H[Validacao de dados]
    G --> I[Persistencia]
    I --> J[Banco de dados MySQL]
