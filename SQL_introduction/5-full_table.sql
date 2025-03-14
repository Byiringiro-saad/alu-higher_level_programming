-- This script prints the full description of the 'first_table' from the database hbtn_0c_0

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, EXTRA
FROM information_schema.columns
WHERE table_name = 'first_table'
  AND table_schema = DATABASE();
