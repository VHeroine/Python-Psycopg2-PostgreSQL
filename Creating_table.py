#!/usr/bin/python

import psycopg2
from config import config

def create_tables():
    """ Creating tables in the PostgreSQL database. """
    commands = (
        """create table vendors(
            vendor_id serial primary key,
            vendor_name varchar(255) not null)
        """,
        """create table parts(
                part_id serial primary key,
                part_name varchar(255) not null)
        """,
        """create table part_drawings(
                part_id integer primary key,
                file_extension varchar(5) not null,
                drawing_data bytea not null,
                foreign key (part_id)
                references parts (part_id)
                on update cascade
                on delete cascade)
        """,
        """create table vendor_parts(
                vendor_id integer not null,
                part_id integer not null,
                primary key (vendor_id , part_id),
                foreign key (vendor_id)
                references vendors (vendor_id)
                on update cascade
                on delete cascade,
                foreign key (part_id)
                references parts (part_id)
                on update cascade
                on delete cascade)
        """,)
    conn = None
    try:
        # Reading the connection parameters.
        params = config()
        # Connecting to the PostgreSQL server.
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Creating table one by one.
        for command in commands:
            cur.execute(command)
        # Closing communication with the PostgreSQL database server.
        cur.close()
        # Committing the changes.
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()