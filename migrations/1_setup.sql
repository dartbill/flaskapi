DROP TABLE IF EXISTS cats;

CREATE TABLE cats (
  id serial PRIMARY KEY,
  name varchar(50) NOT NULL,
  age int NOT NULL
);
