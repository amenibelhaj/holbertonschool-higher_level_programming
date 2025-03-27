-- 16-no_link.sql
-- This script lists all records from second_table where the name column is not NULL.
-- The results are ordered by descending score.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

