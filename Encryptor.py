import random as r 
from tkinter import *
from tkinter import ttk
import re 
def encrypting():
	if combobox.get() == 'One way':
		list_of_rands = []
		int_list = []
		
		for i in text.get('1.0', END+'-1c'):
			int_list.append(r.randint(10, 99000))
		
		print(sum(int_list))

	if combobox.get() == 'Reverse (eng)':
		dictionari_of_letters = {'A':13300, 'a':133, 'B':14000, 'b':140, 'C':1300, 'c':13, 'D':14400, 'd':144, 'E':1900, 'e':19, 'F':3100, 'f':31, 'G':16100, 'g':161, 'H':16200, 'h':162, 'I':3600, 'i':36, 'J':4800, 'j':48, 'K':4900, 'k':49, 'L':17700, 'l':177, 'M':17900, 'm':179, 'N':17800, 'n':178, 'O':18200, 'o':182, 'P':5400, 'p':54, 'Q':5800, 'q':58, 'R':6300, 'r':63, 'S':6400, 's':64, 'T':7000, 't':70, 'U':7300, 'u':73, 'V':7800, 'v':78, 'W':9400, 'w':94, 'X':9800, 'x':98,'Y':10700, 'y':107, 'Z':11800, 'z':118}
		
		for i in text.get('1.0', END+'-1c'):
			print(str(dictionari_of_letters[i]) + '/')

	if combobox.get() == 'Encoding (eng)':
		dictionari_of_numbers = {133:'a', 140:'b', 13:'c', 144:'d', 19:'e', 31:'f', 161:'g', 162:'h', 36:'i', 48:'j', 49:'k', 177:'l', 179:'m', 178:'n', 182:'o', 54:'p', 58:'q', 63:'r', 64:'s', 70:'t', 73:'u', 78:'v', 94:'w', 98:'x', 107:'y', 118:'z',13300:'A', 14000:'B', 1300:'C', 14400:'D', 1900:'E', 3100:'F', 16100:'G', 16200:'H', 3600:'I', 4800:'J', 4900:'K', 17700:'L', 17900:'M', 17800:'N', 18200:'O', 5400:'P', 5800:'Q', 6300:'R', 6400:'S', 7000:'T', 7300:'U', 7800:'V', 9400:'W', 9800:'X', 10700:'Y', 11800:'Z'}
		list_of_numbers = []
		
		for i in re.split('/', text.get('1.0', END+'-1c')):
			list_of_numbers.append(i)
		
		list_of_numbers[-1] = 666
		list_of_numbers.remove(666)
		
		try:
			for i in list_of_numbers:
				print(dictionari_of_numbers[int(i)])
		
		except KeyError:
			print('An error occurred check the correctness of the text')
			
root = Tk()
root.geometry('400x600')
root['bg'] = 'gray13'
root.resizable(width = False, height = False)
root.title('Encryptor')

combobox = StringVar()

label_text = Label(text =('Enter text here'), bg = 'gray13', fg = 'thistle2', font = ('Bandal', 10)).place(x = 10, y = 5)

label_encryption = Label(text = ('Select the encryption type'), bg = 'gray13', fg = 'thistle2', font = ('Bandal', 10)).place(x = 10, y = 190)

text = Text(width = 47, height = 9)
text.place(x = 10, y = 30)

encryption = ttk.Combobox(root, values = ['One way', 'Encoding (eng)', 'Decoding (eng)'],textvariable = combobox, width = 12).place(x = 180, y = 190)

encrypt = Button(root, text =('Encrypt!'), bg = 'gray13', fg = 'thistle2', font = ('Bandal', 10), relief = 'flat', command = encrypting).place(x = 10, y = 220)

root.mainloop()