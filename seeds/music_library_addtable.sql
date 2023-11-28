-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS sponsor;
DROP SEQUENCE IF EXISTS sponsor_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS sponsor_id_seq;
CREATE TABLE sponsor (
    id SERIAL PRIMARY KEY,
    company VARCHAR(255),
    sector VARCHAR(255),
    artist_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO sponsor (company, sector, artist_id) VALUES ('FanClub', 'football', 1);
INSERT INTO sponsor (company, sector, artist_id) VALUES ('CarFast', 'motors', 2);
INSERT INTO sponsor (company, sector, artist_id) VALUES ('Betfred', 'football', 3);
INSERT INTO sponsor (company, sector, artist_id) VALUES ('Allcheap', 'retails', 4);



