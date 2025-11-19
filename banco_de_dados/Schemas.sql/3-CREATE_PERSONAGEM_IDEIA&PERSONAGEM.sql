/* -------------------------------------------------
Tabela: personagem
Armazena os personagens das ideias literárias
------------------------------------------------- */
CREATE TABLE personagem (
    id_personagem INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,          -- Nome do personagem
    descricao TEXT,                       -- Descrição ou detalhes do personagem
    papel ENUM('principal','coadjuvante') DEFAULT 'coadjuvante', -- Papel na história
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

/* -------------------------------------------------
Tabela: ideia_personagem
Relaciona personagens às ideias (N:N)
------------------------------------------------- */
CREATE TABLE ideia_personagem (
    id_ideia INT NOT NULL,
    id_personagem INT NOT NULL,
    PRIMARY KEY (id_ideia, id_personagem),
    FOREIGN KEY (id_ideia) REFERENCES ideia(id_ideia) ON DELETE CASCADE,
    FOREIGN KEY (id_personagem) REFERENCES personagem(id_personagem) ON DELETE CASCADE
);
