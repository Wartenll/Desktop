from turtle import *
tracer(False)
screensize(3000,3000)
m=9

lt(90)

for i in range(2):
    fd(30*m)
    rt(90)
    fd(48*m)
    rt(90)
up()

fd(27*m)
rt(90)
fd(24*m)
lt(90)

down()

for i in range(9):
    fd(29*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
for x in range(0,50):
    for y in range(0, 50):
         goto(x*m, y*m)
         dot(3,'red')
update()
done()
