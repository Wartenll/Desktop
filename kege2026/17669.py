from turtle import *
tracer(False)
screensize(3000,3000)
m=9

lt(90)

for i in range(4):
    fd(19*m)
    rt(90)
    fd(30*m)
    rt(90)
up()

fd(2*m)
rt(90)
fd(8*m)
lt(90)

down()

for i in range(4):
    fd(93*m)
    rt(90)
    fd(97*m)
    rt(90)
up()
for x in range(0,50):
    for y in range(0, 50):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()





update()
done()