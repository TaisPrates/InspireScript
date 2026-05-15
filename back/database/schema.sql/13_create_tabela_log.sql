CREATE TABLE log_alteracao_ideia (
    id_log INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_ideia INTEGER,
    descricao_antiga TEXT,
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);