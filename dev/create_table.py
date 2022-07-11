__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

#
# Author: Robert W. Curtiss
# create_table.py was created on June 15 2022 @ 1:23 PM
# Project: PythonGoogleWeb
#

# !/usr/bin/python
from datetime import datetime
import logging
import re
import string
from collections import namedtuple
from pathlib import Path

import psycopg2
import read_csv_race_schedules
import execute_sql

# from files import file_path
file_path = Path.home() / "PycharmProjects\PythonGoogleWeb\data"
log_file = Path.home() / "PycharmProjects\PythonGoogleWeb\logs" / "create_table_log.txt"
log_file = r"C:\Users\me\PycharmProjects\PythonGoogleWeb\logs\create_table_log.txt"
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')
# log = logging.getLogger(__name__)
# logging.getLogger().level=logging.DEBUG
# log.addHandler(logging.NullHandler())
# logging.basicConfig(filename="create_table_log.txt", level=logging.ERROR)
list_of_sql_scripts = ['races.sql',
                       'bets.sql',
                       'results.sql',
                       'load_results_procedure.sql',
                       'load_bets_procedure.sql',
                       'tracks.sql'
                       ]

commands = (
)
from config import config


class LoadData:
    def __init__(self, procedure, data: list, args=None):
        self._procedure = procedure
        self._data = data
        self.conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            self.conn = psycopg2.connect(**params)
            # self.conn = psycopg2.connect("host=red-barn dbname=racing user=bob password=admin port=49154")
            cur = self.conn.cursor()
            if args == None:
                self._procedure(data, cur)
            else:
                self._procedure(data, cur,args)

            cur.close()
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            logging.error(f'LoadData()={procedure.__name__}() / {error}')
            # print(f'LoadData()={procedure.__name__}() / {error}')
            return None
        finally:
            if self.conn is not None:
                self.conn.close()


def load_race_schedules(data: list, cur):
    """
    Passed a list of schedules and loads the race NASCAR race schedules
    :param data: list of named tuples race(race_date,Track,Race_name) of nascar race schedules
    :return:
    """
    conn = None
    logging.info(f'loading_race_schedules ...')
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        # conn = psycopg2.connect(**params)
        # cur = conn.cursor()
        command = ""
        # create table one by one
        for row in data:
            try:
                command = ""
                command = f"""INSERT INTO public.races(race_date,track,race_name)
                VALUES('{row.RACE_DATE}','{string.capwords(row.TRACK)}','{string.capwords(row.RACE_NAME)}')
                """
                # logging.info(command)
                cur.execute(command)
            except Exception as e:
                logging.CRITICAL(f'load_schedule_data: {e}')
                print(f'load_schedule_data: {e}')
                cur.close
                return None
        # close communication with the PostgreSQL database server
        # command = f"""call load_results('4/17/2022','Ricky Rudd',2,2,'Chevrolet');"""
        cur.close()
        # commit the changes
        # conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def load_track_data(data: list, cur):
    """
    Passed a list of schedules and loads the race NASCAR race schedules
    :param data: list of named tuples race(race_date,Track,Race_name) of nascar race schedules
    :return:
    """
    try:
        # read the connection parameters
        # params = config()
        # connect to the PostgreSQL server
        # conn = psycopg2.connect(**params)
        # cur = conn.cursor()
        command = ""
        # create table one by one
        logging.info("Loading Track Data ...")
        for row in data:
            try:
                command = ""
                command = f"""INSERT INTO public.tracks(track_name,owner_name, miles, config, city, state)
                                VALUES('{string.capwords(row.TRACK)}','{string.capwords(row.OWNER)}',{row.MILES},'{string.capwords(row.CONFIG)}','{string.capwords(row.CITY)}','{string.capwords(row.STATE)}');
                """
                cur.execute(command)
            except Exception as e:
                logging.error(f'load_track_data: {e}')

                print(f'load_track_data: {e}')
                cur.close
                return None
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def load_bets_data(data, cur):
    command = ""
    line_no = 1
    logging.info(f'loading bets ...')
    for d in data:
        try:
            command = ""
            command = f"call load_bets('{d.race_date}','{d.driver_name}', '{d.player_name}');"
            # logging.info(command)
            line_no += 1
            cur.execute(command)
        except Exception as e:
            logging.critical(f'Error line#: {line_no} {command} {e}')

    cur.close()

def load_race_results(data, cur,fname):
    command = ""
    line_no = 1
    month, day, year  = data[1].RACE_DATE.split('-')
    logging.info(f'loading race results ... {data[1].RACE_DATE} {fname}')
    for d in data:
        try:
            command = ""
            command = f"call load_results('{month}/{day}/{year}','{d.DRIVER}',{d.START},{d.POS},'{d.MANUFACTURER}');"
            line_no += 1
            cur.execute(command)
        except Exception as e:
            logging.error(f'Error line#: {line_no} {month}/{day}/{year} {command} {e}')
            return None
            # print(e)
            # exit(-1)

    cur.close()

if __name__ == '__main__':
    logging.info("Started ...")
    # create all tables and stored procedures first
    for c in list_of_sql_scripts:
        print(f'Creating {c}')
        logging.info(f'Creating {c}')
        execute_sql.execute_sql_files(c, logger=logging)
    # data = read_csv_race_schedules.read_race_data_files("tracks.txt")
    data = read_csv_race_schedules.read_race_data_files("2022_schedule.txt")
    x = LoadData(load_race_schedules, data)
    data = read_csv_race_schedules.read_race_data_files("bets.txt")
    x = LoadData(load_bets_data, data)
    # load all nascar tracks
    data = read_csv_race_schedules.read_race_data_files("tracks.txt")
    x = LoadData(load_track_data, data)
    for f in file_path.glob("results*.txt"):
        race_date = re.findall(r'\d+-\d+-\d+', f.name)[0]

        # read results_* race results file
        data = read_csv_race_schedules.read_race_data_files(f,delimiter='\t')
        # add race date to the data
        fields = [f for f in data[1]._fields]
        fields.append('RACE_DATE')
        try:
            # create new named tuple, with the date field added
            new_d = namedtuple("results", fields)
            new_data = []
            for d in data:
                result = new_d(*d, race_date)
                new_data.append(result)
            x = LoadData(load_race_results, new_data,f.stem)
            # todo add the race date to the results data
        except Exception as e:
            logging.critical(f'filename={f.name} {fields}{e}')
