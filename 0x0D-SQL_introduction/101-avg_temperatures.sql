-- average of temprater
SELECT city, AVG(value) AS temperature FROM temperatures
GROUP BY (city)
ORDER BY temperature DESC;
