-- Mostra cada ideia com seu gênero principal e uma lista de todos os subgêneros associados
SELECT 
    i.titulo AS ideia,                   -- Título da ideia
    gp.nome AS genero_principal,         -- Nome do gênero principal
    GROUP_CONCAT(gs.nome SEPARATOR ', ') AS subgeneros  
    -- Concatena todos os subgêneros em uma única coluna, separados por vírgula
FROM ideia i
JOIN genero gp ON i.id_genero_principal = gp.id_genero  
-- Relaciona a ideia com o gênero principal
LEFT JOIN subgenero_ideia isg ON i.id_ideia = isg.id_ideia  
-- Faz LEFT JOIN para incluir ideias que podem não ter subgêneros
LEFT JOIN genero gs ON isg.id_genero = gs.id_genero  
-- Pega o nome de cada subgênero associado
GROUP BY i.id_ideia, i.titulo, gp.nome;  
-- Agrupa por ideia para usar o GROUP_CONCAT
