import turtle
draw = turtle.Turtle()
draw.color('pink','blue')
draw.begin_fill()
draw.speed(6)
draw.shape("turtle")
while True:
    draw.forward(350)
    draw.left(170)
    if abs(draw.pos()) < 1:
        break
draw.end_fill()
turtle.done()