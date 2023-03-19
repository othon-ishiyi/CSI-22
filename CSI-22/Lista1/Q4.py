import turtle

def draw_two_sides(t, l, angle_shift):
    """Draw two consecutives sides of the spiral"""
    for i in range(2):
        t.forward(l)
        t.right(90 + angle_shift)

#Espiral 1 (ângulos de 90)
wn = turtle.Screen()
T = turtle.Turtle()
T.up()
T.ht()
T.setpos(-400, 0)
T.st()
T.down()
T.left(180)
side = 3

for i in range(100):
    draw_two_sides(T, side, 0)
    side = side + 3


#Espiral 2 (ângulos oblíquos)
wn = turtle.Screen()
T = turtle.Turtle()
T.up()
T.ht()
T.setpos(400, 0)
T.st()
T.down()
T.left(180)
side = 3

for i in range(50):
    draw_two_sides(T, side, -0.8)
    side = side + 3

wn.mainloop()
