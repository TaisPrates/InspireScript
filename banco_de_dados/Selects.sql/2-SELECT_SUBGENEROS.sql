/* ============================================================
02 - Listar todos os subgêneros de um gênero específico
Exemplo: subgêneros de Romance (id = 1)
============================================================ */
SELECT * 
FROM genero 
WHERE id_genero_pai = 1;
