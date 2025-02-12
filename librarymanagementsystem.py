import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
def create_db():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          title TEXT,
                          author TEXT,
                          year INTEGER,
                          isbn TEXT)''')
        conn.commit()
def add_book(title, author, year, isbn):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)',
                       (title, author, year, isbn))
        conn.commit()
def edit_book(book_id, title, author, year, isbn):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?',
                       (title, author, year, isbn, book_id))
        conn.commit()
def delete_book(book_id):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()
def get_all_books():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        return cursor.fetchall()
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        create_db()
        self.create_main_frame()
    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)
        tk.Button(self.main_frame, text="Add Book", command=self.add_book).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self.main_frame, text="Edit Book", command=self.edit_book).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.main_frame, text="Delete Book", command=self.delete_book).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(self.main_frame, text="View Books", command=self.view_books).grid(row=0, column=3, padx=5, pady=5)
    def add_book(self):
        title = simpledialog.askstring("Input", "Enter the book title:")
        author = simpledialog.askstring("Input", "Enter the author:")
        year = simpledialog.askinteger("Input", "Enter the publication year:")
        isbn = simpledialog.askstring("Input", "Enter the ISBN:")
        if title and author and year and isbn:
            add_book(title, author, year, isbn)
            messagebox.showinfo("Success", "Book added successfully!")
    def edit_book(self):
        book_id = simpledialog.askinteger("Input", "Enter the book ID to edit:")
        title = simpledialog.askstring("Input", "Enter the new book title:")
        author = simpledialog.askstring("Input", "Enter the new author:")
        year = simpledialog.askinteger("Input", "Enter the new publication year:")
        isbn = simpledialog.askstring("Input", "Enter the new ISBN:")
        if book_id and title and author and year and isbn:
            edit_book(book_id, title, author, year, isbn)
            messagebox.showinfo("Success", "Book edited successfully!")
    def delete_book(self):
        book_id = simpledialog.askinteger("Input", "Enter the book ID to delete:")
        if book_id:
            delete_book(book_id)
            messagebox.showinfo("Success", "Book deleted successfully!")
    def view_books(self):
        books = get_all_books()
        if not books:
            messagebox.showinfo("No Books", "No books in the library.")
            return
        book_list = "\n".join([f"ID: {b[0]}, Title: {b[1]}, Author: {b[2]}, Year: {b[3]}, ISBN: {b[4]}" for b in books])
        messagebox.showinfo("Books", book_list)
root = tk.Tk()
app = LibraryApp(root)
root.mainloop()
