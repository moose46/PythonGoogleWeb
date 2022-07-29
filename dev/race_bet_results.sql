select race.track,race.race_date, b.driver_name,r.finish_pos,b.player_name from bets b, results r, races race
where  r.race_id = b.race_id and race.race_id = b.race_id
  and race.track like 'Dover%'
  and r.driver_name = b.driver_name
group by race.race_date,race.track,b.driver_name,b.player_name, r.finish_pos,b.race_id

order by race.race_date, r.finish_pos