INSERT INTO ideia_personagem (id_ideia, id_personagem, id_papel)

-- Ideia: A Jornada do Herói
SELECT 
    i.id_ideia,
    p.id_personagem,
    pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'A Jornada do Herói'
  AND p.nome = 'Luan'
  AND pp.nome = 'Protagonista'

UNION ALL

-- Amor em Tempos de Guerra
SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'Amor em Tempos de Guerra'
  AND p.nome = 'Clara'
  AND pp.nome = 'Protagonista'

UNION ALL

SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'Amor em Tempos de Guerra'
  AND p.nome = 'Mateus'
  AND pp.nome = 'Coadjuvante'

UNION ALL

-- Mistério na Mansão
SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'Mistério na Mansão'
  AND p.nome = 'Detetive Henrique'
  AND pp.nome = 'Protagonista'

UNION ALL

-- O Último Guardião
SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'O Último Guardião'
  AND p.nome = 'Ayla'
  AND pp.nome = 'Protagonista'

UNION ALL

-- Cartas Nunca Enviadas
SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'Cartas Nunca Enviadas'
  AND p.nome = 'Clara'
  AND pp.nome = 'Protagonista'

UNION ALL

SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'Cartas Nunca Enviadas'
  AND p.nome = 'Mateus'
  AND pp.nome = 'Coadjuvante'

UNION ALL

-- O Mistério do Relógio
SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'O Mistério do Relógio'
  AND p.nome = 'Detetive Henrique'
  AND pp.nome = 'Protagonista'

UNION ALL

-- A Floresta Proibida
SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'A Floresta Proibida'
  AND p.nome = 'Explorador Rafael'
  AND pp.nome = 'Protagonista'

UNION ALL

SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'A Floresta Proibida'
  AND p.nome = 'Elena'
  AND pp.nome = 'Coadjuvante'

UNION ALL

-- Entre Dois Mundos
SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'Entre Dois Mundos'
  AND p.nome = 'Lucas'
  AND pp.nome = 'Protagonista'

UNION ALL

SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'Entre Dois Mundos'
  AND p.nome = 'Sofia'
  AND pp.nome = 'Protagonista'

UNION ALL

-- Segredos do Convento
SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'Segredos do Convento'
  AND p.nome = 'Detetive Henrique'
  AND pp.nome = 'Protagonista'

UNION ALL

SELECT i.id_ideia, p.id_personagem, pp.id_papel
FROM ideia i, personagem p, papel_personagem pp
WHERE i.titulo = 'Segredos do Convento'
  AND p.nome = 'Irmã Beatriz'
  AND pp.nome = 'Coadjuvante';