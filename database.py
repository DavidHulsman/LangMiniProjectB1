__author__ = 'David'

import datetime
import sqlite3
import sys
import json
import entree_check
import data_retrieval

DB_NAME = "kenteken_data.db"
TABLE_NAME = "kentekens"

def check_db(kenteken):
	"""
	Check de database of kenteken al aanwezig is in tabel "kentekens". Als dit niet het geval is, haal je de data uit overheid.io en sla je het op.
	:param kenteken: Tekst in de vorm van een kenteken. vb: aa-11-bb
	:return: True als kenteken aanwezig is in de db
	"""
	data = load_kenteken_from_db(kenteken)
	while data is None:
		save_kenteken_in_db(kenteken)
		data = load_kenteken_from_db(kenteken)
	return True


def save_kenteken_in_db(kenteken):
	"""
	Sla het kenteken en andere aangelinkte data op in de db
	:param kenteken:
	"""
	conn = sqlite3.connect(DB_NAME)
	cur = conn.cursor()
	cur.execute("SELECT * FROM " + TABLE_NAME)

	json_data = data_retrieval.retrieve_car_data_online(kenteken)
	data_retrieval.dev_save_json_kenteken_data(json_data)
	dict_data = json.loads(json_data)
	unix_timestamp = datetime.datetime.now().timestamp()  # yes, this returns Unix Time (that's the amount of (milli) seconds have elapsed since 1970-1-1
	cur.execute("INSERT INTO " + TABLE_NAME + " VALUES (?,?,?,?,?)",
				(None, kenteken, entree_check.car_uses_diesel(dict_data), entree_check.car_is_from_before_2001(dict_data), unix_timestamp))

	conn.commit()
	conn.close()


def load_kenteken_from_db(kenteken):
	"""
	Laad alle data dat bij kenteken hoort uit de db
	:param kenteken: Dit kennen we ondertussen wel
	:return: data is None als er niets gevonden is, anders is het een tuple uit de table kentekens
	"""
	conn = sqlite3.connect(DB_NAME)
	cur = conn.cursor()
	cur.execute("SELECT * FROM " + TABLE_NAME)

	data = None
	for item in cur:
		if item[1] == kenteken:
			# Kenteken staat in de db!
			print("\tHet kenteken uit de db is", item[1])
			# TODO: uitzoeken of dit een copy moet worden ipv een binding
			# TODO: werkt dit echt?
			conn.close()
			data = item  # !! Dit is dus GEEN kopie, ~~maar een binding!~~
			break
	return data

def dev_creer_database():
	"""
	Creer een table
	:return:
	"""
	conn = sqlite3.connect(DB_NAME)
	cur = conn.cursor()
	# cur.execute("CREATE TABLE kentekens (id INTEGER PRIMARY KEY, pin INTEGER NOT NULL, data TEXT)")
	conn.commit()
	conn.close()