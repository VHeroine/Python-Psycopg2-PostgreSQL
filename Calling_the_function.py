#!/usr/bin/python
import psycopg2
from config import config


def get_parts(vendor_id):
    """Getting parts provided by a vendor specified by the vendor_id."""
    conn = None
    try:
        # Reading database configuration.
        params = config()
        # Connecting to the PostgreSQL database.
        conn = psycopg2.connect(**params)
        # Creating a cursor object for execution
        cur = conn.cursor()
        # Calling the function.
        cur.callproc('get_parts_by_vendor', (vendor_id,))
        # Processing the result set.
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        # Closing the cursor.
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    param = input("Enter the provider ID: ")
    get_parts(param)