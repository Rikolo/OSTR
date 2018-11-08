from turtle import *

scale = 5

def setScale(value):
    global scale
    scale = value

def E():
    penup()
    left(90)
    forward(4 * scale)
    right(90)
    forward(2 * scale)
    pendown()
    backward(2 * scale)
    right(90)
    forward(2 * scale)
    left(90)
    forward(1 * scale)
    penup()
    backward(1 * scale)
    right(90)
    pendown()
    forward(2 * scale)
    left(90)
    forward(2 * scale)
    penup()
    forward(0.5 * scale)

def H():
    penup()
    left(90)
    pendown()
    forward(4 * scale)
    penup()
    backward(2 * scale)
    right(90)
    pendown()
    forward(2 * scale)
    penup()
    left(90)
    forward(2 * scale)
    pendown()
    backward(4 * scale)
    penup()
    right(90)
    forward(0.5 * scale)


def L():
    penup()
    left(90)
    forward(4 * scale)
    pendown()
    backward(4 * scale)
    right(90)
    forward(2 * scale)
    penup()
    forward(0.5 * scale)

def O():
    penup()
    forward(1 * scale)
    left(45)
    pendown()
    forward(1.41 * scale)
    left(45)
    forward(2 * scale)
    left(45)
    forward(1.41 * scale)
    right(90)
    backward(1.41 * scale)
    left(45)
    backward(2 * scale)
    left(45)
    backward(1.41 * scale)    
    penup()
    right(90+45)
    forward(1.5 * scale)


def P():
    penup()
    right(90)
    pendown()
    backward(4 * scale)
    right(90)
    backward(1 * scale)
    right(45)
    backward(1.41 * scale)
    right(90)
    backward(1.41 * scale)
    right(45)
    backward(1 * scale)
    penup()
    right(33.7)
    forward(3.61 * scale)
    left(33.7)
    backward(0.5 * scale)
