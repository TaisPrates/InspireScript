-- =========================================================
-- INSERTS: ideia_subgenero
-- =========================================================
INSERT INTO ideia_subgenero (id_ideia, id_subgenero) VALUES
-- Ideia 1 recebe dois subgêneros
(1, (SELECT id_subgenero FROM subgenero WHERE nome = 'Fantasia épica')),
(1, (SELECT id_subgenero FROM subgenero WHERE nome = 'Fantasia urbana')),

-- Ideia 2 recebe um subgênero
(2, (SELECT id_subgenero FROM subgenero WHERE nome = 'Romance histórico')),

-- Ideia 3 recebe dois subgêneros
(3, (SELECT id_subgenero FROM subgenero WHERE nome = 'Noir')),
(3, (SELECT id_subgenero FROM subgenero WHERE nome = 'Thriller psicológico'));
