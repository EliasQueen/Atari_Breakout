from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

w = [1, 1, 1]

def segA(posX, posY, size):
    width = 420 * size / 48
    height = 700 * size / 48

    glBegin(GL_POLYGON)
    glColor3f(w[0], w[1], w[2])
    glVertex2f(posX + 0 * width / 3, posY - 0 * height / 5)
    glVertex2f(posX + 0 * width / 3, posY - 1 * height / 5)
    glVertex2f(posX + 3 * width / 3, posY - 1 * height / 5)
    glVertex2f(posX + 3 * width / 3, posY - 0 * height / 5)
    glEnd()

def segB(posX, posY, size):
    width = 420 * size / 48
    height = 700 * size / 48

    glBegin(GL_POLYGON)
    glColor3f(w[0], w[1], w[2])
    glVertex2f(posX + 2 * width / 3, posY - 0 * height / 5)
    glVertex2f(posX + 2 * width / 3, posY - 3 * height / 5)
    glVertex2f(posX + 3 * width / 3, posY - 3 * height / 5)
    glVertex2f(posX + 3 * width / 3, posY - 0 * height / 5)
    glEnd()

def segC(posX, posY, size):
    width = 420 * size / 48
    height = 700 * size / 48

    glBegin(GL_POLYGON)
    glColor3f(w[0], w[1], w[2])
    glVertex2f(posX + 2 * width / 3, posY - 2 * height / 5)
    glVertex2f(posX + 2 * width / 3, posY - 5 * height / 5)
    glVertex2f(posX + 3 * width / 3, posY - 5 * height / 5)
    glVertex2f(posX + 3 * width / 3, posY - 2 * height / 5)
    glEnd()

def segD(posX, posY, size):
    width = 420 * size / 48
    height = 700 * size / 48

    glBegin(GL_POLYGON)
    glColor3f(w[0], w[1], w[2])
    glVertex2f(posX + 0 * width / 3, posY - 4 * height / 5)
    glVertex2f(posX + 0 * width / 3, posY - 5 * height / 5)
    glVertex2f(posX + 3 * width / 3, posY - 5 * height / 5)
    glVertex2f(posX + 3 * width / 3, posY - 4 * height / 5)
    glEnd()

def segE(posX, posY, size):
    width = 420 * size / 48
    height = 700 * size / 48

    glBegin(GL_POLYGON)
    glColor3f(w[0], w[1], w[2])
    glVertex2f(posX + 0 * width / 3, posY - 2 * height / 5)
    glVertex2f(posX + 0 * width / 3, posY - 5 * height / 5)
    glVertex2f(posX + 1 * width / 3, posY - 5 * height / 5)
    glVertex2f(posX + 1 * width / 3, posY - 2 * height / 5)
    glEnd()

def segF(posX, posY, size):
    width = 420 * size / 48
    height = 700 * size / 48

    glBegin(GL_POLYGON)
    glColor3f(w[0], w[1], w[2])
    glVertex2f(posX + 0 * width / 3, posY - 0 * height / 5)
    glVertex2f(posX + 0 * width / 3, posY - 3 * height / 5)
    glVertex2f(posX + 1 * width / 3, posY - 3 * height / 5)
    glVertex2f(posX + 1 * width / 3, posY - 0 * height / 5)
    glEnd()

def segG(posX, posY, size):
    width = 420 * size / 48
    height = 700 * size / 48

    glBegin(GL_POLYGON)
    glColor3f(w[0], w[1], w[2])
    glVertex2f(posX + 0 * width / 3, posY - 2 * height / 5)
    glVertex2f(posX + 0 * width / 3, posY - 3 * height / 5)
    glVertex2f(posX + 3 * width / 3, posY - 3 * height / 5)
    glVertex2f(posX + 3 * width / 3, posY - 2 * height / 5)
    glEnd()

def dno(no, posX, posY, size):
    if(no == 0):
        n0(posX, posY, size)
    elif(no == 1):
        n1(posX, posY, size)
    elif(no == 2):
        n2(posX, posY, size)
    elif(no == 3):
        n3(posX, posY, size)
    elif(no == 4):
        n4(posX, posY, size)
    elif(no == 5):
        n5(posX, posY, size)
    elif(no == 6):
        n6(posX, posY, size)
    elif(no == 7):
        n7(posX, posY, size)
    elif(no == 8):
        n8(posX, posY, size)
    elif(no == 9):
        n9(posX, posY, size)

def n0(posX, posY, size):
    segA(posX, posY, size)
    segB(posX, posY, size)
    segC(posX, posY, size)
    segD(posX, posY, size)
    segE(posX, posY, size)
    segF(posX, posY, size)

def n1(posX, posY, size):
    segB(posX, posY, size)
    segC(posX, posY, size)

def n2(posX, posY, size):
    segA(posX, posY, size)
    segB(posX, posY, size)
    segG(posX, posY, size)
    segE(posX, posY, size)
    segD(posX, posY, size)

def n3(posX, posY, size):
    segA(posX, posY, size)
    segB(posX, posY, size)
    segC(posX, posY, size)
    segD(posX, posY, size)
    segG(posX, posY, size)

def n4(posX, posY, size):
    segF(posX, posY, size)
    segG(posX, posY, size)
    segB(posX, posY, size)
    segC(posX, posY, size)

def n5(posX, posY, size):
    segA(posX, posY, size)
    segF(posX, posY, size)
    segG(posX, posY, size)
    segC(posX, posY, size)
    segD(posX, posY, size)

def n6(posX, posY, size):
    segA(posX, posY, size)
    segF(posX, posY, size)
    segE(posX, posY, size)
    segD(posX, posY, size)
    segC(posX, posY, size)
    segG(posX, posY, size)

def n7(posX, posY, size):
    segA(posX, posY, size)
    segB(posX, posY, size)
    segC(posX, posY, size)

def n8(posX, posY, size):
    segA(posX, posY, size)
    segB(posX, posY, size)
    segC(posX, posY, size)
    segD(posX, posY, size)
    segE(posX, posY, size)
    segF(posX, posY, size)
    segG(posX, posY, size)

def n9(posX, posY, size):
    segA(posX, posY, size)
    segB(posX, posY, size)
    segC(posX, posY, size)
    segF(posX, posY, size)
    segG(posX, posY, size)