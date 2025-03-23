-- Create user 'user_0d_1' on localhost without a password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Create user 'user_0d_2' on localhost without a password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant all privileges to 'user_0d_1' on localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Grant all privileges to 'user_0d_2' on localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- Show privileges for 'user_0d_1'
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show privileges for 'user_0d_2'
SHOW GRANTS FOR 'user_0d_2'@'localhost';
