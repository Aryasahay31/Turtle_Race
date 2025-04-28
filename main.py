from turtle import Turtle, Screen
import random
my_screen = Screen()
race_on = False

my_screen.setup(width= 500, height= 400)
user_bet = my_screen.textinput(title = "Make your bet", prompt = "which turtle will win the bet? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-240, y= y_positions[i])
    all_turtles.append(new_turtle)
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! The winning turtle is {winning_color}")
            else:
                print(f"You Lose! The winning turtle is {winning_color}")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

my_screen.exitonclick()