-- script that creates a stored procedure AddBonus
-- that adds a new correction for a student.
DELIMITER //
CREATE PROCEDURE AddBonus (
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score INT
)
AS
BEGIN
  -- Check if the project exists
  IF NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name)
  THEN
    -- Create the project
    INSERT INTO projects (name) VALUES (project_name);
  END IF;

  -- Get the project ID
  DECLARE project_id INT;
  SET project_id = (SELECT id FROM projects WHERE name = project_name);

  -- Insert the new correction
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END;
//
DELIMITER;
