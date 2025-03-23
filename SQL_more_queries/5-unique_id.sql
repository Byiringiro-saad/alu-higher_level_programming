-- Create the table unique_id if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL UNIQUE DEFAULT 1, -- Column id of type INT, must be unique, cannot be NULL, with a default value of 1
    name VARCHAR(256)                 -- Column name of type VARCHAR(256)
);

