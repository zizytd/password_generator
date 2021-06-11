import tkinter as tk
from modules.password import Password

class App:
	def __init__(self,window):
		self.window = window
		window.title("Password Generator")
		window.columnconfigure([0, 1], minsize=60, weight=1)
		window.rowconfigure(0,weight=1)
		self.values = [i for i in range(6,15)]
		self.val = self.values[::-1]
		self.var = tk.StringVar(master=window)
		self.var.set(self.val[-1])
		self.length = tk.Spinbox(master=window,values=self.values,textvariable=self.var,width=5,relief=tk.RAISED)
		self.button_generate = tk.Button(master=window, text="Generate",fg="red",command=self.generate_pass)
		self.button_copy = tk.Button(master=window, text="Copy",fg="red",command=self.copy)
		self.entry_generate = tk.Entry(master=window,relief=tk.RAISED)
		self.entry_generate.focus()
		self.length.grid(row=0, column=0, sticky="ew")
		self.button_generate.grid(row=1,column=0,sticky="ew")
		self.entry_generate.grid(row=0,column=1,sticky="ew")
		self.button_copy.grid(row=1,column=1,sticky="ew")
	def generate_pass(self):
		"""Display password on the app"""
		password = Password(int(self.length.get()))
		self.entry_generate.delete(0, "end")
		self.entry_generate.insert(0, password.verification)
	def copy(self):
		"""Copy password to clipboard"""
		self.button_copy.clipboard_clear()
		self.button_copy.clipboard_append(self.entry_generate.get())
		self.button_copy.update()