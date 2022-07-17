#!/usr/bin/python
import psycopg2
from config import config
import os


SQL = "insert into part_drawings(part_id, file_extension, drawing_data) values(%s, %s, %s)"

def write_blob(part_id: int, path_to_file: str, file_extension: str):
    """Inserting a blob into the drawings table."""
    conn = None
    try:
        # Reading data from a picture.
        with open(path_to_file, 'rb') as f:
            drawing = f.read()
            # Reading a database configuration.
            params = config()
            # Connecting to the PostgresQL database.
            conn = psycopg2.connect(**params)
            # Creating a new cursor object.
            cur = conn.cursor()
            # Executing the insert statement.
            cur.execute(SQL, (part_id, file_extension, psycopg2.Binary(drawing)))
            # Committing the changes to the database.
            conn.commit()
            # Closing the cursor.
            cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    write_blob(1, os.path.abspath(os.path.join(os.getcwd(), os.pardir, "Pictures/0001.jpg")), "jpg")
    write_blob(2, os.path.abspath(os.path.join(os.getcwd(), os.pardir, "Pictures/0002.jpg")), "jpg")