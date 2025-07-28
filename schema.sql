-- Creo il tipo ENUM 'Gender'
CREATE TYPE Gender AS ENUM ('Maschio', 'Femmina');

-- Elimino la tabella se esiste
DROP TABLE IF EXISTS users;

-- Creo la tabella 'users'
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    gender Gender NOT NULL,
    phone VARCHAR(10) UNIQUE NOT NULL,
    birthdate DATE NOT NULL,
    terms_accepted BOOLEAN NOT NULL,
    privacy_accepted BOOLEAN NOT NULL CHECK (privacy_accepted = TRUE)
);
