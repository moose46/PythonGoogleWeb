-- Table: public.bets

DROP TABLE IF EXISTS public.bets;

CREATE TABLE IF NOT EXISTS public.bets
(
    bet_id SERIAL PRIMARY KEY,
    player_name character varying COLLATE pg_catalog."default" NOT NULL,
    driver_name character varying COLLATE pg_catalog."default" NOT NULL,
    date_created date NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_updated date NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_name character varying COLLATE pg_catalog."default" NOT NULL DEFAULT 'Bob'::character varying,
    race_id integer NOT NULL,
    CONSTRAINT uk_driver_race_id UNIQUE (race_id, driver_name, player_name),
    CONSTRAINT fk_race FOREIGN KEY (race_id)
        REFERENCES public.races (race_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.bets
    OWNER to postgres;
-- Index: fki_fk_race

-- DROP INDEX IF EXISTS public.fki_fk_race;

CREATE INDEX IF NOT EXISTS fki_fk_race
    ON public.bets USING btree
    (race_id ASC NULLS LAST)
    TABLESPACE pg_default;