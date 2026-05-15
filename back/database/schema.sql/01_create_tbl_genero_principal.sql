-- =========================================================
-- TABELA: genero
-- Gêneros principais das ideias
-- Ex.: Romance, Fantasia, Terror
-- =========================================================
CREATE TABLE genero (
    id_genero INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    CONSTRAINT chk_genero_nome_nao_vazio
        CHECK (length(trim(nome)) > 0)
);
