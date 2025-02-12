import tkinter as tk
from tkinter import messagebox
import sqlite3
def create_db():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL
                )''')
    conn.commit()
    conn.close()

create_db()
def add_product(name, quantity, price):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    conn.close()
def edit_product(product_id, name, quantity, price):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("UPDATE products SET name=?, quantity=?, price=? WHERE id=?", (name, quantity, price, product_id))
    conn.commit()
    conn.close()
def delete_product(product_id):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()
def get_all_products():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return products
def get_low_stock_products(threshold):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE quantity < ?", (threshold,))
    products = c.fetchall()
    conn.close()
    return products
def authenticate(username, password):
    return username == 'admin' and password == 'password'
class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.create_login_frame()

    def create_login_frame(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        tk.Label(self.login_frame, text="Username").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if authenticate(username, password):
            self.login_frame.pack_forget()
            self.create_main_frame()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.create_product_list()
        self.create_controls()

    def create_product_list(self):
        self.product_listbox = tk.Listbox(self.main_frame, height=15, width=50)
        self.product_listbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.load_products()

    def create_controls(self):
        tk.Button(self.main_frame, text="Add Product", command=self.add_product).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.main_frame, text="Edit Product", command=self.edit_product).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.main_frame, text="Delete Product", command=self.delete_product).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(self.main_frame, text="Low Stock Report", command=self.low_stock_report).grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def load_products(self):
        self.product_listbox.delete(0, tk.END)
        for product in get_all_products():
            self.product_listbox.insert(tk.END, f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}, Price: {product[3]}")

    def add_product(self):
        self.show_product_form("Add Product", self.save_new_product)

    def edit_product(self):
        selected = self.product_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No product selected")
            return
        product = get_all_products()[selected[0]]
        self.show_product_form("Edit Product", self.save_edited_product, product)

    def delete_product(self):
        selected = self.product_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No product selected")
            return
        product_id = get_all_products()[selected[0]][0]
        delete_product(product_id)
        self.load_products()

    def low_stock_report(self):
        low_stock_products = get_low_stock_products(threshold=10)
        report = "\n".join([f"ID: {p[0]}, Name: {p[1]}, Quantity: {p[2]}" for p in low_stock_products])
        messagebox.showinfo("Low Stock Report", report)

    def show_product_form(self, title, save_command, product=None):
        self.product_form = tk.Toplevel(self.root)
        self.product_form.title(title)

        tk.Label(self.product_form, text="Name").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.product_form)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        if product:
            self.name_entry.insert(0, product[1])

        tk.Label(self.product_form, text="Quantity").grid(row=1, column=0, padx=10, pady=10)
        self.quantity_entry = tk.Entry(self.product_form)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)
        if product:
            self.quantity_entry.insert(0, product[2])

        tk.Label(self.product_form, text="Price").grid(row=2, column=0, padx=10, pady=10)
        self.price_entry = tk.Entry(self.product_form)
        self.price_entry.grid(row=2, column=1, padx=10, pady=10)
        if product:
            self.price_entry.insert(0, product[3])

        self.save_button = tk.Button(self.product_form, text="Save", command=lambda: save_command(product))
        self.save_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def save_new_product(self, _):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        if not name or not quantity or not price:
            messagebox.showerror("Error", "All fields are required")
            return
        add_product(name, int(quantity), float(price))
        self.product_form.destroy()
        self.load_products()

    def save_edited_product(self, product):
        product_id = product[0]
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        if not name or not quantity or not price:
            messagebox.showerror("Error", "All fields are required")
            return
        edit_product(product_id, name, int(quantity), float(price))
        self.product_form.destroy()
        self.load_products()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
