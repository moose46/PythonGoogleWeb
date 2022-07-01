-- PROCEDURE: public.load_bets(date, character varying, character varying)

DROP PROCEDURE IF EXISTS public.load_bets(date, character varying, character varying);

create or replace procedure load_bets(
    prace_date date,
    pplayer_name varchar(32),
    pdriver_name varchar(32)
    )
language plpgsql
as $$
declare
_race_id integer;
begin
    RAISE NOTICE 'Driver=%', pplayer_name;
    select race_id into _race_id from races where race_date = prace_date;
    insert into bets (race_id, player_name, driver_name)
        VALUES(_race_id, pdriver_name, pplayer_name);
    RAISE NOTICE 'RACE_ID=%', _race_id;
end;$$
