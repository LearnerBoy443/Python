import tkinter as tk
from tkinter import messagebox
def calculate_grades():
    try:
        grades = []
        for entry in entries:
            grade = entry.get()
            if grade:
                grades.append(float(grade))        
        if not grades:
            messagebox.showerror("Error", "No grades entered.")
            return
        average = sum(grades) / len(grades)
        average_label.config(text=f"Average Grade: {average:.2f}")
        if average >= 90:
            letter_grade = 'O'
        elif average >= 80:
            letter_grade = 'E'
        elif average >= 70:
            letter_grade = 'A'
        elif average >= 60:
            letter_grade = 'B'
        elif average >= 50:
            letter_grade = 'C'
        elif average >= 40:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        letter_grade_label.config(text=f"Letter Grade: {letter_grade}")
        gpa_scale = {'O': 10, 'E': 9, 'A': 8, 'B': 7, 'C': 6, 'D': 5, 'F': 4}
        gpa = gpa_scale.get(letter_grade, 0)
        gpa_label.config(text=f"GPA: {gpa:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid grade entered. Please enter numeric values.")
root = tk.Tk()
root.title("Student Grades Tracker")
subjects = ["Mathematics", "Science", "English", "History", "Computer Science"]
tk.Label(root, text="Enter grades for each subject:").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
entries = []
for i, subject in enumerate(subjects):
    tk.Label(root, text=f"{subject}:").grid(row=i+1, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    entries.append(entry)
btn_calculate = tk.Button(root, text="Calculate", command=calculate_grades)
btn_calculate.grid(row=len(subjects)+1, column=0, columnspan=2, padx=10, pady=10)
average_label = tk.Label(root, text="Average Grade: ")
average_label.grid(row=len(subjects)+2, column=0, columnspan=2, padx=10, pady=5)
letter_grade_label = tk.Label(root, text="Letter Grade: ")
letter_grade_label.grid(row=len(subjects)+3, column=0, columnspan=2, padx=10, pady=5)
gpa_label = tk.Label(root, text="GPA: ")
gpa_label.grid(row=len(subjects)+4, column=0, columnspan=2, padx=10, pady=5)
root.mainloop()
