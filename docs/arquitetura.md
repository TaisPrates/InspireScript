# 🧩 Arquitetura

O InspireScript é estruturado como uma aplicação web com separação entre interface, camada de aplicação e persistência de dados.

A arquitetura segue um modelo em camadas, permitindo organização, escalabilidade e facilidade de manutenção.

---

## 🧱 Componentes

### Front-end
Responsável pela interface com o usuário.

- HTML
- CSS
- JavaScript (para interatividade)

---

### Back-end
Responsável pelas regras de negócio e comunicação com o banco de dados.

- Python
- FastAPI

---

### Banco de Dados
Responsável pela persistência das informações.

- MySQL (atual)
- PostgreSQL (evolução futura)

---

## 🔄 Fluxo da aplicação

Usuário → Interface → API (FastAPI) → Banco de Dados

---

## 📌 Observação

A arquitetura foi definida de forma modular, permitindo evolução gradual das tecnologias utilizadas sem comprometer a estrutura principal do sistema.
