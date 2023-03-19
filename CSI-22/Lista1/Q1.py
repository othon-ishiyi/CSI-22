import turtle

def draw_square(t, l):
    """Make turtle t draw a square of l."""
    for i in range(4):
        t.forward(l)
        t.left(90)

wn = turtle.Screen()
T = turtle.Turtle()
side = 20

for i in range(5):
    T.up()
    T.ht()
    T.setpos(-side/2, -side/2)
    T.st()
    T.down()
    draw_square(T, side)
    side = side + 20

wn.mainloop()
