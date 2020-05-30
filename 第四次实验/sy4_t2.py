import turtle
def kooh(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        for i in [0,60,-120,60]:
            turtle.left(i)
            kooh(size/3,n-1)


turtle.setup()

turtle.penup()
turtle.goto(-100,100)
turtle.pendown()

turtle.pencolor("red")
turtle.pensize(2)
for i in range(4):
    kooh(120,3)
    turtle.right(120)

turtle.hideturtle()
