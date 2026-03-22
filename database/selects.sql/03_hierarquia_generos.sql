/* ============================================================
03 - Listar todos os gêneros principais e seus respectivos subgêneros
Mostra em formato de "árvore" simplificada
============================================================ */
SELECT g1.nome AS genero_principal, 
       g2.nome AS subgenero
FROM genero g1
LEFT JOIN genero g2 
       ON g1.id_genero = g2.id_genero_pai
WHERE g1.tipo = 'principal'
ORDER BY g1.nome, g2.nome;

/* ------------------------------------------------------------
Verificar a hierarquia completa de um gênero específico
Exemplo: mostrar gênero principal junto com seus subgêneros
------------------------------------------------------------ */
SELECT g_principal.nome AS genero_principal,
       g_sub.nome AS subgenero
FROM genero g_sub
JOIN genero g_principal 
     ON g_sub.id_genero_pai = g_principal.id_genero
WHERE g_principal.nome = 'Fantasia';

/* ------------------------------------------------------------
Contar quantos subgêneros cada gênero principal possui
------------------------------------------------------------ */
SELECT g1.nome AS genero_principal,
       COUNT(g2.id_genero) AS qtd_subgeneros
FROM genero g1
LEFT JOIN genero g2 
       ON g1.id_genero = g2.id_genero_pai
WHERE g1.tipo = 'principal'
GROUP BY g1.nome
ORDER BY qtd_subgeneros DESC;
