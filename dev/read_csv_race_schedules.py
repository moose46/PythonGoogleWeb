__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
#
# Author: Robert W. Curtiss
# read_csv_race_schedules.py was created on June 15 2022 @ 6:21 PM
# Project: PythonGoogleWeb
#
import csv
import string
from collections import namedtuple
from pathlib import Path

from files import file_path

file_path = Path.cwd() / '..' / 'data'

if not file_path.exists():
    file_path = Path.cwd() / 'data'


def read_race_data_files(file_name='2022_schedule.txt'):
    data = list()
    try:
        with open(file_path / file_name, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            # csv file must have header
            rawResult = namedtuple('race', next(reader), rename=True)
            for row in reader:
                if len(row) > 0:
                    race = rawResult(*row)
                    data.append(race)

    except FileExistsError as e:
        print(e)

    return data


if __name__ == '__main__':
    races = read_race_data_files()

    for s in races:
        print(f'{s.RACE_DATE:9} {string.capwords(s.TRACK):32}')
