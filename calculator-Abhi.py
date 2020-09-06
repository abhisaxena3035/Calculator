"""
Create button GUI for each number and operation
Create a rect to display numbers/answers
Link rect to display numbers clicked and operation then answer

"""
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500,500))
BGCOLOR = (0,0,0)
pygame.display.set_caption('Calculator')
list_display_objects = ['1','2','3','+','4','5','6','-','7','8','9','x','AC','0','=','/']    
BASICFONT = pygame.font.Font('freesansbold.ttf', 32)
strNum = ""
firstNum = 0
operator = ""

def makeCircle(x,y,num):
    global BASICFONT
    pygame.draw.circle(DISPLAYSURF,(0,0,255),(x,y),37,0)
    tempSurf = BASICFONT.render(num,True,(255,255,255))
    tempRect = tempSurf.get_rect()
    tempRect.center = (x,y)
    DISPLAYSURF.blit(tempSurf, tempRect)

def drawCalculator():
    updated_x = 0
    updated_y = 50
    for i in range(16):
        if i%4 == 0:
            updated_y += 100
            updated_x = 100
        else:
            updated_x+=100
        makeCircle(updated_x,updated_y,list_display_objects[i])

def refreshRect(strNum):
    numSurf = BASICFONT.render(strNum,True,(255,255,255))
    numRect = numSurf.get_rect()
    numRect.center = (250,55)
    DISPLAYSURF.blit(numSurf, numRect)

def checkPos(x,y):
    global BASICFONT, strNum, numSurf, numRect, firstNum, operator
    if pygame.Rect(50,110,80,80).collidepoint(x,y):
        strNum += "1"
    if pygame.Rect(150,110,80,80).collidepoint(x,y):
        strNum += "2"
    if pygame.Rect(250,110,80,80).collidepoint(x,y):
        strNum += "3"
    if pygame.Rect(350,110,80,80).collidepoint(x,y):
        firstNum = int(strNum)
        strNum = ""
        operator = "+"
    if pygame.Rect(50,210,80,80).collidepoint(x,y):
        strNum += "4"
    if pygame.Rect(150,210,80,80).collidepoint(x,y):
        strNum += "5"
    if pygame.Rect(250,210,80,80).collidepoint(x,y):
        strNum += "6"
    if pygame.Rect(350,210,80,80).collidepoint(x,y):
        firstNum = int(strNum)
        strNum = ""
        operator = "-"
    if pygame.Rect(50,310,80,80).collidepoint(x,y):
        strNum += "7"
    if pygame.Rect(150,310,80,80).collidepoint(x,y):
        strNum += "8"
    if pygame.Rect(250,310,80,80).collidepoint(x,y):
        strNum += "9"
    if pygame.Rect(350,310,80,80).collidepoint(x,y):
        firstNum = int(strNum)
        strNum = ""
        operator = "x"
    if pygame.Rect(50,410,80,80).collidepoint(x,y):
        strNum = ""
        operator = ""
        firstNum = 0
    if pygame.Rect(150,410,80,80).collidepoint(x,y):
        strNum += "0"
    if pygame.Rect(250,410,80,80).collidepoint(x,y):
        if operator == "+":
            firstNum = float(firstNum)
            strNum = float(strNum)
            strNum = str(firstNum + int(strNum))
        if operator == "-":
            firstNum = float(firstNum)
            strNum = float(strNum)
            strNum = str(firstNum - int(strNum))
        if operator == "x":
            firstNum = float(firstNum)
            strNum = float(strNum)
            strNum = str(firstNum * int(strNum))
        if operator == "/":
            firstNum = float(firstNum)
            strNum = float(strNum)
            strNum = str(firstNum / strNum)
    if pygame.Rect(350,410,80,80).collidepoint(x,y):
        firstNum = int(strNum)
        strNum = ""
        operator = "/"
    
    
    

while True:
    DISPLAYSURF.fill(BGCOLOR)
    drawCalculator()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mousex,mousey = event.pos
            checkPos(mousex,mousey)
    refreshRect(strNum)
    pygame.display.update()   




            

