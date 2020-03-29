CREATE TABLE accounts(
  email VARCHAR(40) NOT NULL,
  password VARCHAR(256) NOT NULL,
  account_type VARCHAR(20) NOT NULL,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (email)
);

CREATE TABLE applicants(
  email VARCHAR(40) NOT NULL,
  profession VARCHAR(20) NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  school VARCHAR(40) NOT NULL,
  grad_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  exp_position VARCHAR(40) NOT NULL,
  exp_description VARCHAR(500) NOT NULL,
  exp_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  exp_to TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (email)
  FOREIGN KEY (email)
    REFERENCES accounts (email)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

CREATE TABLE applications(
  email VARCHAR(40) NOT NULL,
  opening_id INTEGER NOT NULL,
  status VARCHAR(20) NOT NULL,
  PRIMARY KEY (email, opening_id),
  FOREIGN KEY (email)
    REFERENCES accounts (email)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
  FOREIGN KEY (opening_id)
    REFERENCES openings (opening_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

CREATE TABLE employers(
  email VARCHAR(40) NOT NULL,
  name VARCHAR(100) NOT NULL,
  address_1 VARCHAR(40) NOT NULL,
  address_2 VARCHAR(40),
  city VARCHAR(20) NOT NULL,
  state VARCHAR(5) NOT NULL,
  zipcode VARCHAR(5) NOT NULL,
  PRIMARY KEY (email),
  FOREIGN KEY (email)
    REFERENCES accounts (email)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

CREATE TABLE openings(
  opening_id INTEGER NOT NULL,
  date_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  urgency VARCHAR(50) NOT NULL,
  title VARCHAR(20) NOT NULL,
  description VARCHAR(500) NOT NULL,
  email VARCHAR(40) NOT NULL,
  deadline TIMESTAMP NOT NULL,
  PRIMARY KEY (opening_id),
  FOREIGN KEY (email)
    REFERENCES accounts (email)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);