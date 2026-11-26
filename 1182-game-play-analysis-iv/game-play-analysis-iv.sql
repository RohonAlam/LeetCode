WITH CTE AS (
    SELECT
        *,
        MIN(event_date) OVER (PARTITION BY player_id) AS login
    FROM Activity
)

SELECT
    ROUND(
        COUNT(DISTINCT b.player_id) * 1.0 / (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
    
FROM CTE a
LEFT JOIN Activity b
    ON a.player_id = b.player_id
    AND b.event_date = DATE_ADD(a.login, INTERVAL 1 DAY);