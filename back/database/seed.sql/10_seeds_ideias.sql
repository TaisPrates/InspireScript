-- ==========================================
-- POPULAÇÃO DE TABELAS DE APOIO (DOMÍNIO)
-- ==========================================
INSERT INTO subgenero (nome, id_genero_pai) VALUES
-- Romance (agora com vírgula no final para continuar)
('New Adult', (SELECT id_genero FROM genero WHERE nome = 'Romance')),
('Enemies to Lovers', (SELECT id_genero FROM genero WHERE nome = 'Romance')),

-- Fantasia
('Romantasia', (SELECT id_genero FROM genero WHERE nome = 'Fantasia')),
('Steampunk', (SELECT id_genero FROM genero WHERE nome = 'Fantasia')),
('Low Fantasy', (SELECT id_genero FROM genero WHERE nome = 'Fantasia')),

-- Ficção Científica
('Pós-apocalíptico', (SELECT id_genero FROM genero WHERE nome = 'Ficção científica')),
('Utopia', (SELECT id_genero FROM genero WHERE nome = 'Ficção científica')),
('Ficção Científica Soft', (SELECT id_genero FROM genero WHERE nome = 'Ficção científica')),
('Realidade Virtual', (SELECT id_genero FROM genero WHERE nome = 'Ficção científica')),
('Inteligência Artificial', (SELECT id_genero FROM genero WHERE nome = 'Ficção científica')),
('Solarpunk', (SELECT id_genero FROM genero WHERE nome = 'Ficção científica')),

-- Mistério
('Thriller médico', (SELECT id_genero FROM genero WHERE nome = 'Mistério')),
('Mistério de Quarto Fechado', (SELECT id_genero FROM genero WHERE nome = 'Mistério')),
('Techno-thriller', (SELECT id_genero FROM genero WHERE nome = 'Mistério')),
('Cybersegurança', (SELECT id_genero FROM genero WHERE nome = 'Mistério')),
('Investigação Digital', (SELECT id_genero FROM genero WHERE nome = 'Mistério')),
('Espionagem', (SELECT id_genero FROM genero WHERE nome = 'Mistério')),

-- Aventura
('Capa e Espada', (SELECT id_genero FROM genero WHERE nome = 'Aventura')),
('Western', (SELECT id_genero FROM genero WHERE nome = 'Aventura')),

-- Humor
('Comédia de Costumes', (SELECT id_genero FROM genero WHERE nome = 'Humor')),
('Humor Absurdo', (SELECT id_genero FROM genero WHERE nome = 'Humor')); 



-- ==========================================
-- CADASTRO DE IDEIAS LITERÁRIAS
-- ==========================================
INSERT INTO ideia (titulo, id_genero_principal, descricao) VALUES
(
    'RESET: Ponto de Ruptura',
    (SELECT id_genero FROM genero WHERE nome = 'Mistério'),
    'Thalassa é uma hacktivista decidida a expor empresas corruptas. Em uma de suas investigações, ela é rastreada por um hacker ético... que não é um estranho. Ele a conhece melhor do que ela imagina. E agora, os dois estão em lados opostos de uma mesma verdade.'
);

INSERT INTO personagem (nome, descricao) VALUES
('Thalassa', 'Jovem hachtivista que acredita que o sistema pode ser derrubado.'),
('Kylan', 'Hacker ético que acredita que o sistema precisa existir.'),
('Lívia', 'Jornalista investigativa tentando expor a podridão do mundo.'),
('Umbra', 'Ex-militar que sobreviveu ao sistema.');



-- ==========================================
-- VÍNCULOS (TABELAS INTERMEDIÁRIAS)
-- ==========================================
INSERT INTO ideia_subgenero (id_ideia, id_subgenero) VALUES
((SELECT id_ideia FROM ideia WHERE titulo = 'RESET: Ponto de Ruptura'), (SELECT id_subgenero FROM subgenero WHERE nome = 'Suspense romântico')),
((SELECT id_ideia FROM ideia WHERE titulo = 'RESET: Ponto de Ruptura'), (SELECT id_subgenero FROM subgenero WHERE nome = 'Cybersegurança')),
((SELECT id_ideia FROM ideia WHERE titulo = 'RESET: Ponto de Ruptura'), (SELECT id_subgenero FROM subgenero WHERE nome = 'Techno-thriller'));



INSERT INTO ideia_personagem (id_ideia, id_personagem, id_papel)

SELECT 
    i.id_ideia,
    p.id_personagem,
    pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'RESET: Ponto de Ruptura'
  AND p.nome = 'Thalassa'
  AND pp.nome = 'Protagonista'

UNION ALL

SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'RESET: Ponto de Ruptura'
  AND p.nome = 'Kylan'
  AND pp.nome = 'Protagonista'

UNION ALL

SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'RESET: Ponto de Ruptura'
  AND p.nome = 'Lívia'
  AND pp.nome = 'Coadjuvante'

UNION ALL


SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'RESET: Ponto de Ruptura'
  AND p.nome = 'Umbra'
  AND pp.nome = 'Coadjuvante';








SELECT 
    i.titulo,
    g.nome AS genero_principal,
    STRING_AGG(DISTINCT s.nome, ', ') AS subgeneros,
    STRING_AGG(DISTINCT p.nome || ' (' || pp.nome || ')', ', ') AS personagens,
    STRING_AGG(DISTINCT c.nome, ', ') AS cenarios
FROM ideia i
JOIN genero g ON g.id_genero = i.id_genero_principal
LEFT JOIN ideia_subgenero isg ON isg.id_ideia = i.id_ideia
LEFT JOIN subgenero s ON s.id_subgenero = isg.id_subgenero
LEFT JOIN ideia_personagem ip ON ip.id_ideia = i.id_ideia
LEFT JOIN personagem p ON p.id_personagem = ip.id_personagem
LEFT JOIN papel_personagem pp ON pp.id_papel = ip.id_papel
LEFT JOIN ideia_cenario ic ON ic.id_ideia = i.id_ideia
LEFT JOIN cenario c ON c.id_cenario = ic.id_cenario
GROUP BY i.titulo, g.nome
ORDER BY i.titulo;


