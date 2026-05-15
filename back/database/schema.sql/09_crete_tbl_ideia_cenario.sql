-- =========================================================
-- TABELA: ideia_cenario
-- Relação N:N entre ideia e cenário
-- =========================================================
CREATE TABLE ideia_cenario (
    id_ideia INTEGER NOT NULL,
    id_cenario INTEGER NOT NULL,
    PRIMARY KEY (id_ideia, id_cenario),
    CONSTRAINT fk_ideia_cenario_ideia
        FOREIGN KEY (id_ideia)
        REFERENCES ideia(id_ideia)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_ideia_cenario_cenario
        FOREIGN KEY (id_cenario)
        REFERENCES cenario(id_cenario)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);