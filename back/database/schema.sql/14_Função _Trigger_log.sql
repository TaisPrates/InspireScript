CREATE OR REPLACE FUNCTION salvar_historico_ideia()
RETURNS TRIGGER AS $$BEGIN
    -- Só salva no log se a descrição realmente mudou
    IF (OLD.descricao IS DISTINCT FROM NEW.descricao) THEN
        INSERT INTO log_alteracao_ideia (id_ideia, descricao_antiga)
        VALUES (OLD.id_ideia, OLD.descricao);
    END IF;
    RETURN NEW;
END;$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_log_ideia
BEFORE UPDATE ON ideia
FOR EACH ROW
EXECUTE FUNCTION salvar_historico_ideia();