from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class racket:
    def __init__(self, posX, posY, width, height, vel, color):
        self.x = posX
        self.y = posY
        self.w = width
        self.h = height
        self.v = vel
        self.color = color

    def draw(self):
        glBegin(GL_QUADS)
        glColor3f(self.color[0], self.color[1], self.color[2])
        glVertex2f(self.x, self.y - self.h)
        glVertex2f(self.x + self.w, self.y - self.h)
        glVertex2f(self.x + self.w, self.y)
        glVertex2f(self.x, self.y)
        glEnd()
    
    def checkCollision(self, ball):
        for _ in ball.points:
            collisionX = _[0] >= self.x and _[0] <= self.x + self.w
            collisionY = _[1] >= self.y - self.h and _[1] <= self.y
            if (collisionX and collisionY):
                if (_[0] >= self.x and _[0] < self.x + (self.w / 4)):
                    return -2
                elif (_[0] >= self.x + (self.w / 4) and _[0] < self.x + (self.w / 2)):
                    return -1
                elif (_[0] >= self.x + (self.w / 2) and _[0] < self.x + (3 * self.w / 4)):
                    return 1
                elif (_[0] >= self.x + (3 * self.w / 4) and _[0] < self.x + self.w):
                    return 2
        return 0

