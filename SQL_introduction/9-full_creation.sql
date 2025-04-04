-- This script creates the table 'second_table' if it doesn't exist and inserts multiple rows

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert multiple records into the table
INSERT INTO second_table (id, name, score)
VALUES 
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
