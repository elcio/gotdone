#!/usr/bin/env python

import mysql.connector
import configparser
import os

conf=configparser.ConfigParser()
conf.read(os.path.expanduser('~/.gotdone.auth'))

db = mysql.connector.connect(
    host=conf['client']['host'],
    user=conf['client']['user'],
    passwd=conf['client']['password'],
    db=conf['client']['database']
)

def query(q):
    cur = db.cursor()
    cur.execute(q)
    if q.lower().startswith('select'):
        return cur.fetchall()
    else:
        db.commit()
        return True

