-- =========================================================
-- TABELA: personagem
-- Cadastro base de personagens
-- O papel fica na relação com a ideia
-- =========================================================
CREATE TABLE personagem (
    id_personagem INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_personagem_nome_nao_vazio
        CHECK (length(trim(nome)) > 0)
);