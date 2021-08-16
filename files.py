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
log_file = Path.home() / "beerme" /'files_log.txt'
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
        self.individual_bets['05-16-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Martin Truex Jr.'}
        self.individual_bets['05-23-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson'}
        self.individual_bets['05-30-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Chase Elliott'}
        self.individual_bets['06-06-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson'}
        self.individual_bets['06-20-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Larson'}
        self.individual_bets['06-27-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Busch'}
        self.individual_bets['07-04-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'William Byron'}
        self.individual_bets['07-11-2021'] = {'Greg': 'Ryan Blaney', 'Bob': 'Kyle Busch'}
        self.individual_bets['08-08-2021'] = {'Greg': 'Chase Elliott', 'Bob': 'Ryan Blaney'}
        self.individual_bets['08-15-2021'] = {'Greg': 'Kyle Larson', 'Bob': 'William Byron'}
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
                    race_date = re.findall(r'\d+-\d+-\d+', f.name)[0]  # get the date from the file name
                    if strptime(race_date, DATE_FORMAT) > strptime('01-01-2021', DATE_FORMAT):
                        # loop through the bets and check for a driver in the results, if found add to the results list
                        for name in self.individual_bets[race_date]:
                            # the key [race_date][name] returns the driver name
                            if self.individual_bets[race_date][name] == result.DRIVER:
                                parts = race_track.split(" ")  # look to see if the filename has spaces in it
                                capitalized_parts = [p.capitalize() for p in parts]  # cap first letter(s) of name

                                self.race_schedule_results.append(  # add it to the results list
                                    {'race_date': race_date, 'race_track': " ".join([word.capitalize() for word in race_track.split(" ")]), 'driver_name': result.DRIVER,
                                     'finish': int(result.POS),
                                     'player_name': name, 'beers': 0, 'team_bet': False, 'car_number': result.CAR})
                            # logging.info(result)
                    # if the race is in 2021
                    if strptime(race_date, DATE_FORMAT) > strptime('03-14-2021', DATE_FORMAT):
                        for name in self.team_bet:  # checking to see if this driver is in the team bets
                            if result.DRIVER in self.team_bet[name]:  # if found, add it to the results list also
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
