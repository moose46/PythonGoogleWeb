DROP TABLE if EXISTS public.races CASCADE;
CREATE TABLE IF NOT EXISTS public.races
(
    RACE_ID           SERIAL PRIMARY KEY,
    RACE_DATE    date        NOT NULL,
    TRACK        varchar(64) NOT NULL,
    TRACK_ID integer NULL,
    RACE_NAME    varchar(64) NOT NULL,
    DATE_CREATED date        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    DATE_UPDATED date        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    USER_NAME    varchar(32) NOT NULL default 'Bob',
    CONSTRAINT uk_races UNIQUE (RACE_DATE, TRACK, RACE_NAME)
);
-- ALTER TABLE IF EXISTS public.races DROP CONSTRAINT IF EXISTS uk_races;
--
-- ALTER TABLE IF EXISTS public.races
--     ADD CONSTRAINT uk_races UNIQUE (race_date, track, race_name);
