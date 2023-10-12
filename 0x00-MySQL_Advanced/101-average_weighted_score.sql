-- script that creates a stored procedure that computes and store the average weighted
-- score for all students.
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    INNER JOIN (
        SELECT c.user_id, SUM(c.score * p.weight) / SUM(p.weight) AS avg_weighted_score
        FROM corrections c
        INNER JOIN projects p ON p.id = c.project_id
        GROUP BY c.user_id
    ) AS subquery ON users.id = subquery.user_id
    SET users.average_score = subquery.avg_weighted_score;
END;
|
DELIMITER ;
