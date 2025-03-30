from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_list = []

  pass_letter=[random.choice(letters) for _ in range (random.randint(8,10))]
  #for char in range(1, nr_letters + 1):
  #  password_list.append(random.choice(letters))

  pass_symbol = [random.choice(symbols) for _ in range(random.randint(2,4))]

  #for char in range(1, nr_symbols + 1):
  #  password_list += random.choice(symbols)

  pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
  #for char in range(1, nr_numbers + 1):
  #  password_list += random.choice(numbers)

  password_list=pass_letter+pass_symbol+pass_numbers
  random.shuffle(password_list)

  password = "".join(password_list)

  # for char in password_list:
  #  password += char
  password_input.delete(0, END)
  password_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()
    new_data={
        website:{
            "email":email,
            "password":password,
        }
        
    }
    
    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showwarning(
            title="Warning", message="Please don't leave any field empty!")
    else:
        is_ok=messagebox.askokcancel(title="Website", message="Are you sure to save the details")
        if is_ok:
            with open("data.json","r") as data_file:
                data=json.load(data_file)
                data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
                website_input.delete(0,END)
                password_input.delete(0,END)
        
# ---------------------------- UI SETUP ------------------------------- #

windows=Tk()
windows.title("Password Manager")
windows.config(padx=50,pady=50)

canvas =Canvas(width=200,height=200)
password=PhotoImage(file="Pass_manager.png")
canvas.create_image(100,100,image=password)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

website_input=Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2)

email_input=Entry(width=35)
email_input.insert(0,"cabhirup69@gmail.com")
email_input.grid(row=2,column=1,columnspan=2)

password_input=Entry(width=21)
password_input.grid(row=3,column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)




windows.mainloop()