import turtle
turtle.setup()
def set_(s):
    turtle.circle(50+25*s)
    turtle.up()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.down()
n=4
turtle.pencolor("blue")
for i in range(n):
    set_(i)
turtle.hideturtle()
