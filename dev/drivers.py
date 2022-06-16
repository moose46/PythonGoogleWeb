__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

#
# Author: Robert W. Curtiss
# drivers.py was created on June 15 2022 @ 10:46 AM
# Project: PythonGoogleWeb
#

import psycopg2
conn: psycopg2.connection

def connect():
    """
        docker-compose.yml
        volumes:
          data:

        services:
          postgres:
            image: postgres:latest
            environment:
              - POSTGRES_PASSWORD=postgrespw
            ports:
              - 5432:5432
            volumes:
              - data:/var/lib/postgresql
          myapp:
            image: [5b21e2e86aab]
    """
    print(f'Connecting ...')
    global conn
    try:
        conn = psycopg2.connect("dbname=racing user=bob password=admin host=red-barn port=49154")
        print(f'Database {conn.dsn} opened.')
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(f'db version = {db_version}')

    except (psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print(f'Database {conn.dsn} connection closed.')
            conn.close()


def create_tables():
    """Create tables in the PostgresSQL database"""
    command = ("""
               DROP TABLE IF EXISTS public.drivers;
                
                CREATE TABLE IF NOT EXISTS public.drivers
                (
                    id integer NOT NULL DEFAULT nextval('drivers_id_seq'::regclass),
                    name character(32) COLLATE pg_catalog."default" NOT NULL,
                    CONSTRAINT drivers_pkey PRIMARY KEY (id)
                )
                
                TABLESPACE pg_default;
                
                ALTER TABLE IF EXISTS public.drivers
                    OWNER to postgres;
    """)


if __name__ == '__main__':
    conn = connect()
    create_tables()
