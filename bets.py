__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'
# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# bets.py was created on March 31 2021 @ 6:37 PM
# Project: PythonGoogleWeb

__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'

import operator
from collections import defaultdict
from datetime import datetime
# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# race.py was created on April 02 2021 @ 2:04 PM
# Project: nascar
from pathlib import Path

nascar_dir = Path.cwd() / "data"

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


class RaceFan:

    def __init__(self, fan_name):
        self.fan_name = fan_name
        self.total_beers = 0

    def __repr__(self):
        return self.fan_name


class Entry(RaceFan):

    def __init__(self, fan_name, finish=0, driver_name=""):
        RaceFan.__init__(self, fan_name)
        self.driver_name = driver_name
        self.finish = finish
        self.beer = False

    def __repr__(self):
        return f'Entry:{self.fan_name} {self.race_name} {self.driver_name} {self.finish} {self.beer}'


def clean_data(text, track):
    """Remove all tabs file the .txt file and create a list for each line"""
    txt = text.split('\n')
    clean_list = []

    race_date = datetime.today().date()
    cnt = 0
    for d in txt:
        driver_results = d.split('\t')
        if cnt == 0:
            keys = driver_results
            keys.append('DATE')
            keys.append('TRACK')
            cnt += 1
        else:
            driver_results.append(race_date)
            driver_results.append(track)
            clean_list.append(driver_results)

        clean_dict = dict(zip(driver_results, keys))
    return clean_list


race_schedule_results = {}
for f in file_path.glob("results*.txt"):
    # print(f.stem.split('_')[1], end=' - ')  # print track name
    race_track = f.stem.split('_')[1]
    with f.open('r', encoding="utf-8") as file:
        text = file.read()
        results_date = f.name.split('_')
        data = clean_data(text, results_date[1])
        # print(results_date[2])  # print race date
        race_schedule_results[str(results_date[2])] = {'race_track': race_track, 'results': data}

sorted_results = {}
sorted_tuples = sorted(race_schedule_results.items(), key=operator.itemgetter(0))
sorted_dict = {k: v for k, v in sorted_tuples}

bets = defaultdict(list)
bets.setdefault('missing_key')

bets['02-14-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Brad Keselowski'}  # daytona 500
bets['02-21-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Chase Elliott'}  # daytona road
bets['02-28-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Denny Hamlin'}  # miami
bets['03-07-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.'}  # las vagas
bets['03-14-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Chase Elliott'}  # phoenix
bets['03-21-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.'}  # atlanta
bets['03-28-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson'}  # bristol dirt
bets['04-10-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Denny Hamlin'}  # martinsville

team_bet = defaultdict(list)
team_bet.setdefault('missing_key')

team_bet['Greg'] = ["Ryan Blaney", "Joey Logano", "Brad Keselowski"]
team_bet['Bob'] = ["Martin Truex Jr.", "Denny Hamlin", "Kyle Bush"]

bets_data = defaultdict(list)
for race_date in sorted_dict:
    pos = 0
    for race_driver in sorted_dict[race_date]["results"]:
        finish, driver, *_, race_name = sorted_dict[race_date]["results"][pos]
        pos += 1
        if bets.get(race_date):
            # if bets[race_date]['Greg'] == driver:
            #     print(f'Greg - {driver} {finish}')
            # elif bets[race_date]['Bob'] == driver:
            #     print(f'Bob - {driver} {finish}')
            for name in bets[race_date]:
                if bets[race_date][name] == driver:
                    entry = defaultdict()
                    entry = {name: {'driver': driver, 'finish': int(finish)}}
                    bets_data[race_name].append(entry)
