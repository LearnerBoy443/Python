from tkinter import *
root = Tk()
root.geometry('200x150')
button1 = Button(text="Button1")
button1.pack(side="left")
root.mainloop()

def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum
        
print(add(1,2,3,4,5,6,7,8,9,10))

def calculate(n,**kwargs):
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
calculate(2,add=3,multiply=5)
        
