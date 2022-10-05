--Creates a db and user with permissions
--The db hbnb_test_db
--The user hbnb_test host localhost
--The password for hbnb_test is hbnb_test_pwd
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS `hbnb_test`@`localhost` IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test`.* TO `hbnb_test`@`localhost`;
GRANT SELECT ON `performance_schema`.* TO `hbnb_test`@`localhost`;
FLUSH PRIVILEGES;
