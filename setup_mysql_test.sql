-- script that prepares a MySQL server for the project
-- create a database hbnb_test_db
-- create a new user hbnb_test
-- The password of hbnb_test is hbnb_test_pwd
-- hbnb_test have SELECT privilege on the database performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
