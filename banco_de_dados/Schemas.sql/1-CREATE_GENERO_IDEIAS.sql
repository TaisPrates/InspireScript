/* -------------------------------------------------
Tabela: genero
Armazena gêneros principais e subgêneros
------------------------------------------------- */
CREATE TABLE genero (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo ENUM('principal','subgenero') NOT NULL,
    id_genero_pai INT NULL,
    CONSTRAINT fk_genero_pai 
        FOREIGN KEY (id_genero_pai) 
        REFERENCES genero(id_genero)
        ON DELETE SET NULL  -- Se o gênero pai for deletado, subgêneros ficam sem pai
);

/* ----------------------------------------------------
Tabela: ideia
Cada ideia precisa ter um gênero principal
---------------------------------------------------- */
CREATE TABLE ideia (
    id_ideia INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    subtitulo VARCHAR(200),
    id_genero_principal INT NOT NULL,
    descricao TEXT,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_genero_principal) 
        REFERENCES genero(id_genero)
        ON DELETE RESTRICT  -- Impede deletar um gênero que ainda tem ideias
);

/* -------------------------------------------------
Tabela: ideia_subgenero
Permite que cada ideia tenha múltiplos subgêneros
------------------------------------------------- */
CREATE TABLE ideia_subgenero (
    id_ideia INT NOT NULL,
    id_genero INT NOT NULL,
    PRIMARY KEY (id_ideia, id_genero),
    FOREIGN KEY (id_ideia) 
        REFERENCES ideia(id_ideia)
        ON DELETE CASCADE,  -- Se a ideia for apagada, remove associações
    FOREIGN KEY (id_genero) 
        REFERENCES genero(id_genero)
        ON DELETE CASCADE   -- Se o subgênero for apagado, remove associações
);

/* -------------------------------------------------
Índices para melhorar performance nas consultas
------------------------------------------------- */
CREATE INDEX idx_ideia ON ideia_subgenero(id_ideia);
CREATE INDEX idx_genero ON ideia_subgenero(id_genero);

/* -------------------------------------------------
Observações:
1. 'ON DELETE SET NULL' ou 'ON DELETE CASCADE' ajuda na manutenção automática.
2. O uso de ENUM limita os tipos de gênero para consistência.
3. Com essa estrutura, você já consegue:
   - Criar gêneros e subgêneros
   - Associar ideias a múltiplos subgêneros
   - Evitar inconsistências quando registros são deletados
------------------------------------------------- */
