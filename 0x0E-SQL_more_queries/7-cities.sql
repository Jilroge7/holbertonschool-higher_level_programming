-- create a database and table
-- add id, state_id, and name to table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, state_id INT NOT NULL FOREIGN KEY(id) REFERENCES `states`(`id`), name VARCHAR (256) NOT NULL);
