-- Table: public.tracks

DROP TABLE IF EXISTS public.tracks CASCADE;

CREATE TABLE IF NOT EXISTS public.tracks
(
    track_id SERIAL PRIMARY KEY,
    track_name character varying COLLATE pg_catalog."default" NOT NULL,
    owner_name character varying COLLATE pg_catalog."default" NOT NULL,
    miles numeric NOT NULL,
    config character varying COLLATE pg_catalog."default" NOT NULL,
    city character varying COLLATE pg_catalog."default" NOT NULL,
    state character varying COLLATE pg_catalog."default" NOT NULL,
    date_created date NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_updated date NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_name character varying COLLATE pg_catalog."default" NOT NULL DEFAULT 'bob'::character varying,
    CONSTRAINT uk_track_name UNIQUE (track_name,config)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tracks
    OWNER to postgres;

COMMENT ON TABLE public.tracks
    IS 'All tracks';