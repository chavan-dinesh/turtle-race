from turtle import Turtle, Screen
import random

screen = Screen()

screen.listen()
screen.setup(width=500 , height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: (red, purple, yellow, blue)")

is_race_on = False
colors = ["red", "green", "yellow", "purple", "blue", "orange"]
if user_bet not in colors:
    print("Dumb! You chose wrong colour!")
    print(f"Choose the colour from {colors}")
    exit()
y_positions = [ 0, -100, -50, 140, 100, 50 ]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()