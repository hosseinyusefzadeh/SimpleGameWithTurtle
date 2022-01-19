import random
import turtle
from turtle import Turtle, Screen


###################Sketching########################
# juju = Turtle()
# screen = Screen()
#
#
# def move_forward():
#     juju.forward(30)
#
# def move_backward():
#     juju.back(30)
#
# def right():
#         new_pos = juju.heading() + 10
#         juju.setheading(new_pos)
# def left():
#         new_pos = juju.heading() + -10
#         juju.setheading(new_pos)
#
# def clear():
#     screen.reset()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=right)
# screen.onkey(key="d", fun=left)
# screen.onkey(key="c", fun=clear)

# screen.exitonclick()


##################turtle Racing####################

# is_race_on = False
# screen = Screen()
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# colors = ["red", "orange", "blue", "yellow", "purple", "green"]
# positions = [-70, -40, -10, 20, 50, 80]
# all_turtles = []
#
# for turtle_index in range(0, 6):
#     new_turtle = Turtle(shape="turtle")
#     new_turtle.color(colors[turtle_index])
#     new_turtle.penup()
#     new_turtle.goto(x=-230, y=positions[turtle_index])
#     all_turtles.append(new_turtle)
#
# if user_bet:
#     is_race_on = True
#
# while is_race_on:
#
#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've won. the {winning_color} turtle is winner!")
#             else:
#                 print(f"You've Lost! The {winning_color} turtle is winner!")
#                 is_race_on = False
#         rand_distance = random.randint(0, 10)
#         turtle.forward(rand_distance)
#
# screen.exitonclick()