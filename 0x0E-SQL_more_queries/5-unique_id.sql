-- create table "unique_id"
-- add id and name, id must be unique and default is 1
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
