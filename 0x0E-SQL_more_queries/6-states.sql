-- auto generated primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.states (
	id INT UNIQUE DEFAULT (uuid()) NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);
