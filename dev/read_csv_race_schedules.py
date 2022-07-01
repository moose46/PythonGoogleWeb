__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
#
# Author: Robert W. Curtiss
# read_csv_race_schedules.py was created on June 15 2022 @ 6:21 PM
# Project: PythonGoogleWeb
#
import csv
import logging
import string
from collections import namedtuple
from pathlib import Path

from files import file_path

file_path = Path.cwd() / '..' / 'data'

if not file_path.exists():
    file_path = Path.cwd() / 'data'


def read_race_data_files(file_name='2022_schedule.txt', delimiter=','):
    data = list()
    try:
        with open(file_path / file_name, 'r') as file:
            reader = csv.reader(file, delimiter=delimiter)
            # csv file must have header
            rawResult = namedtuple('race', next(reader), rename=True)
            for row in reader:
                if len(row) > 0:
                    try:
                        race = rawResult(*row)
                    except Exception as e:
                        logging.error(f'{e} {row}')
                        continue
                    data.append(race)

    except FileExistsError as e:
        print(e)
        return None

    return data


if __name__ == '__main__':
    races = read_race_data_files()
    bets = read_race_data_files("bets.txt")
    for s in races:
        print(f'{s.RACE_DATE:9} {string.capwords(s.TRACK):32}')
