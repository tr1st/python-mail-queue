#!/usr/bin/env python

import sys
import MySQLdb

def main():
	# Read message from standard in
	mail = sys.stdin.read()
	db = MySQLdb.connect("__HOST__","__USER__","__PASS__","__DATABASE__")
	cur = db.cursor() 
	cur.execute("INSERT INTO queue VALUES (null,%s)",(mail))
	cur.close()
