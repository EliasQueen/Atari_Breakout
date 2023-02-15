from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class block:
    def __init__(self, posX, posY, width, height, color, points):
        self.x = posX
        self.y = posY
        self.w = width
        self.h = height
        self.color = color
        self.p = points

    def draw(self):
        glBegin(GL_QUADS)
        glColor3f(self.color[0], self.color[1], self.color[2])
        glVertex2f(self.x + 2.5, self.y - self.h + 1.25)
        glVertex2f(self.x + self.w - 2.5, self.y - self.h + 1.25)
        glVertex2f(self.x + self.w - 2.5, self.y - 1.25)
        glVertex2f(self.x + 2.5, self.y - 1.25)
        glEnd()
    
    def checkCollision(self, ball, oB):
        cout = [ball, 0, 0]
        _ = ball

        for i, point in enumerate(ball.points):
            collisionX = point[0] >= self.x and point[0] <= self.x + self.w
            collisionY = point[1] >= self.y - self.h and point[1] <= self.y
            if (collisionX and collisionY):
                if(oB.points[i][1] < (self.y - self.h)):
                    _.y = self.y - self.h - ball.r
                    _.dy = -1
                    return [_, 1, self.p]
                if(oB.points[i][1] > (self.y)):
                    _.y = self.y + ball.r
                    _.dy = 1
                    return [_, 1, self.p]

                if(oB.points[i][0] < self.x):
                    _.x = self.x - ball.r
                    _.dx = -1
                    return [_, 1, self.p]
                if(oB.points[i][0] > (self.x + self.w)):
                    _.x = self.x + self.w + ball.r
                    _.dx = 1
                    return [_, 1, self.p]

                cout = [_, 1, self.p]
        return cout
    
    def godCollision(self, posX, posY):
        if(self.x < posX < self.x + self.w):
            if(self.y - self.h < posY < self.y):
                return [True, self.p]
        return [False]