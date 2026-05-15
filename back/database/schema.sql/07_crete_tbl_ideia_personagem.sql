-- ============================================
-- TABELA: ideia_personagem
-- Relação N:N entre ideia e personagem
-- Aqui fica o papel do personagem na ideia
-- ============================================
CREATE TABLE ideia_personagem (
    id_ideia INTEGER NOT NULL,
    id_personagem INTEGER NOT NULL,
    id_papel INTEGER NOT NULL,
    PRIMARY KEY (id_ideia, id_personagem),
    CONSTRAINT fk_ideia_personagem_ideia
        FOREIGN KEY (id_ideia)
        REFERENCES ideia(id_ideia)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_ideia_personagem_personagem
        FOREIGN KEY (id_personagem)
        REFERENCES personagem(id_personagem)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_ideia_personagem_papel
        FOREIGN KEY (id_papel)
        REFERENCES papel_personagem(id_papel)
        ON UPDATE RESTRICT
        ON DELETE RESTRICT
);