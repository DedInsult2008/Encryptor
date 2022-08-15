import random as r 
from tkinter import *
from tkinter import ttk 
def encrypting():
	if combobox.get() == 'One way':
		list_of_rands = []
		int_list = []
		for i in text.get('1.0', END+'-1c'):
			list_of_rands.append(bin(r.randint(10, 99000)))
		for i in list_of_rands:
			int_list.append(int(i , base = 2))


		print(sum(int_list))

values = ['One way']

root = Tk()
root.geometry('400x600')
root['bg'] = 'gray13'
root.resizable(width = False, height = False)
root.title('Encryptor')

text_area = StringVar()

combobox = StringVar()

label_text = Label(text =('Enter text here'), bg = 'gray13', fg = 'thistle2', font = ('Bandal', 10)).place(x = 10, y = 5)

label_encryption = Label(text = ('Select the encryption type'), bg = 'gray13', fg = 'thistle2', font = ('Bandal', 10)).place(x = 10, y = 190)

text = Text(width = 47, height = 9)
text.place(x = 10, y = 30)

encryption = ttk.Combobox(root, values = ['One way'],textvariable = combobox, width = 12).place(x = 180, y = 190)

encrypt = Button(root, text =('Encrypt!'), bg = 'gray13', fg = 'thistle2', font = ('Bandal', 10), relief = 'flat', command = encrypting).place(x = 10, y = 220)




root.mainloop()