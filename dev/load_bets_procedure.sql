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
_id integer;
begin
    RAISE NOTICE 'Driver=%', pplayer_name;
    select id into _id from races where race_date = prace_date;
    insert into bets (race_id, player_name, driver_name)
        VALUES(_id, pdriver_name, pplayer_name);
    RAISE NOTICE 'ID=%', _id;
end;$$
