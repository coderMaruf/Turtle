import turtle as t
t.speed(1)
t.bgcolor('black')

t.penup()
t.goto(-350, 0)
t.pendown()
t.pensize(2)
t.color('crimson')

for i in range(4):
    t.forward(150)
    t.left(90)
    

# Multicolor Square
t.penup()
t.goto(-180, 0)
t.pendown()

for i in ['crimson', 'green', 'orange', 'red']:
    t.color(i)
    t.forward(150)
    t.left(90)
    

# Square with fill and stroke
t.penup()
t.goto(0,0)
t.color('red', 'cyan')
t.pendown()
t.begin_fill()

for i in range(4):
    t.forward(150)
    t.left(90)
    
t.end_fill()

t.hideturtle()

t.exitonclick()