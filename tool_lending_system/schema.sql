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
        'admin', 'active'),
        ('jorge', 'jorge@email.com', 'scrypt:32768:8:1$iCCzRVEakBq89YDo$cbce04983c1562a33d5d66a672607aa710dd2012429cce51fe783b152c050dbed79bd16f704d708c66dc1fc7f8fd9df133122c49e79d52cc8b493a0f5148be0b',
        'normal', 'active');

CREATE TABLE tool (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  description TEXT NOT NULL,
  code TEXT NOT NULL UNIQUE,
  available INTEGER NOT NULL,
  location TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO tool (description, code, available, location) VALUES ('Alicate de corte grande', 'FER-1', 1, 'Armário 1');
INSERT INTO tool (description, code, available, location) VALUES ('Chave de fenda Phillips', 'FER-2', 1, 'Armário 1');
INSERT INTO tool (description, code, available, location) VALUES ('Martelo de carpinteiro', 'FER-3', 1, 'Armário 1');
INSERT INTO tool (description, code, available, location) VALUES ('Trena de 5 metros', 'FER-4', 1, 'Armário 1');
INSERT INTO tool (description, code, available, location) VALUES ('Chave inglesa ajustável', 'FER-5', 1, 'Armário 1');
INSERT INTO tool (description, code, available, location) VALUES ('Alicate de bico meia-cana', 'FER-6', 1, 'Armário 2');
INSERT INTO tool (description, code, available, location) VALUES ('Chave de boca 10mm', 'FER-7', 1, 'Armário 2');
INSERT INTO tool (description, code, available, location) VALUES ('Serra de mão', 'FER-8', 1, 'Armário 2');
INSERT INTO tool (description, code, available, location) VALUES ('Nível a laser', 'FER-9', 1, 'Armário 2');
INSERT INTO tool (description, code, available, location) VALUES ('Chave de fenda de precisão', 'FER-10', 1, 'Armário 2');
INSERT INTO tool (description, code, available, location) VALUES ('Alicate de pressão', 'FER-11', 1, 'Armário 3');
INSERT INTO tool (description, code, available, location) VALUES ('Tesoura de corte', 'FER-12', 1, 'Armário 3');
INSERT INTO tool (description, code, available, location) VALUES ('Furadeira elétrica', 'FER-13', 1, 'Armário 3');
INSERT INTO tool (description, code, available, location) VALUES ('Lixa de grão fino', 'FER-14', 1, 'Armário 3');
INSERT INTO tool (description, code, available, location) VALUES ('Chave de fenda de ponta chata', 'FER-15', 1, 'Armário 3');
INSERT INTO tool (description, code, available, location) VALUES ('Alicate de corte diagonal', 'FER-16', 1, 'Armário 4');
INSERT INTO tool (description, code, available, location) VALUES ('Chave de boca 13mm', 'FER-17', 1, 'Armário 4');
INSERT INTO tool (description, code, available, location) VALUES ('Serra tico-tico', 'FER-18', 1, 'Armário 4');
INSERT INTO tool (description, code, available, location) VALUES ('Trena de 3 metros', 'FER-19', 1, 'Armário 4');
INSERT INTO tool (description, code, available, location) VALUES ('Chave hexagonal', 'FER-20', 1, 'Armário 4');
INSERT INTO tool (description, code, available, location) VALUES ('Alicate de ponta fina', 'FER-21', 1, 'Armário 5');
INSERT INTO tool (description, code, available, location) VALUES ('Chave de boca 17mm', 'FER-22', 1, 'Armário 5');
INSERT INTO tool (description, code, available, location) VALUES ('Plaina manual', 'FER-23', 1, 'Armário 5');
INSERT INTO tool (description, code, available, location) VALUES ('Lápis de carpinteiro', 'FER-24', 1, 'Armário 5');
INSERT INTO tool (description, code, available, location) VALUES ('Chave de fenda de ponta Phillips', 'FER-25', 1, 'Armário 5');
INSERT INTO tool (description, code, available, location) VALUES ('Alicate de crimpar', 'FER-26', 1, 'Armário 1');
INSERT INTO tool (description, code, available, location) VALUES ('Chave ajustável para tubos', 'FER-27', 1, 'Armário 1');
INSERT INTO tool (description, code, available, location) VALUES ('Serra circular', 'FER-28', 1, 'Armário 1');
INSERT INTO tool (description, code, available, location) VALUES ('Nível de bolha', 'FER-29', 1, 'Armário 1');
INSERT INTO tool (description, code, available, location) VALUES ('Fita isolante', 'FER-30', 1, 'Armário 1');


CREATE TABLE loan (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tool_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  loan_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  devolution_date TIMESTAMP,
  user_id_checked_out INTEGER,
  returned INTEGER NOT NULL,
  requester_name TEXT NOT NULL,
  requester_area TEXT NOT NULL,
  obs TEXT,
  FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (user_id_checked_out) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (tool_id) REFERENCES tool (id) ON DELETE CASCADE ON UPDATE CASCADE
);

