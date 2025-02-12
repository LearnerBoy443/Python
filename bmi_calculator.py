import tkinter as tk
from tkinter import messagebox
import csv

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("300x250")
        self.weight_label = tk.Label(root, text="Weight (kg):")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()
        self.height_label = tk.Label(root, text="Height (m):")
        self.height_label.pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()
        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        self.storage_button = tk.Button(root, text="View Historical Data", command=self.view_historical_data)
        self.storage_button.pack()
        self.visualization_button = tk.Button(root, text="Visualize BMI Trend", command=self.visualize_bmi_trend)
        self.visualization_button.pack()
    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            if weight < 30 or weight > 300:
                raise ValueError("Invalid weight range")
            if height < 1.2 or height > 2.2:
                raise ValueError("Invalid height range")
            bmi = weight / (height ** 2)
            category = self.categorize_bmi(bmi)
            self.result_label.config(text=f"BMI: {bmi:.2f} ({category})")
            self.store_data(weight, height, bmi, category)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def categorize_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    def store_data(self, weight, height, bmi, category):
        with open("bmi_data.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([weight, height, bmi, category])
    def view_historical_data(self):
        try:
            with open("bmi_data.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
                messagebox.showinfo("Historical Data", "\n".join([",".join(row) for row in data]))
        except FileNotFoundError:
            messagebox.showerror("Error", "No historical data found")
    def visualize_bmi_trend(self):
        messagebox.showinfo("Coming Soon", "BMI trend visualization will be implemented soon!")
root = tk.Tk()
bmi_calculator = BMICalculator(root)
root.mainloop()