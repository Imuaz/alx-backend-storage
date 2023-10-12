-- script that creates a trigger that resets the attribute `valid_email`
-- only when the `email` has been changed.

CREATE TRIGGER update_valid_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET valid_email = 0
    END IF;
END;
