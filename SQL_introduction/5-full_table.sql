-- This script prints the full description of the first_table in the hbtn_0c_0 database
-- The database name will be passed as an argument of the mysql command

SELECT `Create Table` 
FROM information_schema.tables 
WHERE table_name = 'first_table' 
AND table_schema = 'hbtn_0c_0';
