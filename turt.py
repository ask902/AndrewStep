from turtle import *
color('pink', 'purple')
begin_fill()
while True:
    forward(150)
    left(100)
    forward(40)
    left(30)
    if abs(pos()) < 1:
        break
end_fill()
done()