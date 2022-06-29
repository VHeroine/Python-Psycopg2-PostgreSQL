#!/usr/bin/python

import psycopg2
from config import config


def insert_vendor(vendor_name):
    """ Inserting a new vendor into the vendors table. """
    sql = "insert into vendors(vendor_name) values(%s) returning vendor_id;"
    conn = None
    vendor_id = None
    try:
        # Reading database configuration.
        params = config()
        # Connecting to the PostgreSQL database.
        conn = psycopg2.connect(**params)
        # Creating a new cursor.
        cur = conn.cursor()
        # Executing the insert statement.
        cur.execute(sql, (vendor_name,))
        # Getting the generated id back.
        vendor_id = cur.fetchone()[0]
        # Making the changes to the database persistent.
        conn.commit()
        # Closing communication with the database.
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id

def insert_vendor_list(vendor_list):
    """ Insert multiple vendors into the vendors table. """
    sql = "insert into vendors(vendor_name) values(%s);"
    conn = None
    try:
        # Reading database configuration.
        params = config()
        # Connecting to the PostgreSQL database.
        conn = psycopg2.connect(**params)
        # Creating a new cursor
        cur = conn.cursor()
        # Executing the insert statement.
        cur.executemany(sql,vendor_list)
        # Making the changes to the database persistent.
        conn.commit()
        # Closing communication with the database.
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # Inserting one vendor.
    insert_vendor("3M Co.")
    # Inserting multiple vendors.
    insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])