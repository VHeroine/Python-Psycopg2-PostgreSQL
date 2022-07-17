#!/usr/bin/python
import psycopg2
from config import config


def connect() -> None:
    """ Connecting to the PostgreSQL database server. """
    conn = None
    try:
        # Reading connection parameters.
        params = config()
        # Connecting to the PostgreSQL server.
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        # Creating a cursor.
        cur = conn.cursor() 
    	# Executing a statement.
        print('PostgreSQL database version: ', end='')
        cur.execute('select version()')
        # Displaying the PostgreSQL database server version.
        db_version = cur.fetchone()
        print(db_version)
        # Closing the cursor.
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()