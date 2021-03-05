#!/usr/bin/python

import sys
import sqlite3

db = sqlite3.connect("dugnad.db")
db.row_factory = sqlite3.Row

c = db.cursor()
c.execute("SELECT * FROM waterbody")
for row in c.fetchall():
  print(row['name'].lower())
  query = "UPDATE waterbody SET search = ? WHERE id = ?"
  search = row['name'].lower()
  c.execute(query, [search, row['id']])
  db.commit()

