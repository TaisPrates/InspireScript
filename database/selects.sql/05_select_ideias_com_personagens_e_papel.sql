-- Mostra cada ideia com os personagens associados e seu papel na história
SELECT 
    i.titulo AS ideia,     -- Título da ideia
    p.nome AS personagem,  -- Nome do personagem
    p.papel               -- Papel do personagem (principal ou coadjuvante)
FROM ideia i
JOIN ideia_personagem ip ON i.id_ideia = ip.id_ideia -- Relaciona ideias aos personagens
JOIN personagem p ON ip.id_personagem = p.id_personagem
ORDER BY i.id_ideia;
