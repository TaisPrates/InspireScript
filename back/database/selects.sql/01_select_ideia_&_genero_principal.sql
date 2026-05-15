SELECT
    i.id_ideia,
    i.titulo,
    g.nome AS genero_principal
FROM ideia i
JOIN genero g ON g.id_genero = i.id_genero_principal
ORDER BY i.id_ideia;