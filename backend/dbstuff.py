import psycopg2
from backend.config import dbconfig
 
def ownerconnect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = dbconfig()
 
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        cur.execute("SELECT * from siteowner")
 
        # display the PostgreSQL database server version
        owner = cur.fetchone()
        # print(owner)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            # close the cursor with the PostgreSQL
            cur.close()
            # close the connection with the PostgreSQL
            conn.close()
            print("The database is closed.")
    return owner 
# ownerconnect()