-- list all the cities of state california
-- sort ascending order
SELECT `id`, `name`= (SELECT `name` FROM `states` WHERE `name` = `California`) FROM `cities` ORDER BY id ASC;
