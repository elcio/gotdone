#!/usr/bin/env python

import db
import re
import sys

if '--reset' in sys.argv:
    db.query('UPDATE log SET category=NULL')

cats=db.query('SELECT * FROM categories ORDER BY priority,id')
logs=db.query('SELECT * FROM log WHERE category IS NULL')

for log in logs:
    match=False
    for cat in cats:
        r='.*%s.*' % cat[1]
        if re.match(r,log[1]):
            db.query("UPDATE log SET category='%s' WHERE id=%d" % (cat[2],log[0]))
            match=True
            break
    if not match:
        print log


