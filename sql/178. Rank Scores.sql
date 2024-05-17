SELECT score, 
       (SELECT COUNT(DISTINCT score) + 1 
        FROM Scores 
        WHERE score > s.score) AS `rank`
FROM Scores s
ORDER BY score DESC;
