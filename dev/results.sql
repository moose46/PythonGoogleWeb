DROP TABLE IF EXISTS public.results CASCADE;
CREATE TABLE IF NOT EXISTS public.results
       (
           ID SERIAL PRIMARY KEY,
           RACE_ID integer NOT NULL,
           TRACK_ID integer NULL,
           DRIVER_NAME varchar(64)NOT NULL,
           START_POS integer NOT NULL,
           FINISH_POS integer NOT NULL,
           MANUFACTURER varchar(64)NOT NULL,
           DATE_CREATED date NOT NULL DEFAULT CURRENT_TIMESTAMP,
           DATE_UPDATED date NOT NULL DEFAULT CURRENT_TIMESTAMP,
           USER_NAME varchar(32) NOT NULL default 'Bob',
           CONSTRAINT uk_race_driver_start_finish UNIQUE (RACE_ID,DRIVER_NAME,START_POS,FINISH_POS),
           FOREIGN KEY (RACE_ID)
           REFERENCES races (race_id)
           ON UPDATE CASCADE ON DELETE CASCADE
       )
       TABLESPACE pg_default;

