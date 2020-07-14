-- list all the cities of state california
-- sort ascending order
SELECT `id`, `name` FROM `cities` WHERE `name` IN (SELECT `name` FROM `states` WHERE `name` = `California`) ORDER BY cities.id ASC;
