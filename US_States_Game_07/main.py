import turtle
import os
import pandas
import statename
import time

path_curr_folder = os.path.dirname(os.path.abspath(__file__))
print(path_curr_folder)

screen = turtle.Screen()
screen.title("U.S States Game")
image = path_curr_folder + "/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width = 800, height = 600)
screen.tracer(0)

file = path_curr_folder + "/50_states.csv"
data_raw = pandas.read_csv(file)
#print(data_raw)

keep_playing = True
while keep_playing:
    answer_state   = screen.textinput(title="Guess the State",prompt="What's another state's name?")
    data_sel_state = data_raw[data_raw.state == answer_state]
    data_xcor      = float(data_sel_state.x.values[0])
    data_ycor      = float(data_sel_state.y.values[0])
    state_name     = statename.StateName(answer_state,data_xcor,data_ycor)

    move_statename = True
    while move_statename:
        time.sleep(0.01)
        screen.update()

        state_name.speed()
        state_name.move()
        
        check_arrival = state_name.check_position()
        if check_arrival == False:
            state_name.write_statename()
        else:
            state_name.goto(data_xcor,data_ycor)
            state_name.write_statename()
            move_statename = False        

def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

#screen.exitonclick()