-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.name
FROM cities
WHERE states.name = 'California'
ORDER BY cities.id;
