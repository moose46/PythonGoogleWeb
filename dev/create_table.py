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

list_of_commands = ['races.sql','bets.sql','results.sql','procedure.sql']

commands = (
)
from config import config



def load_schedule_data(data: list):
    conn = None

    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for row in data:
            command = f"""INSERT INTO public.races(race_date,track,race_name)
            VALUES('{row.RACE_DATE}','{string.capwords(row.TRACK)}','{string.capwords(row.RACE_NAME)}')
            """
            cur.execute(command)
        # close communication with the PostgreSQL database server
        command = f"""call list_races('4/17/2022','Ricky Rudd',2,2,'Chevrolet');"""
        cur.execute(command)
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    for c in list_of_commands:
        execute_sql.execute_sql_files(c)
    data = read_csv_race_schedules.read_race_data_files()
    load_schedule_data(data)

