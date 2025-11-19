-- Seleciona todas as ideias, mostrando também o gênero principal de cada uma
SELECT 
    i.id_ideia,           -- ID da ideia
    i.titulo,             -- Título da ideia
    i.subtitulo,          -- Subtítulo da ideia
    g.nome AS genero_principal,  -- Nome do gênero principal
    i.descricao,          -- Descrição da ideia
    i.data_criacao        -- Data de criação da ideia
FROM ideia i
JOIN genero g ON i.id_genero_principal = g.id_genero;  
-- JOIN para relacionar cada ideia ao seu gênero principal



-- Lista cada ideia com todos os subgêneros associados a ela
SELECT 
    i.titulo AS ideia,  -- Título da ideia
    g.nome AS subgenero  -- Nome do subgênero associado
FROM ideia i
JOIN ideia_subgenero isg ON i.id_ideia = isg.id_ideia  
-- Relaciona ideias à tabela de associação de subgêneros
JOIN genero g ON isg.id_genero = g.id_genero  
-- Pega o nome do subgênero correspondente
ORDER BY i.id_ideia;  
-- Ordena para facilitar a leitura por ideia



-- Mostra cada ideia com seu gênero principal e uma lista de todos os subgêneros associados
SELECT 
    i.titulo AS ideia,                   -- Título da ideia
    gp.nome AS genero_principal,         -- Nome do gênero principal
    GROUP_CONCAT(gs.nome SEPARATOR ', ') AS subgeneros  
    -- Concatena todos os subgêneros em uma única coluna, separados por vírgula
FROM ideia i
JOIN genero gp ON i.id_genero_principal = gp.id_genero  
-- Relaciona a ideia com o gênero principal
LEFT JOIN ideia_subgenero isg ON i.id_ideia = isg.id_ideia  
-- Faz LEFT JOIN para incluir ideias que podem não ter subgêneros
LEFT JOIN genero gs ON isg.id_genero = gs.id_genero  
-- Pega o nome de cada subgênero associado
GROUP BY i.id_ideia, i.titulo, gp.nome;  
-- Agrupa por ideia para usar o GROUP_CONCAT
