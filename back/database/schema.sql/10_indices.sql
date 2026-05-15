-- =========================================================
-- ÍNDICES
-- =========================================================
CREATE INDEX idx_ideia_genero_principal
    ON ideia (id_genero_principal);

CREATE INDEX idx_subgenero_genero_pai
    ON subgenero (id_genero_pai);

CREATE INDEX idx_ideia_subgenero_subgenero
    ON ideia_subgenero (id_subgenero);

CREATE INDEX idx_personagem_nome
    ON personagem (nome);

CREATE INDEX idx_ideia_personagem_personagem
    ON ideia_personagem (id_personagem);

CREATE INDEX idx_ideia_personagem_papel
    ON ideia_personagem (id_papel);

CREATE INDEX idx_cenario_nome
    ON cenario (nome);

CREATE INDEX idx_ideia_cenario_cenario
    ON ideia_cenario (id_cenario);

COMMIT;