--Creates a db, creates a user and gives privileges to the user

--create db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--grant permissions
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
--grant permissions
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
