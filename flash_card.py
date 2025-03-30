from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card={}

def next_card():
    global current_card,flip_timer
    windows.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(background_image,image=card_front_img)
    flip_timer=windows.after(3000,func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(background_image,image=card_back_img)
    

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv",index=False)
    next_card()
    
windows=Tk()
windows.title("Flash")
windows.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=windows.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
card_front_img=PhotoImage(file="card_front.png")
card_back_img=PhotoImage(file="card_back.png")
background_image=canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400, 150,text="Title",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="Word", font=("Ariel",35, "bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image=PhotoImage(file="right.png")
known_button = Button(image=check_image, highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)


next_card()


windows.mainloop()