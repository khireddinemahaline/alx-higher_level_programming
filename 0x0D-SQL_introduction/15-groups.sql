-- group score.
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER by score DESC;
