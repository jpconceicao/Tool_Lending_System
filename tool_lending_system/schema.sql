DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS tool;
DROP TABLE IF EXISTS loan;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  status TEXT NOT NULL,
  level TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO user (name, email, password, level, status)
VALUES ('admin', 'admin@email.com', 'scrypt:32768:8:1$iCCzRVEakBq89YDo$cbce04983c1562a33d5d66a672607aa710dd2012429cce51fe783b152c050dbed79bd16f704d708c66dc1fc7f8fd9df133122c49e79d52cc8b493a0f5148be0b',
        'admin', 'ativo'
       );

CREATE TABLE tool (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  description TEXT NOT NULL,
  code TEXT NOT NULL,
  available INTEGER NOT NULL,
  location TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE loan (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tool_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  loan_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  devolution_date TIMESTAMP,
  returned INTEGER NOT NULL,
  requester_name TEXT NOT NULL,
  requester_area TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (tool_id) REFERENCES tool (id) ON DELETE CASCADE ON UPDATE CASCADE
);

