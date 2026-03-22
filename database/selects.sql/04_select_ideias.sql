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
