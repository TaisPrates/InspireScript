-- Gêneros principais
INSERT INTO genero (nome, tipo, id_genero_pai) VALUES 
('Romance', 'principal', NULL),           -- id 1
('Fantasia', 'principal', NULL),          -- id 2
('Ficção científica', 'principal', NULL), -- id 3
('Terror', 'principal', NULL),            -- id 4
('Mistério', 'principal', NULL),          -- id 5
('Aventura', 'principal', NULL),          -- id 6
('Drama', 'principal', NULL),             -- id 7
('Humor', 'principal', NULL),             -- id 8
('Biografia', 'principal', NULL);         -- id 9

-- Subgêneros de Romance
INSERT INTO genero (nome, tipo, id_genero_pai) VALUES 
('Romance histórico', 'subgenero', 1),
('Romance contemporâneo', 'subgenero', 1),
('Romance policial', 'subgenero', 1),
('Romance paranormal', 'subgenero', 1),
('Chick lit', 'subgenero', 1),
('Romance erótico', 'subgenero', 1);

-- Subgêneros de Fantasia
INSERT INTO genero (nome, tipo, id_genero_pai) VALUES 
('Fantasia épica', 'subgenero', 2),
('Fantasia urbana', 'subgenero', 2),
('Fantasia sombria', 'subgenero', 2),
('Contos de fadas reimaginados', 'subgenero', 2);

-- Subgêneros de Ficção científica
INSERT INTO genero (nome, tipo, id_genero_pai) VALUES 
('Cyberpunk', 'subgenero', 3),
('Distopia', 'subgenero', 3),
('Viagem no tempo', 'subgenero', 3),
('Space opera', 'subgenero', 3),
('Ficção científica hard', 'subgenero', 3);

-- Subgêneros de Terror
INSERT INTO genero (nome, tipo, id_genero_pai) VALUES 
('Sobrenatural', 'subgenero', 4),
('Psicológico', 'subgenero', 4),
('Gore', 'subgenero', 4),
('Horror cósmico', 'subgenero', 4),
('Slasher', 'subgenero', 4);

-- Subgêneros de Mistério
INSERT INTO genero (nome, tipo, id_genero_pai) VALUES 
('Thriller psicológico', 'subgenero', 5),
('Policial', 'subgenero', 5),
('Noir', 'subgenero', 5),
('Suspense romântico', 'subgenero', 5);

-- Subgêneros de Aventura
INSERT INTO genero (nome, tipo, id_genero_pai) VALUES 
('Exploração', 'subgenero', 6),
('Sobrevivência', 'subgenero', 6),
('Viagem épica', 'subgenero', 6),
('Piratas', 'subgenero', 6);

-- Subgêneros de Drama
INSERT INTO genero (nome, tipo, id_genero_pai) VALUES 
('Drama familiar', 'subgenero', 7),
('Drama social', 'subgenero', 7),
('Drama psicológico', 'subgenero', 7),
('Tragicomédia', 'subgenero', 7);

-- Subgêneros de Humor
INSERT INTO genero (nome, tipo, id_genero_pai) VALUES 
('Satírico', 'subgenero', 8),
('Paródico', 'subgenero', 8),
('Comédia romântica', 'subgenero', 8),
('Humor negro', 'subgenero', 8);

-- Subgêneros de Biografia
INSERT INTO genero (nome, tipo, id_genero_pai) VALUES 
('Autobiografia', 'subgenero', 9),
('Biografia histórica', 'subgenero', 9),
('Memórias literárias', 'subgenero', 9);
