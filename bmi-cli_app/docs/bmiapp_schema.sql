DROP DATABASE IF EXISTS bmiapp;

CREATE DATABASE bmiapp;

USE bmiapp

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT AUTO_INCREMENT,
    name VARCHAR(64) NOT NULL,
    birthday DATE NOT NULL,
    height DECIMAL(4, 1) NOT NULL,
    target_weight DECIMAL(4, 1) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (name)
);

DROP TABLE IF EXISTS weight_records;

CREATE TABLE weight_records (
    id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    record_date DATETIME NOT NULL,
    height DECIMAL(4, 1) NOT NULL,
    weight DECIMAL(4, 1) NOT NULL,
    target_weight DECIMAL(4, 1) NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE weight_records
ADD CONSTRAINT user_FK1 FOREIGN KEY (user_id) REFERENCES users (id);