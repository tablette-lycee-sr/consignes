from p5 import *
from random import randint

lettres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
lettre1 = int(randint(0, 24))
lettre2 = int(randint(0, 24))
lettre3 = int(randint(0, 24))
numerohasard = int(randint(1, 9))
global code
code = str(numerohasard)+str(lettres[lettre1])+str(lettres[lettre2])+str(lettres[lettre3])+"X"+str(10-numerohasard)

def setup():
    createCanvas(400, 400)
    colorMode(RGB)
    # Set angle mode so that atan2() returns angles in degrees
    angleMode(DEGREES)
       


def draw():
    background(255,216,103)
   
    textSize(18)
    fill('tomato')
    text("Python c'est aussi du dessin !", 90, 30)
    fill('cornflowerblue')
    text("Notez le code ci-dessous à la ligne 17 du script", 15, 230)
    fill('gray')
    text("#|   Mon code est:", 25, 260)
    textSize(30)
    text(code, 180, 260)
    fill('cornflowerblue')
    textSize(18)
    text("Revenez ensuite dans la vue Console", 20, 300)
    text("( utilisez le bouton  >_  ci-dessous)", 20, 320)
    text("et saissez ce code au prompt >>> ", 20, 340)
    text("puis appuyez sur la touche Entrée", 20, 360)

    # Draw left eye
    leftX = 150
    leftY = 150
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
    rightY = 150
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

    
