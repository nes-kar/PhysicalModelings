import numpy as np
import turtle 

pen = turtle.Turtle()
#pen.penup()
pen.speed(15)
pen.color("green")

f = turtle.Turtle()
f.color("purple")
f.speed(15)


def step(n):
	if n > 0.5:
		return 1
	else:
		return -1

x, y = 0, 0
xf, yf = 0, 0

def walk(x=x, y=y, xf=xf, yf=yf, steps=500):
	i = 0
	while i <= steps:
		dx = step(np.random.random(1))
		dy = step(np.random.random(1))
		x += dx
		y += dy
		pen.goto(x, y)
		dxf = step(np.random.random(1))
		dyf = step(np.random.random(1))
		xf += dxf
		yf += dyf
		f.goto(xf, yf)
		i += 1

walk(steps=1000)