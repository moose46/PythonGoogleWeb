__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'

# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# bets.py was created on April 15 2021 @ 3:01 PM
# Project: nascar
from collections import defaultdict
from datetime import datetime
from itertools import groupby
from operator import itemgetter
from pathlib import Path
from time import strptime

from beerbet import BeerBet
from entry import Entry

DATE_FORMAT = '%m-%d-%Y'
nascar_dir = Path.home() / "beerme" / "data"
if not nascar_dir.exists():
    nascar_dir = Path.home() / "PycharmProjects" / "Python-Google-Web" / "data"

file_path = nascar_dir  # / "bristol_dirt.txt"
file_path_csv = nascar_dir / "bristol_dirt.csv"


def process_race_row(row):
    row['POS'] = int(row['POS'])
    row['CAR'] = int(row['CAR'])
    row['LAPS'] = int(row['LAPS'])
    row['START'] = int(row['START'])
    row['LED'] = int(row['LED'])
    row['PTS'] = int(row['PTS'])
    row['BONUS'] = int(row['BONUS'])
    row['PENALTY'] = int(row['PENALTY'])
    row['RACE'] = 'Bristol Dirt'


def clean_data(text, track):
    """Remove all tabs file the .txt file and create a list for each line"""
    txt = text.split('\n')
    clean_list = []

    race_date = datetime.today().date().strftime("%m-%d-%Y")
    cnt = 0
    for d in txt:
        driver_results = d.split('\t')
        if cnt == 0:
            keys = driver_results
            keys.append('DATE')
            keys.append('TRACK')
            cnt += 1
        else:
            driver_results.append(strptime(race_date, '%m-%d-%Y'))
            driver_results.append(track)
            clean_list.append(driver_results)

        clean_dict = dict(zip(driver_results, keys))
    return clean_list


race_schedule_results = {}
bets = defaultdict(list)
bets.setdefault('missing_key')

bets['02-14-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Brad Keselowski'}
bets['02-21-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Chase Elliott'}
bets['02-28-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Denny Hamlin'}
bets['03-07-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.'}
bets['03-14-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Chase Elliott'}
bets['03-21-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.'}
bets['03-28-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson'}
bets['04-10-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Denny Hamlin'}
bets['04-18-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.'}

team_bet = defaultdict(list)
# team_bet.setdefault('missing_key')

team_bet['Greg'] = ["Ryan Blaney", "Joey Logano", "Brad Keselowski"]
team_bet['Bob'] = ["Martin Truex Jr.", "Denny Hamlin", "Kyle Busch"]

race_schedule_results = []
bets_team = []
for f in file_path.glob("results*.txt"):
    results_date = f.name.split('_')

    race_date = results_date[2]
    month, day, year = race_date.split('-')
    # print(f.stem.split('_')[1], end=' - ')  # print track name
    race_track = f.stem.split('_')[1]
    with f.open('r', encoding="utf-8") as file:
        text = file.read()
        results_date = f.name.split('_')
        data = clean_data(text, results_date[1])
        print(f'{f.name}')
        # print(results_date[2])  # print race date
        for d in data:
            finish, driver, *_, race_name = d
            race_date = results_date[2]
            if strptime(race_date, DATE_FORMAT) > strptime('01-01-2021', DATE_FORMAT):
                sql_race_date = year + '-' + month + '-' + day
                # individual bet
                for name in bets[race_date]:
                    if bets[race_date][name] == driver:
                        race_schedule_results.append(
                            {'race_date': race_date, 'race_track': race_track.capitalize(), 'driver_name': d[1],
                             'finish': int(finish),
                             'fan_name': name, 'beers': 0, 'team_bet': False})
            if strptime(race_date, DATE_FORMAT) > strptime('03-14-2021', DATE_FORMAT):
                for name in team_bet:
                    if driver in team_bet[name]:
                        # print(f' {name} - {race_name}, {driver} - {finish}')
                        # bets_team[race_date].append((race_name, name, driver, finish))
                        race_schedule_results.append(
                            {'race_date': race_date, 'race_track': race_track.capitalize(), 'driver_name': driver,
                             'finish': int(finish),
                             'fan_name': name, 'beers': 0, 'team_bet': True})

results = sorted(race_schedule_results, key=itemgetter('race_date', 'team_bet', 'fan_name'))

bets = []
team_bets = []
for date, items in groupby(results, key=itemgetter('race_date')):
    print(date)
    bob = None
    greg = None
    for i in items:
        if not i['team_bet']:
            if i['fan_name'] == 'Bob':
                bob = i
            else:
                greg = i
            if bob and greg:
                if bob['finish'] < greg['finish']:
                    if bob['finish'] == 1:
                        bob['beers'] = 2
                    else:
                        bob['beers'] = 1
                else:
                    if greg['finish'] == 1:
                        greg['beers'] = 2
                    else:
                        greg['beers'] = 1
                bets.append(BeerBet(race_name=bob['race_track'],
                                             greg=Entry(driver_name=greg['driver_name'],
                                                        finish=greg['finish'],
                                                        fan_name=greg['fan_name'],
                                                        beers=greg["beers"]),
                                             bob=Entry(driver_name=bob['driver_name'],
                                                       finish=bob['finish'],
                                                       fan_name=bob['fan_name'],
                                                       beers=bob["beers"])))
                # final_results.append(greg)
                bob = None
                greg = None
        else:
            team_bets.append(i)

final_team = []
total_bob = 0
total_greg = 0

for date, items in groupby(team_bets, key=itemgetter('race_date')):
    # print(date)
    bob = 0
    greg = 0
    penske = 0
    gibbs = 0
    for i in items:
        # print('     ', i)
        if i['fan_name'] == 'Bob':
            bob += i['finish']
            gibbs = bob
        else:
            greg += i['finish']
            penske = greg
    if greg < bob:
        total_greg += 1
        greg = 1
        bob = 0
    else:
        total_bob += 1
        bob = 1
        greg = 0
    final_team.append({'race_name': i['race_track'], 'Greg': greg, 'Bob': bob, 'Penske' : penske, 'Gibbs' : gibbs})


if total_bob > total_greg:
    total_bob = total_bob - total_greg
    total_greg -= total_bob
    if total_greg < 0:
        total_greg = 0
    if total_bob < 0:
        total_bob = 0
else:
    total_greg = total_greg - total_bob
    total_bob -= total_greg
    if total_bob < 0:
        total_bob = 0
    if total_greg < 0:
        total_greg = 0

team_cooler = {'Bob': total_bob, 'Greg': total_greg}
