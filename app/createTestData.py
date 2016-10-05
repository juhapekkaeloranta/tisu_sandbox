#!/usr/bin/env python

"""
This script connects to db and executes queries
"""

import runQueryOnPSQLServer as connection
import generateMockPumpData as mockdata

def main():
	listOfQueries = getQueries()
	databaseInfo = "dbname=juhapekm user=juhapekm"
	executeQueries(databaseInfo, listOfQueries)

def getQueries():
	startdate = "2015/03/01 00:00:00"
	noOfDays = 30
	return mockdata.create_sql_rows(startdate, noOfDays)

def executeQueries(databaseInfo, listOfQueries):
	for row in listOfQueries:
	    print('row:')
	    print(row)
	    print('connecting...')
	    print(connection.executeQuery(databaseInfo, row))
	    print('closed')

main()