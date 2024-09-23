from p5 import *

def setup():
    createCanvas(400, 400)
    colorMode(HSB)
    # Set angle mode so that atan2() returns angles in degrees
    angleMode(DEGREES)


def draw():
    background(0)
    # Draw left eye
    leftX = 150
    leftY = 200
    # Calculate angle between left eye and mouse
    leftAngle = atan2(mouseY - leftY, mouseX - leftX)
    push()
    translate(leftX, leftY)
    fill(255)
    ellipse(0, 0, 50, 50)
    rotate(leftAngle)
    fill(0)
    ellipse(12.5, 0, 25, 25)
    pop()
    # Draw right eye
    rightX = 250
    rightY = 200
    # Calculate angle between right eye and angle
    rightAngle = atan2(mouseY - rightY, mouseX - rightX)
    push()
    translate(rightX, rightY)
    fill(255)
    ellipse(0, 0, 50, 50)
    rotate(rightAngle)
    fill(0)
    ellipse(12.5, 0, 25, 25)
    pop()
