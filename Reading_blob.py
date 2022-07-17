#!/usr/bin/python
import psycopg2
from config import config
import os


SQL = """select part_name,
                file_extension,
                drawing_data
           from part_drawings
           join parts
             on parts.part_id = part_drawings.part_id
          where parts.part_id = %s"""

def read_blob(part_id: int, path_to_dir: str):
    """Reading blob data from the drawings table."""
    conn = None
    try:
        # Reading a database configuration.
        params = config()
        # Connecting to the PostgresQL database.
        conn = psycopg2.connect(**params)
        # Creating a new cursor object.
        cur = conn.cursor()
        # Executing the select statement.
        cur.execute(SQL, (part_id,))
        # Writing the picture into the file.
        blob = cur.fetchone()
        with open(os.path.normpath(path_to_dir + '/' + blob[0] + '.' + blob[1]), 'wb') as f:
            f.write(blob[2])
        # Closing the cursor.
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    read_blob(1, os.getcwd())
    read_blob(2, os.getcwd())