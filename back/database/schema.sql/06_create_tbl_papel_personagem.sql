-- =========================================================
-- TABELA: papel_personagem
-- =========================================================
CREATE TABLE papel_personagem (
    id_papel INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    CONSTRAINT chk_papel_personagem_nome_nao_vazio
        CHECK (length(trim(nome)) > 0)
);

