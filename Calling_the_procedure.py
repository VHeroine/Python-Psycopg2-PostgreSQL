#!/usr/bin/python
import psycopg2
from config import config


def add_part(part_name: str, vendor_name: str) -> None:
    """Creating some new data by calling the procedure."""
    conn = None
    try:
        # Reading database configuration.
        params = config()
        # Connecting to the PostgreSQL database.
        conn = psycopg2.connect(**params)
        # Creating a cursor object for execution.
        cur = conn.cursor()
        # Calling a stored procedure.
        cur.execute('call add_new_part(%s, %s)', (part_name, vendor_name))
        # Committing the transaction.
        conn.commit()
        # Closing the cursor.
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    part_name = input("Enter a part name: ")
    vendor_name = input('Enter a vendor name: ')
    add_part(part_name, vendor_name)