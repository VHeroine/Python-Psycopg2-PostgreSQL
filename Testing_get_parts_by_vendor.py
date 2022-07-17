#!/usr/bin/python
import psycopg2
from config import config


def get_parts(vendor_id):
    """ Getting parts provided by a vendor specified by the vendor_id. """
    conn = None
    try:
        # Reading the connection parameters.
        params = config()
        # Connecting to the PostgreSQL database.
        conn = psycopg2.connect(**params)
        # Creating a cursor object for execution.
        cur = conn.cursor()
        # Calling a function.
        cur.callproc('get_parts_by_vendor', (vendor_id,))
        # Processing the result set.
        row = cur.fetchone()
        while row is not None:
            print(f'ID = {row[0]}, part name = {row[1]}')
            row = cur.fetchone()
        # Closing the cursor.
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_parts(1)