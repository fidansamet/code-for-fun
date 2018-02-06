"""Draws a heptagon with triangles."""

import turtle

bobby = turtle.Turtle()


def triangle_3(t, l, a):
    t.fd(l)
    t.lt(180-((180-a)/2))
    t.fd(l-13)
    t.lt(180-((180-a)/2))
    t.fd(l)
    t.lt(180 - a)
    t.lt(a)


def heptagon_2(t, l, n):
    a = 360/n
    t.lt(a/2)
    for i in range(n):
        triangle_3(t, l, a)


heptagon_2(bobby, 100, 7)
turtle.mainloop()