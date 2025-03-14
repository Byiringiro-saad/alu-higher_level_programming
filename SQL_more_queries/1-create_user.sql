#!/bin/bash
# Task: Create MySQL user 'user_0d_1' with all privileges on the MySQL server if not exists
# This script will create the MySQL user 'user_0d_1' with all privileges on all databases and set the password to 'user_0d_1_pwd'.
# If the user already exists, no error will occur.

# Connect to MySQL server and run the following SQL commands

mysql -u root -p <<EOF
-- Check if the user 'user_0d_1' already exists, and create it if not
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to ensure the changes take effect
FLUSH PRIVILEGES;
EOF
