import turtle as t

t.speed(1)
t.bgcolor('dodgerblue')

t.penup()
t.goto(-150, -100)
t.fillcolor('orangered')
t.begin_fill()
t.pendown()

# t.forward(300)
# t.left(120)
# t.forward(300)
# t.left(120)
# t.forward(300)
# t.left(120)

for i in range(3):
    t.forward(300)
    t.left(120)

t.end_fill()
t.hideturtle()