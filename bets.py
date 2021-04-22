__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'

# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# bets.py was created on April 15 2021 @ 3:01 PM
# Project: nascar
import operator
from collections import defaultdict
from datetime import datetime
from itertools import groupby
from operator import itemgetter
from pathlib import Path
from time import strptime

from beerbet import BeerBet
from entry import Entry
from files import ProcessDataFiles
from summary import Summary
from wager import MyWager

DATE_FORMAT = '%m-%d-%Y'
nascar_dir = Path.home() / "beerme" / "data"
if not nascar_dir.exists():
    nascar_dir = Path.home() / "PycharmProjects" / "PythonGoogleWeb" / "data"

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
"""
    read all csv / txt files for 2021
    match wagers with results both team and individual wagers
"""
p = ProcessDataFiles()
results = p.read_data_files()

bets = []
team_bets = []
wager = MyWager()
for date, items in groupby(results, key=itemgetter('race_date')):
    print(date)
    wager.reset()  # zero out one bet
    for player in items:
        # bob or greg, bet on one driver
        if not player['team_bet']:
            operator.methodcaller(player["player_name"].lower(), player)(wager)
            if wager.enabled():
                wager.brew_some_beer()
                bets.append(BeerBet(race_name=wager.bobs_bet['race_track'],
                                    greg=Entry(driver_name=wager.gregs_bet['driver_name'],
                                               finish=wager.gregs_bet['finish'],
                                               player_name=wager.gregs_bet['player_name'],
                                               beers=wager.gregs_bet["beers"]),
                                    bob=Entry(driver_name=wager.bobs_bet['driver_name'],
                                              finish=wager.bobs_bet['finish'],
                                              player_name=wager.bobs_bet['player_name'],
                                              beers=wager.bobs_bet["beers"])))
        else:
            team_bets.append(player)


total_bets_summary = wager.beers_in_the_cooler()
betting_summary = Summary(bets)
betting_summary.total_beers_owed = wager.beers_in_the_cooler()
print(total_bets_summary)
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
        if i['player_name'] == 'Bob':
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
    final_team.append({'race_name': i['race_track'], 'Greg': greg, 'Bob': bob, 'Penske': penske, 'Gibbs': gibbs})

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
