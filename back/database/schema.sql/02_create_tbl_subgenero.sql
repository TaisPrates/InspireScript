-- =========================================================
-- TABELA: subgenero
-- Subgêneros ligados a um gênero principal
-- Ex.: Romance histórico -> Romance
-- =========================================================
CREATE TABLE subgenero (
    id_subgenero INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_genero_pai INTEGER NOT NULL,
    CONSTRAINT fk_subgenero_genero_pai
        FOREIGN KEY (id_genero_pai)
        REFERENCES genero(id_genero)
        ON UPDATE RESTRICT
        ON DELETE RESTRICT,
    CONSTRAINT uq_subgenero_nome_genero UNIQUE (nome, id_genero_pai),
    CONSTRAINT chk_subgenero_nome_nao_vazio
        CHECK (length(trim(nome)) > 0)
);