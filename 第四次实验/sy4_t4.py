import turtle
color_ls=["blue","green","red","black","orange"]
for x in range(1,20):
    turtle.color(color_ls[x%5])
    turtle.forward(100)
    turtle.left(95)
