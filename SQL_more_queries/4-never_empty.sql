-- Create the table id_not_null if it does not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1, -- Column id of type INT, cannot be NULL, with a default value of 1
    name VARCHAR(256)          -- Column name of type VARCHAR(256)
);

