-- Lista cada ideia com todos os subgêneros associados a ela
SELECT 
    i.titulo AS ideia,  -- Título da ideia
    g.nome AS subgenero  -- Nome do subgênero associado
FROM ideia i
JOIN subgenero_ideia isg ON i.id_ideia = isg.id_ideia  
-- Relaciona ideias à tabela de associação de subgêneros
JOIN genero g ON isg.id_genero = g.id_genero  
-- Pega o nome do subgênero correspondente
ORDER BY i.id_ideia;  
-- Ordena para facilitar a leitura por ideia
