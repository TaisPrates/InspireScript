-- Associando subgêneros a ideias existentes
INSERT INTO ideia_subgenero (id_ideia, id_genero) VALUES
-- Ideia 1 recebe dois subgêneros
(1, (SELECT id_genero FROM genero WHERE nome='Fantasia Épica')),
(1, (SELECT id_genero FROM genero WHERE nome='Fantasia Urbana')),

-- Ideia 2 recebe um subgênero
(2, (SELECT id_genero FROM genero WHERE nome='Romance Histórico')),

-- Ideia 3 recebe dois subgêneros
(3, (SELECT id_genero FROM genero WHERE nome='Noir')),
(3, (SELECT id_genero FROM genero WHERE nome='Thriller Psicológico'));
