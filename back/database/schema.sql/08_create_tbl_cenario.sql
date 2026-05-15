-- =========================================================
-- TABELA: cenario
-- Cadastro base de cenários
-- =========================================================
CREATE TABLE cenario (
    id_cenario INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    tipo VARCHAR(50),
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP,
    CONSTRAINT chk_cenario_nome_nao_vazio
        CHECK (length(trim(nome)) > 0)
);