import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    if length < 8 or length > 32:
        messagebox.showwarning(
            "Invalid Input", "Password length must be between 8 and 32.")
        return
    character_set = ""
    if include_uppercase:
        character_set += string.ascii_uppercase
    if include_lowercase:
        character_set += string.ascii_lowercase
    if include_numbers:
        character_set += string.digits
    if include_symbols:
        character_set += string.punctuation
    if not character_set:
        messagebox.showwarning("No Options Selected",
                               "Please select at least one character type.")
        return
    password = ''.join(random.choice(character_set) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")
window = tk.Tk()
window.title("Advanced Password Generator")
tk.Label(window, text="Password Length (8-32):").grid(row=0,
                                                      column=0, padx=10, pady=10)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1)
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Uppercase Letters",
               variable=uppercase_var).grid(row=1, column=0, padx=10, pady=5)
tk.Checkbutton(window, text="Include Lowercase Letters",
               variable=lowercase_var).grid(row=1, column=1, padx=10, pady=5)
tk.Checkbutton(window, text="Include Numbers", variable=numbers_var).grid(
    row=2, column=0, padx=10, pady=5)
tk.Checkbutton(window, text="Include Symbols", variable=symbols_var).grid(
    row=2, column=1, padx=10, pady=5)
tk.Label(window, text="Generated Password:").grid(
    row=3, column=0, padx=10, pady=10)
password_entry = tk.Entry(window, width=30)
password_entry.grid(row=3, column=1)
tk.Button(window, text="Generate Password", command=generate_password).grid(
    row=4, column=0, padx=10, pady=10)
tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard).grid(
    row=4, column=1, padx=10, pady=10)
window.mainloop()
