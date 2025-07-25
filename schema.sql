DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    gender TEXT CHECK (gender IN ('Maschio', 'Femmina')) NOT NULL,
    phone TEXT,
    birthdate DATE NOT NULL,
    terms_accepted BOOLEAN NOT NULL CHECK (terms_accepted IN (0, 1)),
    privacy_accepted BOOLEAN NOT NULL CHECK (privacy_accepted IN (0, 1))
);
