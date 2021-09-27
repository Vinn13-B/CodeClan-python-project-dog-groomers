-- creating sql db for dog groomer business with required tables

DROP TABLE IF EXISTS walks;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS groomers;
DROP TABLE IF EXISTS dogs;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_number VARCHAR(255)
);

CREATE TABLE dogs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    breed VARCHAR(255),
    age INT,
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    comments text
);

CREATE TABLE groomers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_number VARCHAR(255)
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    date VARCHAR(255),
    time VARCHAR(255),
    dog_id INT REFERENCES dogs(id) ON DELETE CASCADE,
    groomer_id INT REFERENCES groomers(id)
);

CREATE TABLE walks (
    id SERIAL PRIMARY KEY,
    date VARCHAR(255),
    time VARCHAR(255),
    capacity int,
    head_count int,
    dog_id INT REFERENCES dogs(id) ON DELETE CASCADE
);