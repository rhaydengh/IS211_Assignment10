#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Query Pets database for people and their pets"""

import sqlite3 as lite
import sys

con = lite.connect('pets.db')

with con:
    cur = con.cursor()
    petsquery = raw_input("Please enter the person's ID number: ")
    cur.execute("SELECT * FROM person WHERE id =?", [(petsquery)])
    data = cur.fetchone()

while True:
    petsquery = raw_input("Please enter the person's ID number: ")

    for data in con.execute(
        "SELECT * FROM person_pet WHERE person_id =?", [(petsquery)]):

        if data == None:
            print "Error, no person with that id"
            continue
        elif petsquery == '-1':
            sys.exit()

        for name in con.execute("SELECT * FROM person WHERE id =?", [(petsquery)]):
            personinfo = (name['first_name'] + ' ' + name['last_name'] + ',' + name['age'] + 'years old')

        for petinfo in con.execute("SELECT * FROM pet WHERE id =?", [(data['pet_id'])]):

            print (personinfo + ' owns a ' + petinfo['breed'] + 'named' + petinfo['name'] + 'who is' +
                   str(petinfo['age']) + ' years old.')

 
    if con:
        con.close()

