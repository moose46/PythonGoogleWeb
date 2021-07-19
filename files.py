import csv
import logging
import re
from collections import defaultdict
from collections import namedtuple
from operator import itemgetter
from pathlib import Path
from time import strptime

DATE_FORMAT = '%m-%d-%Y'
file_path = Path.home() / "beerme" / "data"
log_file = Path.home() / "beerme" / 'files_log.txt'
if not file_path.exists():
    file_path = Path.cwd() / "data"
    log_file = Path.cwd() / 'files_log.txt'

logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')
DriverBet = namedtuple('DriverBet', 'date, person_name, driver_name')


class ProcessDataFiles:
    def __init__(self):
        self.race_schedule_results = []
        self.bets_team = []
        self.individual_bets = defaultdict(list)
        self.individual_bets.setdefault('missing_key')
        self.individual_bets['02-14-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Brad Keselowski', 'Race': 'Daytona 500'}
        self.individual_bets['02-21-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Chase Elliott', 'Race': 'Daytona RC'}
        self.individual_bets['02-28-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Denny Hamlin', 'Race': 'Miami'}
        self.individual_bets['03-07-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.', 'Race': 'Las Vegas'}
        self.individual_bets['03-14-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Chase Elliott', 'Race': 'Phoenix'}
        self.individual_bets['03-21-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.', 'Race': 'Atlanta'}
        self.individual_bets['03-28-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson', 'Race' : 'Bristol (Dirt)'}
        self.individual_bets['04-10-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Denny Hamlin', 'Race': 'Martinsville'}
        self.individual_bets['04-18-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.','Race': 'Richmond'}
        self.individual_bets['04-25-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Denny Hamlin','Race': 'Talladega'}
        self.individual_bets['05-02-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Brad Keselowski','Race': 'Kansas'}
        self.individual_bets['05-09-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson', 'Race': 'Darlington'}
        self.individual_bets['05-16-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.','Race': 'Dover'}
        self.individual_bets['05-23-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson', 'Race':'Road America'}
        self.individual_bets['05-30-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Chase Elliott', 'Race': 'Charlotte'}
        self.individual_bets['06-06-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson', "Race": 'Sonoma'}
        self.individual_bets['06-20-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson', 'Race': 'Nashville'}
        self.individual_bets['06-27-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Busch', 'Race': 'Pocono 350'}
        self.individual_bets['07-04-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'William Byron', 'Race': 'Road America'}
        self.individual_bets['07-11-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Bush', 'Race': 'Atlanta'}
        self.individual_bets['07-18-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Denny Hamlin', 'Race': 'New Hampshire'}
        self.team_bet = defaultdict(list)

        self.team_bet['Greg'] = ["Ryan Blaney", "Joey Logano", "Brad Keselowski"]
        self.team_bet['Bob'] = ["Martin Truex Jr.", "Denny Hamlin", "Kyle Busch"]

    def read_data_files(self):
        for f in file_path.glob("results*.txt"):
            race_track = f.stem.split('_')[1]

            with open(Path(f'{f.parent}/{f.name}'), 'r') as file:
                reader = csv.reader(file, delimiter='\t')
                # csv file must have header
                rawResult = namedtuple("rawResult", next(reader), rename=True)
                # Result = namedtuple('Result', [*rawResult._fields, 'picked_by', 'race_date', 'race_track'])

                for row in reader:
                    result = rawResult(*row)
                    race_date = re.findall(r'\d+-\d+-\d+', f.name)[0]  # returns a list
                    if strptime(race_date, DATE_FORMAT) > strptime('01-01-2021', DATE_FORMAT):
                        # check for a driver in the results, if found add to the results list
                        for name in self.individual_bets[race_date]:
                            # the key [race_date][name] returns the driver name
                            if self.individual_bets[race_date][name] == result.DRIVER:
                                parts = race_track.split(" ")
                                capitalized_parts = [p.capitalize() for p in parts]

                                self.race_schedule_results.append(
                                    {'race_date': race_date,
                                     'race_track': " ".join([word.capitalize() for word in race_track.split(" ")]),
                                     'driver_name': result.DRIVER,
                                     'finish': int(result.POS),
                                     'player_name': name, 'beers': 0, 'team_bet': False, 'car_number': result.CAR})
                            # logging.info(result)
                    if strptime(race_date, DATE_FORMAT) > strptime('03-14-2021', DATE_FORMAT):
                        for name in self.team_bet:
                            if result.DRIVER in self.team_bet[name]:
                                parts = race_track.split(" ")
                                capitalized_parts = [p.capitalize() for p in parts]
                                self.race_schedule_results.append(
                                    {'race_date': race_date, 'race_track': " ".join(capitalized_parts),
                                     'driver_name': result.DRIVER,
                                     'finish': int(result.POS),
                                     'player_name': name, 'beers': 0, 'team_bet': True, 'car_number': result.CAR}, )
                                # logging.info(result)

        """
            Only data in the list is either a team bet or individual bet
            , separated by team_bet, either true or false
           sort the list by race_date, team_bet and player name (greg or bob) 
        """
        sorted_race_results = sorted(self.race_schedule_results, key=itemgetter('race_date', 'team_bet', 'player_name'))
        for b in sorted_race_results:
            logging.info(b)
        return sorted_race_results


if __name__ == '__main__':
    p = ProcessDataFiles()
    race_results_data = p.read_data_files()
