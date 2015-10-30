from graphics import *
import time
from random import randint
window = GraphWin("Visualisation", 600, 600)
datafile = open("datacopy.txt", 'r')

for line in datafile:
    grade = float(line)
    square = Rectangle(Point(200,50),Point(250,150))
    square.setFill(color_rgb(204,0,0))
    square.draw(window)

    
    
xspeed = 4
yspeed = 4

while True:
    currentPos = square.getCenter()
    if(currentPos.getY() >= 600): yspeed = -yspeed
    if(currentPos.getY() <= 0): yspeed = -yspeed
    if(currentPos.getX() >= 600): xspeed = -xspeed
    if(currentPos.getX() <= 0): xspeed = -xspeed
    square.move(xspeed,yspeed)
    
results = ["datafile" + square]




window.getMouse()


