DELIMITER $$

-- Garantir que o gênero principal seja do tipo 'principal'
CREATE TRIGGER trg_ideia_genero_principal
BEFORE INSERT ON ideia
FOR EACH ROW
BEGIN
    IF (SELECT tipo FROM genero WHERE id_genero = NEW.id_genero_principal) <> 'principal' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O gênero principal precisa ser do tipo "principal".';
    END IF;
END$$

CREATE TRIGGER trg_ideia_genero_principal_update
BEFORE UPDATE ON ideia
FOR EACH ROW
BEGIN
    IF (SELECT tipo FROM genero WHERE id_genero = NEW.id_genero_principal) <> 'principal' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O gênero principal precisa ser do tipo "principal".';
    END IF;
END$$

-- Garantir que os subgêneros sejam do tipo 'subgenero'
CREATE TRIGGER trg_ideia_subgenero
BEFORE INSERT ON ideia_subgenero
FOR EACH ROW
BEGIN
    IF (SELECT tipo FROM genero WHERE id_genero = NEW.id_genero) <> 'subgenero' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O gênero associado como subgênero precisa ser do tipo "subgenero".';
    END IF;
END$$

CREATE TRIGGER trg_ideia_subgenero_update
BEFORE UPDATE ON ideia_subgenero
FOR EACH ROW
BEGIN
    IF (SELECT tipo FROM genero WHERE id_genero = NEW.id_genero) <> 'subgenero' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O gênero associado como subgênero precisa ser do tipo "subgenero".';
    END IF;
END$$

DELIMITER ;
