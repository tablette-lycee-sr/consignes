from p5 import *

def setup():
    createCanvas(400, 400)
    colorMode(RGB)
    # Set angle mode so that atan2() returns angles in degrees
    angleMode(DEGREES)
    



    


def draw():
    background(255,216,103)

    lettres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
    lettre1 = int(random(0, 24))
    lettre2 = int(random(0, 24))
    lettre3 = int(random(0, 24))
    numerohasard = int(random(1, 9))
    code = str(numerohasard)+str(lettres[lettre1])+str(lettres[lettre2])+str(lettres[lettre3])+str(10-numerohasard)
    textSize(18)
    fill('limegree')
    text("Python c'est aussi du dessin !", 50, 300)
    fill('cornflowerblue')
    text(code, 6, 45)
    fill('tomato')
    text('rainbows', 6, 70)

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

    
