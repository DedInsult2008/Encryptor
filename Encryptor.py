import random as r 
from tkinter import *
from tkinter import ttk
import re 
def encrypting():
	rus_dictionary_of_letters = {'а':130, 'А':13000, 'б':133, 'Б':13300, 'в':139, 'В':13900, 'г':12, 'Г':1200, 'д':98, 'Д':9800, 'е':11, 'Е':1100, 'ё':140, 'Ё':14000, 'ж':141, 'Ж':14100, 'з':142, 'З':14200, 'и':20, 'И':2000, 'й':23, 'Й':2300, 'к':24, 'К':2400, 'л':26, 'Л':2600, 'м':27, 'М':2700, 'н':34, 'Н':3400, 'о':163, 'О':16300, 'п':37, 'П':3700, 'р':168, 'Р':16800, 'с':48, 'С':4800, 'т':50, 'Т':5000, 'у':181, 'У':18100, 'ф':56, 'Ф':5600, 'х':57, 'Х':5700, 'ц':186, 'Ц':18600, 'ч':59, 'Ч':5900, 'ш':187, 'Ш':18700, 'щ':189, 'Щ':18900, 'ъ':75, 'Ъ':7500, 'ы':79, 'Ы':7900, 'ь':85, 'Ь':8500, 'э':89, 'Э':8900, 'ю':90, 'Ю':9000, 'я':95, 'Я':9500, ' ':1, '.':2, ',':3}
	dictionari_of_letters = {'A':13300, 'a':133, 'B':14000, 'b':140, 'C':1300, 'c':13, 'D':14400, 'd':144, 'E':1900, 'e':19, 'F':3100, 'f':31, 'G':16100, 'g':161, 'H':16200, 'h':162, 'I':3600, 'i':36, 'J':4800, 'j':48, 'K':4900, 'k':49, 'L':17700, 'l':177, 'M':17900, 'm':179, 'N':17800, 'n':178, 'O':18200, 'o':182, 'P':5400, 'p':54, 'Q':5800, 'q':58, 'R':6300, 'r':63, 'S':6400, 's':64, 'T':7000, 't':70, 'U':7300, 'u':73, 'V':7800, 'v':78, 'W':9400, 'w':94, 'X':9800, 'x':98,'Y':10700, 'y':107, 'Z':11800, 'z':118, ' ':1, '.':2, ',':3}
	if combobox.get() == 'One way':
		list_of_rands = []
		int_list = []
		
		for i in text.get('1.0', END+'-1c'):
			int_list.append(r.randint(10, 99000))
		
		print(sum(int_list))

	if combobox.get() == 'Encoding (eng)':
		
		try:
			for i in text.get('1.0', END+'-1c'):
				print(str(hex(dictionari_of_letters[i] + 10)) + '/')

		except KeyError:
			print('Unknown error!')

	if combobox.get() == 'Decoding (eng)':
		dictionari_of_numbers = dict(map(reversed, dictionari_of_letters.items()))
		list_of_numbers = []
		
		for i in re.split('/', text.get('1.0', END+'-1c')):
			list_of_numbers.append(i)
		list_of_numbers[-1] = 666
		list_of_numbers.remove(666)
		
		try:
			for i in list_of_numbers:
				print(dictionari_of_numbers[int(i ,base = 16) - 10])
		
		except KeyError:
			print('An error occurred check the correctness of the text')

	if combobox.get() == 'Encoding (rus)':
		try:
			for i in text.get('1.0', END+'-1c'):
				print(str(hex(rus_dictionary_of_letters[i] + 10)) + '/')
		except KeyError:
			print('Неизвестная ошибка!')
	if combobox.get() == 'Decoding (rus)':
		reversed_dict = dict(map(reversed, rus_dictionary_of_letters.items()))
		list_of_numbers = []

		for i in re.split('/', text.get('1.0', END+'-1c')):
			list_of_numbers.append(i)
		list_of_numbers[-1] = 666
		list_of_numbers.remove(666)
		
		try:
			for i in list_of_numbers:
				print(reversed_dict[int(i ,base = 16) - 10])
		
		except KeyError:
			print('Произошла ошибка, проверьте правильность набранного текста')
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

encryption = ttk.Combobox(root, values = ['One way', 'Encoding (eng)', 'Decoding (eng)', 'Encoding (rus)', 'Decoding (rus)'],textvariable = combobox, width = 12).place(x = 180, y = 190)

encrypt = Button(root, text =('Encrypt!'), bg = 'gray13', fg = 'thistle2', font = ('Bandal', 10), relief = 'flat', command = encrypting).place(x = 10, y = 220)

root.mainloop()