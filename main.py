# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 100)
# for each_color in colors:
#     r = each_color.rgb.r
#     g = each_color.rgb.g
#     b = each_color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35),
              (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64),
              (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79),
              (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90),
              (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210), (61, 60, 72), (183, 190, 204),
              (78, 66, 42), (23, 99, 96)]

# set tim's position to the edge of the frame, to include all dots in the same frame
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)  # turn left by 90 degree
        tim.forward(50)
        tim.setheading(180)  # turn left again
        tim.forward(500)  # move forward 10 dots X 50 paces
        tim.setheading(0)  # face right

screen = turtle_module.Screen()
screen.exitonclick()
