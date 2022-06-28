import psycopg2

with psycopg2.connect(host='localhost', database='suppliers', user='postgres', password='as34df67jk90') as conn:
        # create a cursor
        cur = conn.cursor()
        
	    # execute a statement
        print('PostgreSQL database version: ', end='')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()