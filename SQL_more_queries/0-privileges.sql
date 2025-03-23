-- Task: Grant all privileges and list privileges of MySQL users 'user_0d_1' and 'user_0d_2' on localhost

-- Grant all privileges to 'user_0d_1' on localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Grant all privileges to 'user_0d_2' on localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;

-- Flush privileges to ensure changes take effect
FLUSH PRIVILEGES;

-- Show privileges for user 'user_0d_1' on localhost
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show privileges for user 'user_0d_2' on localhost
SHOW GRANTS FOR 'user_0d_2'@'localhost';
