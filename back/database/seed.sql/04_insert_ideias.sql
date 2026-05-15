-- =========================================================
-- INSERTS: ideia
-- =========================================================
INSERT INTO ideia (titulo, subtitulo, id_genero_principal, descricao) VALUES
(
    'A Jornada do Herói',
    'Uma aventura épica pelo mundo fantástico',
    (SELECT id_genero FROM genero WHERE nome = 'Fantasia'),
    'Um jovem herói descobre poderes antigos e enfrenta grandes desafios.'
),
(
    'Amor em Tempos de Guerra',
    'Romance em meio ao conflito',
    (SELECT id_genero FROM genero WHERE nome = 'Romance'),
    'Dois amantes tentam sobreviver durante um período turbulento.'
),
(
    'Mistério na Mansão',
    'Um suspense cheio de reviravoltas',
    (SELECT id_genero FROM genero WHERE nome = 'Mistério'),
    'Um detetive investiga estranhos acontecimentos em uma velha mansão.'
),
(
    'O Último Guardião',
    'A proteção de um segredo ancestral',
    (SELECT id_genero FROM genero WHERE nome = 'Fantasia'),
    'Um guardião protege um portal mágico que mantém o equilíbrio do mundo.'
),
(
    'Cartas Nunca Enviadas',
    'Histórias de amor e perda',
    (SELECT id_genero FROM genero WHERE nome = 'Romance'),
    'Um romance que se desenrola através de cartas não entregues.'
),
(
    'O Mistério do Relógio',
    'Segredos escondidos no tempo',
    (SELECT id_genero FROM genero WHERE nome = 'Mistério'),
    'Um relógio antigo contém pistas sobre desaparecimentos misteriosos.'
),
(
    'A Floresta Proibida',
    'Exploração e descobertas',
    (SELECT id_genero FROM genero WHERE nome = 'Fantasia'),
    'Um grupo de exploradores entra em uma floresta mágica cheia de perigos e enigmas.'
),
(
    'Entre Dois Mundos',
    'Conflito e escolhas',
    (SELECT id_genero FROM genero WHERE nome = 'Romance'),
    'Um casal enfrenta diferenças culturais e conflitos familiares em sua história de amor.'
),
(
    'Segredos do Convento',
    'Suspense e intrigas religiosas',
    (SELECT id_genero FROM genero WHERE nome = 'Mistério'),
    'Um detetive investiga estranhos eventos em um antigo convento cheio de segredos.'
);
