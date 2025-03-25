-- Script to create the MySQL server user user_0d_1 with all privileges
-- The user should not be created again if already exists

-- Check if the user already exists and create it if it doesn't
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user on the MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';

-- Apply changes
FLUSH PRIVILEGES;