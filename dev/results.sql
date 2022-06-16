DROP TABLE IF EXISTS public.results;
CREATE TABLE IF NOT EXISTS public.results
       (
           ID SERIAL PRIMARY KEY,
           RACE_ID integer NOT NULL,
           DRIVER varchar(64)NOT NULL,
           START_POS integer NOT NULL,
           FINISH_POS integer NOT NULL,
           MANUFACTURER varchar(64)NOT NULL,
           DATE_CREATED date NOT NULL DEFAULT CURRENT_TIMESTAMP,
           DATE_UPDATED date NOT NULL DEFAULT CURRENT_TIMESTAMP,
           USER_NAME varchar(32) NOT NULL default 'Bob',
           CONSTRAINT uk_race_date_track_driver UNIQUE (RACE_ID, DRIVER),
           CONSTRAINT uk_race_finish UNIQUE (RACE_ID,FINISH_POS),
           CONSTRAINT uk_race_start UNIQUE (RACE_ID, START_POS),
           FOREIGN KEY (RACE_ID)
           REFERENCES races (id)
           ON UPDATE CASCADE ON DELETE CASCADE
       )
       TABLESPACE pg_default;

