import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. States game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#   print(x,y)
    
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()


data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_state=[]
while len(guessed_state) < 50:
   answer_state=screen.textinput(title=f"{len(guessed_state)}/50 states are correct" , prompt="Enter the next state known.").title()
   
   if answer_state=="Exit":
       missing_states = [
           state for state in all_states if state not in guessed_state]
       #for state in all_states:
           #if state not in guessed_state:
             #missing_states.append(state)
             
       df=pandas.DataFrame(missing_states)
       df.to_csv("states_to_learn.csv")
       break
     
   if answer_state in all_states:
       guessed_state.append(answer_state)
       t=turtle.Turtle()
       t.hideturtle()
       t.penup()
       state_data=data[data.state==answer_state]
       t.goto(state_data.x.item(),state_data.y.item())
       t.write(answer_state)
       
screen.exitonclick()