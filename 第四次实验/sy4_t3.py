import turtle
ls=[3784,2205,1577,1015,673]
turtle.setup()
turtle.up()
turtle.goto(-300,0)
turtle.down()
def Draw(s):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(s//20)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(s//20)
    turtle.left(90)
    turtle.forward(50)
for i in ls:
    Draw(i)
turtle.forward(25)
turtle.left(135)
turtle.forward(10)
turtle.backward(10)
turtle.left(90)
turtle.forward(10)
turtle.up()
turtle.goto(-275,-50)
turtle.right(135)
turtle.down()
turtle.forward(270)
