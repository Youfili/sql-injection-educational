DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    UNIQUE(username)
);

INSERT INTO Users (username, password, email) VALUES
    ('alice', '1234', 'alice@email.com'),
    ('bob', 'qwerty', 'bob@email.com'),
    ('charlie', 'admin', 'charlie@email.com');
