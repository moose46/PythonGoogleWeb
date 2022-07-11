import logging
import csv
from collections import namedtuple

import csv
import string
from collections import namedtuple
from pathlib import Path

import psycopg2

from dev.config import config
from files import file_path

file_path = Path.cwd()

if not file_path.exists():
    file_path = Path.cwd() / 'data'


def execute_sql_files(file_name: str='bets.sql', logger: logging=None):
    try:
        with open(file_path / file_name, 'r') as file:
            sql = file.read()
            exec_sql(sql)
    except FileExistsError as e:
        logging.error(f'execute_sql_files() -> {file_name} {e}')



def exec_sql(command: str):
    conn = None

    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f'exec_sql({command}): {error}')
    finally:
        if conn is not None:
            conn.close()

if "__main__" == __name__:
    execute_sql_files()
