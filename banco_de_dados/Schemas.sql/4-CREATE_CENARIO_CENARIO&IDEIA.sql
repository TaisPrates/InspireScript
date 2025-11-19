/* -------------------------------------------------
Tabela: cenario
Armazena os cenários ou locais das ideias literárias
------------------------------------------------- */
CREATE TABLE cenario (
    id_cenario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,       -- Nome do cenário
    descricao TEXT,                   -- Descrição do cenário
    tipo ENUM('real','fantástico','mistério','outro') DEFAULT 'outro', -- Tipo do cenário
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
);
/* -------------------------------------------------
Tabela: ideia_cenario
Relaciona cenários às ideias (N:N)
------------------------------------------------- */
CREATE TABLE ideia_cenario (
    id_ideia INT NOT NULL,
    id_cenario INT NOT NULL,
    PRIMARY KEY (id_ideia, id_cenario),
    FOREIGN KEY (id_ideia) REFERENCES ideia(id_ideia) ON DELETE CASCADE,
    FOREIGN KEY (id_cenario) REFERENCES cenario(id_cenario) ON DELETE CASCADE
);
