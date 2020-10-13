__author__ = 'David'

import os
import pytesseract
import Image


def retrieve_license_plate_from_img(bestandsnaam):
	"""
	Laad image bestand in, analyseer het en return het kenteken (als het gevonden is)
	:param bestandsnaam: Bestandsnaam in de norm BESTANDSNAAM.jpg/png/bmp
	:return: De tekst dat zich in het plaatje bevind, of object None of aan te geven dat het kenteken niet kan worden gevonden!

	>>> retrieve_license_plate_from_img(TEST_IMAGE)
	60-HT-RR
	"""
	try:
		img = Image.open(bestandsnaam)
		# Tesseract herkend het dash teken "-" niet correct, vandaar de .replace()
		kenteken = pytesseract.image_to_string(img).replace("'", "-")
		print("\tHet gevonden kenteken is", kenteken)
		if kenteken == "":
			return None
		else:
			return kenteken  # TesseractOCR maakt van een - de tekst —
	except FileNotFoundError as ex:
		print(ex, ":", bestandsnaam)
		print("Current path:", os.getcwd())
	except Exception as ex:
		print("Something terrible happened!")
		print(ex)
