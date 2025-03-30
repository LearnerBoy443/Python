from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    Timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long_break_sec)
        Timer_label.config(text="Break",fg=RED)
    if reps%2==0:
        count_down(short_break_sec)
        Timer_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        Timer_label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=windows.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark = "✓"
            check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

windows=Tk()
windows.title("Pamodora")
windows.config(padx=100,pady=50,bg=YELLOW)


canvas =Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,128,text="00:00",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2, column=2)


Timer_label=Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
Timer_label.grid(row=1,column=2)

check_mark = Label(fg=GREEN,bg=YELLOW)
check_mark.grid(row=3, column=2)

button = Button(text="Start",command=start_timer)
button.grid(row=3,column=1)
button = Button(text="Reset",command=reset_timer)
button.grid(row=3,column=3)


windows.mainloop()