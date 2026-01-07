DROP DATABASE IF EXISTS 23010025_exam_db;

CREATE DATABASE 23010025_exam_db;

USE 23010025_exam_db;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  birthday DATE NOT NULL,
  experience INT NOT NULL,
  progress INT NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

DROP TABLE IF EXISTS todo_records;

CREATE TABLE todo_records (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  title TEXT NOT NULL,
  deadline DATE,
  priority INT NOT NULL,
  PRIMARY KEY (id)
);

ALTER TABLE todo_records ADD CONSTRAINT user_FK1
  FOREIGN KEY (user_id) REFERENCES users(id);

DROP TABLE IF EXISTS levels;

CREATE TABLE levels (
  id INT AUTO_INCREMENT,
  level INT NOT NULL,
  required_experience INT NOT NULL,
  power INT NOT NULL,
  health INT NOT NULL,
  PRIMARY KEY (id)
);

DELETE FROM levels;

INSERT INTO levels (level, required_experience, power, health) VALUES
(1, 0, 10, 100),
(2, 2, 20, 150),
(3, 4, 30, 200),
(4, 8, 40, 250),
(5, 16, 50, 300),
(6, 32, 60, 350),
(7, 64, 70, 400),
(8, 128, 80, 450),
(9, 256, 90, 500),
(10, 512, 100, 550),
(11, 1024, 110, 600),
(12, 2048, 120, 650),
(13, 4096, 130, 700),
(14, 5192, 140, 750),
(15, 6384, 150, 800),
(16, 12768, 160, 850),
(17, 15536, 170, 900),
(18, 31072, 180, 950),
(19, 62144, 190, 1000),
(20, 124288, 200, 1050),
(21, 148576, 210, 1080),
(22, 197152, 220, 1110),
(23, 294304, 230, 1140),
(24, 388608, 240, 1170),
(25, 477216, 250, 1200),
(26, 554432, 255, 1225),
(27, 708864, 260, 1250),
(28, 1017728, 265, 1275),
(29, 1435456, 270, 1300),
(30, 136870912, 275, 1325);

DROP TABLE IF EXISTS enemies;

CREATE TABLE enemies (
  id INT AUTO_INCREMENT,
  name VARCHAR(64) NOT NULL,
  level INT NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

DELETE FROM enemies;

INSERT INTO enemies (name, level) VALUES
('Goblin', 1),
('Skeleton', 2),
('Orc', 3),
('Spider', 4),
('Dragon', 5),
('Zombie', 6),
('Slime', 7),
('Witch', 8),
('Troll', 9),
('Ghost', 10),
('Vampire', 11),
('Werewolf', 12),
('Mummy', 13),
('Harpy', 14),
('Cyclops', 15),
('Banshee', 16),
('Minotaur', 17),
('Succubus', 18),
('Yeti', 19),
('Gorgon', 20),
('Chimera', 21),
('Basilisk', 22),
('Kraken', 23),
('Phoenix', 24),
('Siren', 25),
('Cerberus', 26),
('Griffin', 27),
('Hydra', 28),
('Medusa', 29),
('Behemoth', 30);
