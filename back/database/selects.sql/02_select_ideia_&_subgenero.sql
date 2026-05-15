SELECT
    i.titulo,
    s.nome AS subgenero
FROM ideia i
JOIN ideia_subgenero isg ON isg.id_ideia = i.id_ideia
JOIN subgenero s ON s.id_subgenero = isg.id_subgenero
ORDER BY i.titulo;