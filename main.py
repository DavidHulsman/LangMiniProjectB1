__author__ = 'David'

from tkinter import Tk, StringVar, FALSE, Label, Frame, RIDGE, NW, NE, N, W, Button, Canvas

# mijn bestanden
import encryptie
import tesseract
import database
import entree_check
from PIL import ImageTk, Image

APP_NAME = "Garagetoeganggever"
APP_WIDTH = 1024
APP_HEIGHT = 400


class MyLabel(Label):
	"""
	Dit zijn de labels aan de linkerkant van de app. Elke keer dat ik er 1 maak, word die onder de laatst gemaakte label geplaatst.
	Deze objecten worden _alleen_ in de linkerkant van de app geplaatst. Als je ergens anders een label wilt plaatsen, zal je een aparte class moeten maken.
	"""

	def __init__(self, frame, strvalue = ""):
		"""
		:param frame: Het frame waar de label in geplaatst word
		:param strvalue: De tekst die de label op het scherm print
		"""
		self.stringvar = StringVar(value = strvalue)
		super().__init__(frame, textvariable = self.stringvar)

		global positie
		self.grid(row = positie, column = 1, sticky = W)

		positie += 1

	def set_stringvar(self, string):
		self.stringvar.set(string)

	def get_stringvar(self):
		return self.stringvar

	def get_string(self):
		return self.stringvar.get()


def ask_for_file():
	"""
	Vraag de gebruiker om het te analyseren bestand/plaatje en analyseer het bestand en laad de informatie zien op het scherm.
	Deze functie doet dus eigenlijk meer dan de naam aangeeft.
	"""
	filename = askopenfilename(filetypes = [("JPEG", '*.jpg'),
											('All', '*')])
	global lbl_selected_file
	global right_frame
	lbl_selected_file.set_stringvar(filename)

	canvas = Canvas(right_frame, width = 512, height = 512)
	canvas.grid(row = 0, column = 1)
	imgfile = Image.open(filename)
	size = 512, 512
	imgfile.thumbnail(size, Image.ANTIALIAS)
	img = ImageTk.PhotoImage(imgfile)
	canvas.create_image(1, 1, image = img, anchor = NW)
	# assigned the gif1 to the canvas object
	# canvas.scale(xscale = 10, yscale = 10)
	canvas.gif1 = img

	kenteken = tesseract.retrieve_license_plate_from_img(filename)
	if kenteken == None:
		lbl_selected_file.set_stringvar("Kan bestand niet analyseren! Maak een nieuwe foto en probeer het opnieuw!")
	else:
		if database.check_db(kenteken):
			data = database.load_kenteken_from_db(kenteken)
			print(type(data))
			print("data", (data))
			# TODO: labels opvullen
			lbl_retrieved_kenteken.set_stringvar(data[1])
			if data[2] == 1:
				lbl_retrieved_diesel.set_stringvar("ja")
			else:
				lbl_retrieved_diesel.set_stringvar("nee")
			if data[3] == 1:
				lbl_retrieved_bouwjaar.set_stringvar("ja")
			else:
				lbl_retrieved_bouwjaar.set_stringvar("nee")
			if entree_check.allow_car_access(data):
				lbl_retrieved_entree.set_stringvar("ja")
			else:
				lbl_retrieved_entree.set_stringvar("nee")
			# dev_save_json_kenteken_data(data)


from tkinter.filedialog import askopenfilename

window = Tk(baseName = APP_NAME)
window.wm_title(APP_NAME)
window.resizable(width = FALSE, height = FALSE)

window.minsize(width = APP_WIDTH, height = APP_HEIGHT)
window.maxsize(width = APP_WIDTH, height = APP_HEIGHT)

main_frame = Frame(window, padx = 15, pady = 15)
main_frame.grid()

left_frame = Frame(main_frame, width = 200)
left_frame.pack_propagate(0)
left_frame.grid(row = 0, column = 0, sticky = NW)

right_frame = Frame(main_frame, relief = RIDGE)
right_frame.grid(row = 0, column = 1, sticky = NE)

positie = 1

btn_bestand = Button(left_frame, command = ask_for_file, width = 20,
					 text = "Selecteer Bestand")
btn_bestand.grid(row = positie, column = 1, sticky = W)
positie += 1

lbl_selected_file = MyLabel(left_frame)
lbl_kenteken = MyLabel(left_frame, "Kenteken:")
lbl_retrieved_kenteken = MyLabel(left_frame)
lbl_diesel = MyLabel(left_frame, "Diesel:")
lbl_retrieved_diesel = MyLabel(left_frame)
lbl_bouwjaar = MyLabel(left_frame, "Bouwjaar voor 2001:")
lbl_retrieved_bouwjaar = MyLabel(left_frame)

lbl_entree = MyLabel(left_frame, "Mag u er in:")
lbl_retrieved_entree = MyLabel(left_frame)

btn_quit = Button(left_frame, width = 20,
				  command = window.destroy,
				  text = "Quit")
btn_quit.grid(row = positie, pady = 20, column = 1, sticky = W)
positie += 1

window.mainloop()
