import tkinter as tk
from src.password import Password


class App:
    def __init__(self, window):
        self.window = window
        window.title("Password Generator")
        window.geometry("450x150")
        window.resizable(0, 0)
        window.columnconfigure(0, weight=2)
        window.columnconfigure(1, weight=1)
        window.columnconfigure(1, weight=1)
        self.lbl_pass_len = tk.Label(master=window, text="Password Length:", fg="blue")
        self.values = [i for i in range(6, 19)]
        self.val = self.values[::-1]
        self.var = tk.StringVar(master=window)
        self.var.set(self.val[-1])
        self.length = tk.Spinbox(
            master=window,
            values=self.values,
            textvariable=self.var,
            width=5,
            relief=tk.RAISED,
            command=self.pass_strength,
            fg="blue",
        )
        self.lbl_strength = tk.Label(
            master=window, text="Password Strength:", fg="blue"
        )
        self.strength = tk.Label(master=window, text="Low", fg="red")
        self.button_generate = tk.Button(
            master=window, text="Generate", fg="blue", command=self.generate_pass
        )
        self.button_copy = tk.Button(
            master=window, text="Copy", fg="blue", command=self.copy
        )
        self.entry_generate = tk.Entry(master=window, relief=tk.RAISED, fg="blue")
        self.entry_generate.focus()
        self.lbl_pass_len.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.length.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.lbl_strength.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.strength.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.button_generate.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.entry_generate.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        self.button_copy.grid(row=2, column=2, sticky="w", padx=5, pady=5)

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

    def pass_strength(self):
        """Define password strength to be low/medium/high"""
        if int(self.var.get()) < 8:
            self.strength.config(text="Low", fg="red")
        elif int(self.var.get()) < 13:
            self.strength.config(text="Medium", fg="orange")
        else:
            self.strength.config(text="High", fg="green")
