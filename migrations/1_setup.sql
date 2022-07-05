DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id serial PRIMARY KEY,
  name varchar(50) NOT NULL,
  score int NOT NULL
);
