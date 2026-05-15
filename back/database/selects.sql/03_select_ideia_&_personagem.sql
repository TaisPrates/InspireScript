SELECT
    i.titulo,
    p.nome AS personagem,
    pp.nome AS papel
FROM ideia i
JOIN ideia_personagem ip ON ip.id_ideia = i.id_ideia
JOIN personagem p ON p.id_personagem = ip.id_personagem
JOIN papel_personagem pp ON pp.id_papel = ip.id_papel
ORDER BY i.titulo;