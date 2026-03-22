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