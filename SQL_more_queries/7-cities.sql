-- Create the database hbtn_0d_usa if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create the table cities if it does not already exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique ID, auto-incremented, primary key, and can't be NULL
    state_id INT NOT NULL,              -- Column state_id of type INT that can't be NULL
    name VARCHAR(256) NOT NULL,         -- Column name of type VARCHAR(256) that can't be NULL
    CONSTRAINT FK_state_id FOREIGN KEY (state_id) REFERENCES states(id)  -- Create a foreign key constraint referencing the id column of the states table
);

