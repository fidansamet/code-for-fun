"""Draws a pentagon with triangles."""

import turtle

bobby = turtle.Turtle()


def triangle(t, l, a):
    t.fd(l)
    t.lt(180-((180-a)/2))
    t.fd(l+18)
    t.lt(180-((180-a)/2))
    t.fd(l)
    t.lt(180 - a)
    t.lt(a)


def petagon(t, l, n):
    a = 360/n
    t.lt(a/2)
    for i in range(n):
        triangle(t, l, a)


petagon(bobby, 100, 5)
turtle.mainloop()
