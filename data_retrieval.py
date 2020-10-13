__author__ = 'David'

import sys
import requests
import json

KENTEKEN_DATA_FILE = "kenteken.json"


def retrieve_car_data_online(kenteken):
	"""
	:param kenteken: Nederlands kenteken
	:return: string in de vorm van een standaard kenteken
	"""
	auth_details = ("DavidHulsmanNL@gmail.com", "2d178a0f29e3019212606961939ec8759b0baec42da7084663adcf6dc3e3e996")
	url = "".join(["https://overheid.io/api/voertuiggegevens/" + kenteken +
				   "/?ovio-api-key=2d178a0f29e3019212606961939ec8759b0baec42da7084663adcf6dc3e3e996"])
	# url = "".join(["https://overheid.io/api/voertuiggegevens/60-HT-RR/?ovio-api-key=2d178a0f29e3019212606961939ec8759b0baec42da7084663adcf6dc3e3e996"])
	response = requests.get(url, auth = auth_details)  # retrieve data
	print(response.text)
	return response._content.decode('utf-8')


def dev_save_json_kenteken_data(data):
	"""
	GEBRUIK ALLEEN TIJDENS DEVELOPMENT;
	Laad de data van een tijdelijk .json bestand. Dit maakt het programma sneller
	Als tijdelijke vervanging van retrieve_car_data_online()
	:param data:
	"""
	f = open(KENTEKEN_DATA_FILE, "w")
	obj = json.loads(data)
	f.write(json.dumps(obj, indent = 4))
	f.close()


def dev_load_json_kenteken_data():
	"""
	GEBRUIK ALLEEN TIJDENS DEVELOPMENT;
	Laad de data van een tijdelijk .json bestand. Dit maakt het programma sneller
	Als tijdelijke vervanging van retrieve_car_data_online()
	:return: kenteken JSON data
	"""

	f = open(KENTEKEN_DATA_FILE)
	data = f.read()
	return data
