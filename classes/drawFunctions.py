import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Função para desenhar retângulos
def dRetan(posX, posY, width, height, color):
    glBegin(GL_QUADS)
    glColor3f(color[0], color[1], color[2])
    glVertex2f(posX, posY - height)
    glVertex2f(posX + width, posY - height)
    glVertex2f(posX + width, posY)
    glVertex2f(posX, posY)
    glEnd()


# Função para desenhar losangos
def dLosan(posX, posY, width, height, color):
    glBegin(GL_QUADS)
    glColor3f(color[0], color[1], color[2])
    glVertex2f(posX - 0.5 * width, posY)
    glVertex2f(posX, posY + 0.5 * height)
    glVertex2f(posX + 0.5 * width, posY)
    glVertex2f(posX, posY - 0.5 * height)
    glEnd()


# Função para desenhar estrelas
def dEstre(posX, posY, radius, color):
    u = radius / 1.2
    glBegin(GL_POLYGON)
    glColor3f(color[0], color[1], color[2])
    glVertex2f(posX + 1.1 * u, posY + 1.5 * u)
    glVertex2f(posX + 4.8 * u, posY + 1.5 * u)
    glVertex2f(posX + 1.9 * u, posY - 0.6 * u)
    glVertex2f(posX + 2.9 * u, posY - 4.0 * u)
    glVertex2f(posX, posY - 2.0 * u)
    glVertex2f(posX - 2.9 * u, posY - 4.0 * u)
    glVertex2f(posX - 1.9 * u, posY - 0.6 * u)
    glVertex2f(posX - 4.8 * u, posY + 1.5 * u)
    glVertex2f(posX - 1.1 * u, posY + 1.5 * u)
    glVertex2f(posX, posY + 5.0 * u)
    glEnd()


# Função para desenhar círculos
def dCircu(posX, posY, points, radius, color):
    glBegin(GL_POLYGON)
    glColor3f(color[0], color[1], color[2])
    for i in range(points):
        cos = radius * math.cos(i * 2 * math.pi / points) + posX
        sin = radius * math.sin(i * 2 * math.pi / points) + posY
        glVertex2f(cos, sin)
    glEnd()
