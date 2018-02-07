"""Draws flowers."""

import turtle
import math


bob = turtle.Turtle()


def polyline(t, n, length, a):
    for i in range(n):
        t.fd(length)
        t.lt(a)


def arc(t, r, a):
    arc_length = 2 * math.pi * r * abs(a) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(a) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def petal(t, r, a):
    for i in range(2):
        arc(t, r, a)
        bob.lt(180-a)
    bob.lt(a)


def flower(t, r, a):
    n = int(360/a)
    for i in range(n):
        petal(t, r, a)


flower(bob, 200, 45)            # Length and angle are up to you
turtle.mainloop()