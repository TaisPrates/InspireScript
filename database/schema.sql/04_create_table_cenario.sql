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
