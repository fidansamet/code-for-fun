"""Draws snowflakes."""

import turtle

bobby = turtle.Turtle()


def koch(t, l):
    if l < 10:
        t.fd(l)
    else:
        koch(t, l/3)
        t.lt(60)
        koch(t, l/3)
        t.rt(120)
        koch(t, l/3)
        t.lt(60)
        koch(t, l/3)


def snowflake(t, l):
    for i in range(3):
        koch(t, l)
        t.rt(120)


snowflake(bobby, 500)
turtle.mainloop()
