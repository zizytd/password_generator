#!/usr/bin/env python3
import tkinter as tk
import random
import string

#create class to use for the generate button
class Password:
	def __init__(self, length: int):
		self.length = length
	def generate(self):
		return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=self.length))
	@property
	def verification(self):
		while True:
			passw = self.generate()
			c = any( a == True for a in [i.islower() for i in passw])
			d = any( a == True for a in [i.isupper() for i in passw])
			e = any( a == True for a in [i.isdigit() for i in passw])
			f = set(passw).difference(string.ascii_letters,string.digits)
			if c == False: #check if generated password contains lowercase, if not continue
				continue
			elif d == False: #check if generated password contains uppercase, if not continue
				continue
			elif e == False:
				continue   #check if generated password contains digit, if not continue
			elif len(f) == self.length or f == set(): #check if password contains only special chars or no special char, continue.
				continue
			else:
				break
		return passw
#function for the generate button
def generate_pass():
	password = Password(int(length.get()))
	entry_generate.delete(0, "end")
	entry_generate.insert(0, password.verification)
#function to copy password to clipboard copy button
def copy():
	button_copy.clipboard_clear()
	button_copy.clipboard_append(entry_generate.get())
	button_copy.update()
#create the tkinter window
window = tk.Tk()
window.title("Password Generator")
window.columnconfigure([0, 1], minsize=60, weight=1)
window.rowconfigure(0,weight=1)
values = [i for i in range(6,15)]
valuess = values[::-1]
var = tk.StringVar(master=window)
var.set(valuess[-1])
length = tk.Spinbox(master=window,values=values,textvariable=var,width=5,relief=tk.RAISED)
button_generate = tk.Button(master=window, text="Generate",fg="red",command=generate_pass)
button_copy = tk.Button(master=window, text="Copy",fg="red",command=copy)
entry_generate = tk.Entry(master=window,relief=tk.RAISED)
entry_generate.focus()
length.grid(row=0, column=0, sticky="ew")
button_generate.grid(row=1,column=0,sticky="ew")
entry_generate.grid(row=0,column=1,sticky="ew")
button_copy.grid(row=1,column=1,sticky="ew")
window.mainloop()


