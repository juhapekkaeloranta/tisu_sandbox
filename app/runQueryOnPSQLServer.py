#!/usr/bin/env python

"""
This script runs a sql query on pqsl server

@param: dbinfo (String) = database info for connecting, see psycopg2 manual
@param: sqlQueryString (String) = single sql query 
@return: result (list) = 
    success: [1, returning value from query]
    failure: [0, error]
"""

#import module for db connection
import psycopg2

def executeQuery(dbinfo, sqlQueryString):
    dbinfo = "dbname=juhapekm user=juhapekm"
    
    # Establish connection to database
    conn = psycopg2.connect(dbinfo)
    # Create cursor for db
    cur = conn.cursor()
    
    # Query the database and obtain data as Python objects
    #cur.execute("SELECT * FROM tisu.users;")
    #cur.execute("INSERT INTO tisu.pumpdata VALUES ('pump3', '2015-01-17 23:00:00', '662');")
    try:
        cur.execute(sqlQueryString)
        result = ['1', cur.fetchall()]
    except psycopg2.Error, e:
        result = ['0', e]
    #print(cur.fetchall())
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()
    return result

