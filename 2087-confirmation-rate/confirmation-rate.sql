# Write your MySQL query statement below
SELECT s.user_id,
ROUND(IFNULL(SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(c.action), 0), 2) AS confirmation_rate
FROM signups s
LEFT JOIN confirmations c -- Fixed spelling
    ON s.user_id = c.user_id -- Added the missing ON clause
GROUP BY s.user_id;
