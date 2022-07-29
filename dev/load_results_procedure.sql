DROP PROCEDURE IF EXISTS load_results;
create or replace procedure load_results(
    prace_date date,
    pdriver_name varchar(32),
    pstart_pos int,
    pfinish_pos int,
    pmanufacturer varchar(64))
language plpgsql
as $$
declare
_race_id integer;
_track_id integer;
begin
    RAISE NOTICE 'Driver=%', pdriver_name;
    select race_id into _race_id from races where race_date = prace_date;
    select t.track_id into _track_id from races r, tracks t where r.race_id = _race_id and t.track_name = r.track;
    insert into results (race_id, track_id, driver_name, start_pos, finish_pos, manufacturer)
        VALUES(_race_id,_track_id, pdriver_name,pstart_pos, pfinish_pos, pmanufacturer);
    RAISE NOTICE 'RACE_ID=%', _race_id;
end;$$



