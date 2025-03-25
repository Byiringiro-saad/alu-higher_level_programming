-- Script to list all cities in California from the database hbtn_0d_usa

-- Select city names from cities table where the state_id matches California's id
-- We avoid using JOIN by using a subquery instead
SELECT cities.id, cities.name 
FROM cities 
WHERE cities.state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id ASC;