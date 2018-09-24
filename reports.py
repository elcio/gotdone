#!/usr/bin/env python

import sys
import db

dates=False
if len(sys.argv)>2:
    dates=sys.argv[1:3]

where="category IS NOT NULL"

if dates:
    where+=" AND (`when` BETWEEN '%s' AND '%s')" % tuple(dates)

logs = db.query(
    'SELECT COUNT(id) as spent,category FROM log WHERE %s GROUP BY category ORDER BY spent DESC' % where
)

for l in logs:
    print l[0],l[1]


