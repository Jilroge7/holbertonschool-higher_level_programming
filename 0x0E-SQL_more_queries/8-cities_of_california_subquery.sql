-- list all the cities of state california
-- sort ascending order
SELECT `id`, `name` FROM `cities` WHERE states.name = `California` ORDER BY cities.id ASC;
