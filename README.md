# README #

LangMiniProjectB1 is een programma voor een virtueele parkeergarage. Het programma checked of een auto naar binnen mag of niet. Het laad een foto van een nummerplaat in, voert OCR (Optical Character Recognition) uit om de nummerplaat in tekst vorm te krijgen en checked bij de overheid of de auto van die nummerplaat van voor 2001 is en op diesel rijd. Zo ja, dan mag die auto de garage niet binnen.

### How do I get set up? ###

**I'll assume you're using PyCharm.**

Install the following  packages via File > Settings > Project: PROJECTNAME > Project Interpreter (_press the green + on the right of the window_)

	* Pillow (Python Image Library fork)
	* Pillow-PIL (Pillow wrapper for PIL compatibility)
	* PyTesseract (python wrapper for google's Tesseract-OCR)
	* Matplotlib
	* Requests
	* Xmltodict
	
Also download and install the following libs:

* `tesseract-ocr-setup-3.02.02.exe` from https://code.google.com/p/tesseract-ocr/downloads/detail?name=tesseract-ocr-setup-3.02.02.exe&can=2&q=

