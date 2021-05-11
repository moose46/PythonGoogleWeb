import logging
import re
from collections import defaultdict
from datetime import datetime
from operator import itemgetter
from pathlib import Path
from time import strptime

DATE_FORMAT = '%m-%d-%Y'
nascar_dir = Path.home() / "beerme" / "data"
if not nascar_dir.exists():
    nascar_dir = Path.home() / "PycharmProjects" / "PythonGoogleWeb" / "data"
else:
    nascar_dir = Path.home() / "PycharmProjects" / "Python-Google-Web" / "data"

file_path = nascar_dir  # / "bristol_dirt.txt"
file_path_csv = nascar_dir / "bristol_dirt.csv"

logging.basicConfig(filename='files_log.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')


class ProcessDataFiles:
    def __init__(self):
        self.race_schedule_results = []
        self.bets_team = []
        self.individual_bets = defaultdict(list)
        self.individual_bets.setdefault('missing_key')
        self.individual_bets['02-14-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Brad Keselowski'}
        self.individual_bets['02-21-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Chase Elliott'}
        self.individual_bets['02-28-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Denny Hamlin'}
        self.individual_bets['03-07-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.'}
        self.individual_bets['03-14-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Chase Elliott'}
        self.individual_bets['03-21-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.'}
        self.individual_bets['03-28-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson'}
        self.individual_bets['04-10-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Denny Hamlin'}
        self.individual_bets['04-18-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.'}
        self.individual_bets['04-25-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Denny Hamlin'}
        self.individual_bets['05-02-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Brad Keselowski'}
        self.individual_bets['05-09-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson'}
        self.team_bet = defaultdict(list)

        self.team_bet['Greg'] = ["Ryan Blaney", "Joey Logano", "Brad Keselowski"]
        self.team_bet['Bob'] = ["Martin Truex Jr.", "Denny Hamlin", "Kyle Busch"]

    @staticmethod
    def process_race_row(self, row):
        row['POS'] = int(row['POS'])
        row['CAR'] = int(row['CAR'])
        row['LAPS'] = int(row['LAPS'])
        row['START'] = int(row['START'])
        row['LED'] = int(row['LED'])
        row['PTS'] = int(row['PTS'])
        row['BONUS'] = int(row['BONUS'])
        row['PENALTY'] = int(row['PENALTY'])
        row['RACE'] = 'Bristol Dirt'

    @staticmethod
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
                keys.append('CAR_NUMBER')
                cnt += 1
            else:
                driver_results.append(strptime(race_date, '%m-%d-%Y'))
                driver_results.append(track)
                clean_list.append(driver_results)

            clean_dict = dict(zip(driver_results, keys))
        return clean_list

    def read_data_files(self):
        for f in file_path.glob("results*.txt"):
            results_date = f.name.split('_')

            race_date = results_date[2]
            month, day, year = race_date.split('-')
            # print(f.stem.split('_')[1], end=' - ')  # print track name
            race_track = f.stem.split('_')[1]
            with f.open('r', encoding="utf-8") as file:
                text = file.read()
                results_date = f.name.split('_')
                race_date = re.findall(r'\d+-\d+-\d+', f.name)[0]  # returns a list
                data = self.clean_data(text, race_track)
                print(f'{f.name} - {race_date}')
                logging.info(msg=f'{f.name} - {race_date}')
                # print(results_date[2])  # print race date
                for d in data:
                    finish, driver, car_number, *_, race_name = d
                    # race_date = results_date[2]
                    if strptime(race_date, DATE_FORMAT) > strptime('01-01-2021', DATE_FORMAT):
                        sql_race_date = year + '-' + month + '-' + day
                        # check for a driver in the results, if found add to the results list
                        for name in self.individual_bets[race_date]:
                            if self.individual_bets[race_date][name] == driver:
                                self.race_schedule_results.append(
                                    {'race_date': race_date, 'race_track': race_track.capitalize(), 'driver_name': d[1],
                                     'finish': int(finish),
                                     'player_name': name, 'beers': 0, 'team_bet': False, 'car_number': car_number})
                    if strptime(race_date, DATE_FORMAT) > strptime('03-14-2021', DATE_FORMAT):
                        for name in self.team_bet:
                            if driver in self.team_bet[name]:
                                # print(f' {name} - {race_name}, {driver} - {finish}')
                                # bets_team[race_date].append((race_name, name, driver, finish))
                                self.race_schedule_results.append(
                                    {'race_date': race_date, 'race_track': race_track.capitalize(),
                                     'driver_name': driver,
                                     'finish': int(finish),
                                     'player_name': name, 'beers': 0, 'team_bet': True})

        """
            Only data in the list is either a team bet or individual bet
            , separated by team_bet, either true or false
           sort the list by race_date, team_bet and player name (greg or bob) 
        """
        sorted_race_results = sorted(self.race_schedule_results, key=itemgetter('race_date', 'team_bet', 'player_name'))
        for b in sorted_race_results:
            logging.info(b)
        return sorted_race_results


p = ProcessDataFiles()
#
race_results_data = p.read_data_files()

pass
