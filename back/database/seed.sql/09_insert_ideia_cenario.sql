INSERT INTO ideia_cenario (id_ideia, id_cenario)

-- A Jornada do Herói
SELECT i.id_ideia, c.id_cenario
FROM ideia i, cenario c
WHERE i.titulo = 'A Jornada do Herói'
  AND c.nome = 'Reino de Eldoria'

UNION ALL

-- Amor em Tempos de Guerra
SELECT i.id_ideia, c.id_cenario
FROM ideia i, cenario c
WHERE i.titulo = 'Amor em Tempos de Guerra'
  AND c.nome = 'Campo de Batalha de Arthen'

UNION ALL

-- Mistério na Mansão
SELECT i.id_ideia, c.id_cenario
FROM ideia i, cenario c
WHERE i.titulo = 'Mistério na Mansão'
  AND c.nome = 'Mansão Blackwood'

UNION ALL

-- O Último Guardião
SELECT i.id_ideia, c.id_cenario
FROM ideia i, cenario c
WHERE i.titulo = 'O Último Guardião'
  AND c.nome = 'Templo do Véu'

UNION ALL

-- Cartas Nunca Enviadas
SELECT i.id_ideia, c.id_cenario
FROM ideia i, cenario c
WHERE i.titulo = 'Cartas Nunca Enviadas'
  AND c.nome = 'Cidade das Cartas Perdidas'

UNION ALL

-- O Mistério do Relógio
SELECT i.id_ideia, c.id_cenario
FROM ideia i, cenario c
WHERE i.titulo = 'O Mistério do Relógio'
  AND c.nome = 'Oficina do Relógio Antigo'

UNION ALL

-- A Floresta Proibida
SELECT i.id_ideia, c.id_cenario
FROM ideia i, cenario c
WHERE i.titulo = 'A Floresta Proibida'
  AND c.nome = 'Floresta Proibida'

UNION ALL

-- Entre Dois Mundos
SELECT i.id_ideia, c.id_cenario
FROM ideia i, cenario c
WHERE i.titulo = 'Entre Dois Mundos'
  AND c.nome = 'Cidade de Dois Mundos'

UNION ALL

-- Segredos do Convento
SELECT i.id_ideia, c.id_cenario
FROM ideia i, cenario c
WHERE i.titulo = 'Segredos do Convento'
  AND c.nome = 'Convento de Santa Luz';