import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class ball:
    def __init__(self, posX, posY, velX, dirX, velY, dirY, radius, color):
        self.x = posX
        self.y = posY
        self.vx = velX
        self.dx = dirX
        self.vy = velY
        self.dy = dirY
        self.r = radius
        self.color = color
        self.points = []

    def copy(self, ball):
        self.x = ball.x
        self.y = ball.y
        self.vx = ball.vx
        self.dx = ball.dx
        self.vy = ball.vy
        self.dy = ball.dy
        self.r = ball.r
        self.color = ball.color
        self.points = ball.points

    def draw(self):
        self.points = []
        glBegin(GL_POLYGON)
        glColor3f(self.color[0], self.color[1], self.color[2])
        for _ in range(10):
            cos = self.r * math.cos(_ * 2 * math.pi / 10) + self.x
            sin = self.r * math.sin(_ * 2 * math.pi / 10) + self.y
            self.points.append([cos, sin])
            glVertex2f(cos, sin)
        glEnd()
