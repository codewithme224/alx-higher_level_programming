-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
USE hbtn_0c_0;
SELECT `city`, AVG(`value`) AS `avg_temperature`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temperature` DESC;
