import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()

def drawSpiral(t, t2, maxSide):
    for sideLength in range(1, maxSide+1, 5):
        t.forward(sideLength)
        t.right(90)
        t2.forward(sideLength)
        t2.left(90)

drawSpiral(t, t2, 150)
