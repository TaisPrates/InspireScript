-- =========================================================
-- TABELA: ideia
-- Cada ideia possui 1 gênero principal
-- =========================================================
CREATE TABLE ideia (
    id_ideia INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    subtitulo VARCHAR(200),
    descricao TEXT,
    id_genero_principal INTEGER NOT NULL,
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_ideia_genero_principal
        FOREIGN KEY (id_genero_principal)
        REFERENCES genero(id_genero)
        ON UPDATE RESTRICT
        ON DELETE RESTRICT,
    CONSTRAINT chk_ideia_titulo_nao_vazio
        CHECK (length(trim(titulo)) > 0)
);