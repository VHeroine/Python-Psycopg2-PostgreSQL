#!/usr/bin/python
import psycopg2
from config import config


def update_vendor(vendor_id, vendor_name) -> None:
    """Updating vendor name based on the vendor id."""
    sql = """update vendors
                set vendor_name = %s
              where vendor_id = %s;"""
    conn = None
    updated_rows = 0
    try:
        # Reading database configuration.
        params = config()
        # Connecting to the PostgreSQL database.
        conn = psycopg2.connect(**params)
        # Creating a new cursor.
        cur = conn.cursor()
        # Executing the update statement.
        cur.execute(sql, (vendor_name, vendor_id))
        # Getting the number of updated rows.
        updated_rows = cur.rowcount
        # Making the changes to the database persistent.
        conn.commit()
        # Closing the cursor.
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows

if __name__ == '__main__':
    # Updating vendor id = 1
    update_vendor(1, "3M Corp.")