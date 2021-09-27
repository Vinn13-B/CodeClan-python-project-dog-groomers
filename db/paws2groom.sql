-- creating sql db for dog groomer business with required tables

DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS groomers;
DROP TABLE IF EXISTS dogs;

CREATE TABLE dogs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    breed VARCHAR(255),
    age INT,
    owner_first_name VARCHAR(255),
    owner_last_name VARCHAR(255),
    owner_contact_number VARCHAR(255)
);

CREATE TABLE groomers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    date VARCHAR(255),
    time VARCHAR(255),
    dog_id INT REFERENCES dogs(id) ON DELETE CASCADE,
    groomer_id INT REFERENCES groomers(id)
);