-- This script lists all records from 'second_table' with a non-null 'name' value,
-- ordered by descending score, displaying score and name in that order.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
