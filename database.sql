DROP DATABASE IF EXISTS PhotoBomb;
CREATE DATABASE PhotoBomb;
USE PhotoBomb;
CREATE TABLE User
(
ID int NOT NULL AUTO_INCREMENT,
firstname varchar(255),
lastname varchar(255),
email varchar(255),
password varchar(255),
PRIMARY KEY (ID)
);

CREATE TABLE Image
(
ID int NOT NULL AUTO_INCREMENT,
user_ID int,
name varchar(100),
is_private tinyint default 0,
PRIMARY KEY (ID) 
);
