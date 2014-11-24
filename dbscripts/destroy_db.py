#!/usr/bin/python

import psycopg2
import sys

# This script is responsible for dropping the Dmoz table.
try:
    conn = psycopg2.connect("dbname='scrapeDB' user='testuser' host='localhost' password='test'")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Dmoz;")
    conn.commit()

except  psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
        print 'Error %s' % e    
    sys.exit(1)

finally:
    if conn:
        conn.close()
