SELECT
    i.titulo,
    c.nome AS cenario
FROM ideia i
JOIN ideia_cenario ic ON ic.id_ideia = i.id_ideia
JOIN cenario c ON c.id_cenario = ic.id_cenario
ORDER BY i.titulo;