__author__ = 'David'

import sys
from dateutil.parser import parse
import json


def car_uses_diesel(data):
	return int(data["hoofdbrandstof"] == "Diesel")


def car_uses_diesel_db(data):
	return int(data == 1)


def car_is_from_before_2001(data):
	return int(parse(str(data["datumeersteafgiftenederland"])).year < 2001)


def car_is_from_before_2001_db(data):
	return int(data == 1)


def allow_car_access(car_data):
	"""
	May the car access the garage?
	:param car_data: utf-8 json data
	:return: False als de auto op diesel rijd en ouder is dan 2001
	"""
	if isinstance(car_data, str):
		# run this if the json file is used
		obj = json.loads(car_data)
		if car_uses_diesel(obj) and car_is_from_before_2001(obj):
			return False
		return True
	elif isinstance(car_data, tuple):
		# run this if the db is used
		if car_uses_diesel_db(car_data[2]) and car_is_from_before_2001_db(car_data[3]):
			return False
		return True
