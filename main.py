import turtle
from turtle import Turtle, Screen
import random

turtle_list = []
is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_choice = screen.textinput(title="place your bet", prompt="which turtle will the race? Enter a color:")
colors = ["red", "blue", "green", "brown", "purple", "yellow"]
names = ["tom", "tim", "jake", "rose", "lily", "viola"]
if user_choice:
    is_race_on = True


for i in range(6):
    names[i] = Turtle(shape="turtle")
    names[i].color(colors[i])
    names[i].penup()
    names[i].goto(x=-230, y=(i+1)*25)
    turtle_list.append(names[i])
    names[i].speed("fastest")

while is_race_on:
    for turtles in turtle_list:
        if turtles.xcor() > 230:
            is_race_on = False
            winner = turtles.pencolor()
            if winner == user_choice:
                print(f"Your turtle wins!!")
            else:
                print(f"Your turtle lost...The winning turtle is {winner}")
        random_distance = random.randint(0, 10)
        turtles.forward(random_distance)





screen.exitonclick()