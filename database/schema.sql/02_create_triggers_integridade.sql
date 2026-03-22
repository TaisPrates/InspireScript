DELIMITER $$

-- Gênero principal válido em ideia
CREATE TRIGGER trg_ideia_genero_principal
BEFORE INSERT ON ideia
FOR EACH ROW
BEGIN
    DECLARE tipo_genero ENUM('principal','subgenero');
    SELECT tipo INTO tipo_genero FROM genero WHERE id_genero = NEW.id_genero_principal;
    IF tipo_genero <> 'principal' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O gênero principal precisa ser do tipo "principal".';
    END IF;
END$$

CREATE TRIGGER trg_ideia_genero_principal_update
BEFORE UPDATE ON ideia
FOR EACH ROW
BEGIN
    DECLARE tipo_genero ENUM('principal','subgenero');
    SELECT tipo INTO tipo_genero FROM genero WHERE id_genero = NEW.id_genero_principal;
    IF tipo_genero <> 'principal' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O gênero principal precisa ser do tipo "principal".';
    END IF;
END$$

-- Subgêneros válidos em ideia_subgenero
CREATE TRIGGER trg_ideia_subgenero_insert
BEFORE INSERT ON ideia_subgenero
FOR EACH ROW
BEGIN
    DECLARE tipo_genero ENUM('principal','subgenero');
    SELECT tipo INTO tipo_genero FROM genero WHERE id_genero = NEW.id_genero;
    IF tipo_genero <> 'subgenero' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O gênero associado como subgênero precisa ser do tipo "subgenero".';
    END IF;
END$$

CREATE TRIGGER trg_ideia_subgenero_update
BEFORE UPDATE ON ideia_subgenero
FOR EACH ROW
BEGIN
    DECLARE tipo_genero ENUM('principal','subgenero');
    SELECT tipo INTO tipo_genero FROM genero WHERE id_genero = NEW.id_genero;
    IF tipo_genero <> 'subgenero' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O gênero associado como subgênero precisa ser do tipo "subgenero".';
    END IF;
END$$

DELIMITER ;
