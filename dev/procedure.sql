      create or replace procedure list_races(
    prace_date date,
    pdriver varchar(32),
    pstart_pos int,
    pfinish_pos int,
    pmanufacturer varchar(64))
language plpgsql
as $$
declare
_id integer;
begin
    RAISE NOTICE 'Driver=%', pdriver;
    select id into _id from races where race_date = prace_date;
    insert into results (race_id, driver, start_pos, finish_pos, manufacturer)
        VALUES(_id, pdriver,pstart_pos, pfinish_pos, pmanufacturer);
    RAISE NOTICE 'ID=%', _id;
end;$$
