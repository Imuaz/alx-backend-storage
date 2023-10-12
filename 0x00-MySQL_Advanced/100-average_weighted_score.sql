-- script that creates a stored procedure that computes and store the
-- average weighted score for a student.
DELIMITER |
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE average_weighted_score DECIMAL(10, 2);

    -- Calculate the average weighted score for the user
    SELECT AVG(corrections.score * projects.weight) INTO average_weighted_score
    FROM corrections
    INNER JOIN projects
    ON projects.id = corrections.project_id
    where corrections.user_id = user_id;

    -- Update the user's average_score column with the calculated average weighted score
    UPDATE users set average_score = average_weighted_score
    where users.id = user_id;
END;
|
