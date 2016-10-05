#!/usr/bin/env python

"""
This script generates mockdata psql insert statements
"""

from datetime import datetime, timedelta
import random

#Random numbers for variation in data
def randomVariation():
    return random.randint(10, 150) #(min, max)

#Basevalues for hourly amount of water pumped
def createBaseValues():
    return [300, 300, 200, 200, 300, 400, 500, 700, 900, 700, 500, 500, 600, 600, 400, 400, 500, 600, 700, 600, 700, 900, 600, 400]

#Create psql insert statements
def create_sql_rows(beginDateTime, numberOfDays):
    datestamp = datetime.strptime(beginDateTime, "%Y/%m/%d %H:%M:%S")
    insert_prefix = "INSERT INTO tisu.pumpdata VALUES ('"
    insert_suffix = "') RETURNING 'Success';"
    c = "', '"
    pumpid = "pump3"
    basevalues = createBaseValues()

    listOfQueries = []

    for day in range(numberOfDays):
        for hour in range(24):
            datestamp = datestamp + timedelta(hours=1)
            value = basevalues[hour] + randomVariation()
            #print(insert_prefix + pumpid + c + str(datestamp) + c + str(value) + insert_suffix)
            listOfQueries.append(insert_prefix + pumpid + c + str(datestamp) + c + str(value) + insert_suffix)

    return listOfQueries

