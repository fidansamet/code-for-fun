"""Draws a hexagon with triangles."""

import turtle

bobby = turtle.Turtle()


def triangle(t, l, a):
    for i in range(3):
        t.fd(l)
        t.lt(180-a)
    t.lt(a)


def hexagon(t, l, n):
    a = 360/n
    t.lt(a/2)
    for i in range(n):
        triangle(t, l, a)


hexagon(bobby, 100, 6)

turtle.mainloop()

