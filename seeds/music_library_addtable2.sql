-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- Finally, we add any records that are needed for the tests to run
INSERT INTO sponsor (company, sector, artist_id) VALUES ('Nothing', 'football', 4);



