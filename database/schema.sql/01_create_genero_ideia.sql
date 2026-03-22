/* -------------------------------------------------
Tabela: genero
Armazena gêneros principais e subgêneros
------------------------------------------------- */
CREATE TABLE genero (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo ENUM('principal','subgenero') NOT NULL,
    id_genero_pai INT NULL,
    CONSTRAINT fk_genero_pai FOREIGN KEY (id_genero_pai) REFERENCES genero(id_genero)
);

/* ----------------------------------------------------
Tabela: ideia
Cada ideia precisa ter um gênero principal
------------------------------------------------- */
CREATE TABLE ideia (
    id_ideia INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    subtitulo VARCHAR(200),
    id_genero_principal INT NOT NULL,
    descricao TEXT,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_genero_principal) REFERENCES genero(id_genero)
);

/* -------------------------------------------------
Tabela: subgenero_ideia
Permite que cada ideia tenha múltiplos subgêneros
------------------------------------------------- */
CREATE TABLE subgenero_ideia (
    id_ideia INT NOT NULL,
    id_genero INT NOT NULL,
    PRIMARY KEY (id_ideia, id_genero),
    FOREIGN KEY (id_ideia) REFERENCES ideia(id_ideia),
    FOREIGN KEY (id_genero) REFERENCES genero(id_genero)
);

-- Índices opcionais para performance
CREATE INDEX idx_ideia ON subgenero_ideia(id_ideia);
CREATE INDEX idx_genero ON subgenero_ideia(id_genero);


