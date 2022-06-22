__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

#
# Author: Robert W. Curtiss
# create_table.py was created on June 15 2022 @ 1:23 PM
# Project: PythonGoogleWeb
#

# !/usr/bin/python
import string

import psycopg2
import read_csv_race_schedules
import execute_sql

list_of_sql_scripts = ['races.sql',
                       'bets.sql',
                       'results.sql',
                       'load_results_procedure.sql',
                       'load_bets_procedure.sql'
                       ]

commands = (
)
from config import config


class LoadData:
    def __init__(self, procedure, data):
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
            self._procedure(data, cur)
            cur.close()
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()


def load_schedule_data(data: list, cur):
    """
    Passed a list of schedules and loads the race NASCAR race schedules
    :param data: list of named tuples race(race_date,Track,Race_name) of nascar race schedules
    :return:
    """
    conn = None

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
                print(command)
                cur.execute(command)
            except Exception as e:
                print(e)
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


def load_bets_data(data, cur):
    command = ""
    for d in data:
        try:
            command = ""
            command = f"call load_bets('{d.race_date}','{d.player_name}', '{d.driver_name}');"
            print(command)
            cur.execute(command)
        except Exception as e:
            cur.close
            print(command)
            print(e)

    cur.close()

if __name__ == '__main__':
    # create all tables and stored procedures first
    for c in list_of_sql_scripts:
        print(f'Creating {c}')
        execute_sql.execute_sql_files(c)
    data = read_csv_race_schedules.read_race_data_files("2022_schedule.txt")
    x = LoadData(load_schedule_data, data)
    # data = read_csv_race_schedules.read_race_data_files("bets.txt")
    # x = LoadData(load_bets_data, data)
