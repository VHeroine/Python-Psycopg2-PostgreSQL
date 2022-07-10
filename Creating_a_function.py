#!/usr/bin/python

import psycopg2
from config import config


def create_function(sql: str) -> None:
    conn = None
    try:
        # Reading database configuration.
        params = config()
        # Connecting to the PostgreSQL database.
        conn = psycopg2.connect(**params)
        # Creating a new cursor.
        cur = conn.cursor()
        # Inserting a new part.
        cur.execute(sql)
        # Making the changes to the database persistent.
        conn.commit()
        # Closing the cursor.
        cur.close()
        print('Функция успешно создана.')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # Opening the file and reading the DDL statement.
    with open('Get_parts_by_vendor.sql', 'r') as f:
        sql = f.read()
    # Calling the function executing the DDL statement.
    create_function(sql)