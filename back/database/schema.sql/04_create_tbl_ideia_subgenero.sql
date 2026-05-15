-- =========================================================
-- TABELA: ideia_subgenero
-- Relação N:N entre ideia e subgênero
-- =========================================================
CREATE TABLE ideia_subgenero (
    id_ideia INTEGER NOT NULL,
    id_subgenero INTEGER NOT NULL,
    PRIMARY KEY (id_ideia, id_subgenero),
    CONSTRAINT fk_ideia_subgenero_ideia
        FOREIGN KEY (id_ideia)
        REFERENCES ideia(id_ideia)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_ideia_subgenero_subgenero
        FOREIGN KEY (id_subgenero)
        REFERENCES subgenero(id_subgenero)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
