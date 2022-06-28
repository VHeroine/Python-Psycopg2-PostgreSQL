#!/usr/bin/python

import psycopg2
from config import config


def test_connection() -> None:
    """ This function just tests a connection with PostgreSQL server. """
    try:
        # Reading the connection parameters.
        params = config()
        # Trying to establish a connection between Python programme and a PostgreSQL server.
        conn = psycopg2.connect(**params)
        # Creating a cursor.
        cur = conn.cursor()  
        # Executing a statement.
        print('PostgreSQL database version: ', end='')
        cur.execute('select version()')
        # Displaying the PostgreSQL database server version.
        db_version = cur.fetchone()
        print(db_version)
        # Closing the communication with the PostgreSQL.
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    test_connection()