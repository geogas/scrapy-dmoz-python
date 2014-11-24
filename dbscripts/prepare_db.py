#!/usr/bin/python

import psycopg2
import sys

# This script creates a table in the scrapeDB database with the following credentials
try:
    conn = psycopg2.connect("dbname='scrapeDB' user='testuser' host='localhost' password='test'")
    cur = conn.cursor()

    cur.execute("CREATE TABLE Dmoz(id SERIAL PRIMARY KEY, category VARCHAR (15), title VARCHAR(150), description VARCHAR(500))")
    conn.commit()

except  psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e    
    sys.exit(1)

finally:
    if conn:
        conn.close()
