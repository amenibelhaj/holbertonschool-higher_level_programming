-- This script lists all records from the second_table
-- Results are ordered by score in descending order (top score first)
-- Only the score and name will be displayed

SELECT score, name
FROM second_table
ORDER BY score DESC;
