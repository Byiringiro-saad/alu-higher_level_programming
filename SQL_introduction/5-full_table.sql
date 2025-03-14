-- This script generates the CREATE TABLE statement for the 'first_table'

SELECT 
    CONCAT(
        TABLE_NAME, ' CREATE TABLE `', TABLE_NAME, '` (',
        GROUP_CONCAT(
            CONCAT(
                '`', COLUMN_NAME, '` ', COLUMN_TYPE,
                IF(IS_NULLABLE = 'NO', ' NOT NULL', ''),
                IF(COLUMN_DEFAULT IS NOT NULL, CONCAT(' DEFAULT ', COLUMN_DEFAULT), ''),
                IF(EXTRA != '', CONCAT(' ', EXTRA), '')
            ) ORDER BY ORDINAL_POSITION SEPARATOR ', '), 
        ', PRIMARY KEY(`id`)) ENGINE=', ENGINE,
        ' DEFAULT CHARSET=', TABLE_COLLATION
    ) AS create_table_query
FROM INFORMATION_SCHEMA.COLUMNS
JOIN INFORMATION_SCHEMA.TABLES
    ON COLUMNS.TABLE_NAME = TABLES.TABLE_NAME 
    AND COLUMNS.TABLE_SCHEMA = TABLES.TABLE_SCHEMA
WHERE COLUMNS.TABLE_SCHEMA = DATABASE() 
  AND COLUMNS.TABLE_NAME = 'first_table'
GROUP BY COLUMNS.TABLE_NAME, ENGINE, TABLE_COLLATION;
