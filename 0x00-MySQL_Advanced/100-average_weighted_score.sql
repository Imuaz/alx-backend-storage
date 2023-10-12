-- script that creates a stored procedure that computes and store the
-- average weighted score for a student.
DELIMITER |
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    UPDATE users
    INNER JOIN (
        SELECT corrections.user_id, SUM(corrections.score * projects.weight) / SUM(projects.weight) AS avg_weighted_score
        FROM corrections
        INNER JOIN projects ON projects.id = corrections.project_id
        WHERE corrections.user_id = user_id
        GROUP BY corrections.user_id
    ) AS subquery ON users.id = subquery.user_id
    SET users.average_score = subquery.avg_weighted_score;
END;
|
DELIMITER;
