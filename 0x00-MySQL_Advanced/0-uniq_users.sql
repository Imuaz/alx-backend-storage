-- script that creates a table users
CREATE TABLE IF NOT EXISTS users (id int AUTO_INCREMENT PRIMARY KEY NOT NULL, email VARCHAR(255) UNIQUE NOT NULL, name VARCHAR(255))
