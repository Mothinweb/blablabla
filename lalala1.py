#!/usr/bin/python3
import turtle
turtle.shape("turtle")
turtle.speed(10)

for i in range (100):
    for m in range(4):
        turtle.forward(10+i*10)
        turtle.left(90)
    turtle.penup()
    turtle.right(135)
    turtle.forward(5*2**0.5)
    turtle.left(135)
    turtle.pendown()
