-- =========================================================
-- INSERTS: subgenero
-- =========================================================
INSERT INTO subgenero (nome, id_genero_pai) VALUES
-- Subgêneros de Romance
('Romance histórico',        (SELECT id_genero FROM genero WHERE nome = 'Romance')),
('Romance contemporâneo',    (SELECT id_genero FROM genero WHERE nome = 'Romance')),
('Romance policial',         (SELECT id_genero FROM genero WHERE nome = 'Romance')),
('Romance paranormal',       (SELECT id_genero FROM genero WHERE nome = 'Romance')),
('Chick lit',                (SELECT id_genero FROM genero WHERE nome = 'Romance')),
('Romance erótico',          (SELECT id_genero FROM genero WHERE nome = 'Romance')),

-- Subgêneros de Fantasia
('Fantasia épica',               (SELECT id_genero FROM genero WHERE nome = 'Fantasia')),
('Fantasia urbana',              (SELECT id_genero FROM genero WHERE nome = 'Fantasia')),
('Fantasia sombria',             (SELECT id_genero FROM genero WHERE nome = 'Fantasia')),
('Contos de fadas reimaginados', (SELECT id_genero FROM genero WHERE nome = 'Fantasia')),

-- Subgêneros de Ficção científica
('Cyberpunk',                (SELECT id_genero FROM genero WHERE nome = 'Ficção científica')),
('Distopia',                 (SELECT id_genero FROM genero WHERE nome = 'Ficção científica')),
('Viagem no tempo',          (SELECT id_genero FROM genero WHERE nome = 'Ficção científica')),
('Space opera',              (SELECT id_genero FROM genero WHERE nome = 'Ficção científica')),
('Ficção científica hard',   (SELECT id_genero FROM genero WHERE nome = 'Ficção científica')),

-- Subgêneros de Terror
('Sobrenatural',             (SELECT id_genero FROM genero WHERE nome = 'Terror')),
('Psicológico',              (SELECT id_genero FROM genero WHERE nome = 'Terror')),
('Gore',                     (SELECT id_genero FROM genero WHERE nome = 'Terror')),
('Horror cósmico',           (SELECT id_genero FROM genero WHERE nome = 'Terror')),
('Slasher',                  (SELECT id_genero FROM genero WHERE nome = 'Terror')),

-- Subgêneros de Mistério
('Thriller psicológico',     (SELECT id_genero FROM genero WHERE nome = 'Mistério')),
('Policial',                 (SELECT id_genero FROM genero WHERE nome = 'Mistério')),
('Noir',                     (SELECT id_genero FROM genero WHERE nome = 'Mistério')),
('Suspense romântico',       (SELECT id_genero FROM genero WHERE nome = 'Mistério')),

-- Subgêneros de Aventura
('Exploração',               (SELECT id_genero FROM genero WHERE nome = 'Aventura')),
('Sobrevivência',            (SELECT id_genero FROM genero WHERE nome = 'Aventura')),
('Viagem épica',             (SELECT id_genero FROM genero WHERE nome = 'Aventura')),
('Piratas',                  (SELECT id_genero FROM genero WHERE nome = 'Aventura')),

-- Subgêneros de Drama
('Drama familiar',           (SELECT id_genero FROM genero WHERE nome = 'Drama')),
('Drama social',             (SELECT id_genero FROM genero WHERE nome = 'Drama')),
('Drama psicológico',        (SELECT id_genero FROM genero WHERE nome = 'Drama')),
('Tragicomédia',             (SELECT id_genero FROM genero WHERE nome = 'Drama')),

-- Subgêneros de Humor
('Satírico',                 (SELECT id_genero FROM genero WHERE nome = 'Humor')),
('Paródico',                 (SELECT id_genero FROM genero WHERE nome = 'Humor')),
('Comédia romântica',        (SELECT id_genero FROM genero WHERE nome = 'Humor')),
('Humor negro',              (SELECT id_genero FROM genero WHERE nome = 'Humor')),

-- Subgêneros de Biografia
('Autobiografia',            (SELECT id_genero FROM genero WHERE nome = 'Biografia')),
('Biografia histórica',      (SELECT id_genero FROM genero WHERE nome = 'Biografia')),
('Memórias literárias',      (SELECT id_genero FROM genero WHERE nome = 'Biografia'));
