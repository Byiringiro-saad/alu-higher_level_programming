-- This script lists all databases on the MySQL server

SELECT DISTINCT SCHEMA_NAME
FROM INFORMATION_SCHEMA.SCHEMATA
WHERE SCHEMA_NAME != 'information_schema'
  AND SCHEMA_NAME != 'performance_schema'
  AND SCHEMA_NAME != 'mysql'
  AND SCHEMA_NAME != 'sys';
