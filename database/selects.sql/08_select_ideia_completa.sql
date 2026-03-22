-- Uma visão completa de cada ideia: gênero principal, subgêneros e personagens
SELECT 
    i.titulo AS ideia,                        -- Título da ideia
    gp.nome AS genero_principal,              -- Nome do gênero principal
    GROUP_CONCAT(DISTINCT gs.nome SEPARATOR ', ') AS subgeneros,  -- Todos os subgêneros, concatenados
    GROUP_CONCAT(DISTINCT p.nome SEPARATOR ', ') AS personagens   -- Todos os personagens, concatenados
FROM ideia i
JOIN genero gp ON i.id_genero_principal = gp.id_genero
LEFT JOIN subgenero_ideia isg ON i.id_ideia = isg.id_ideia   -- Inclui subgêneros (se houver)
LEFT JOIN genero gs ON isg.id_genero = gs.id_genero
LEFT JOIN ideia_personagem ip ON i.id_ideia = ip.id_ideia     -- Inclui personagens (se houver)
LEFT JOIN personagem p ON ip.id_personagem = p.id_personagem
GROUP BY i.id_ideia, i.titulo, gp.nome
ORDER BY i.id_ideia;
