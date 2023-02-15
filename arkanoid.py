import math
from random import randrange

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT import GLUT_BITMAP_TIMES_ROMAN_24

import classes.ball
import classes.block
import classes.drawFunctions as env
import classes.drawNumbers as d
import classes.racket

global windowWidth, windowHeight, windowX, windowY, w1, h1
global tela, raquete, bola, oB, points, lifes, gm_stt, mod_vel, checks
global gm_run, gm, hits

# Definindo variáveis globais da tela
windowWidth = 500
windowHeight = 660
windowX = 350
windowY = 10

# Variáveis de cor
azul = [0/255, 92/255, 139/255]
verde = [0/255, 168/255, 89/255]
amarelo = [255/255, 221/255, 33/255]
branco = [1, 1, 1]
cinza = [200 / 255, 200 / 255, 200 / 255]
blocos_color = [[163 / 255, 30 / 255, 10 / 255],
                [194 / 255, 133 / 255, 10 / 255],
                [10 / 255, 133 / 255, 51 / 255],
                [194 / 255, 194 / 255, 41 / 255]]

# Criando objetos do jogo
raquete = classes.racket.racket(int((windowWidth - 80) / 2), 80, 100, 15, 15, azul)
bola = classes.ball.ball(int(windowWidth / 2), 1000, 0, 0, 0, 0, 6, branco)
oB = classes.ball.ball(int(windowWidth / 2), 1000, 0, 0, 0, 0, 6, branco)
blocos = []
for i in range(8):
    blocos.append([])
    c = blocos_color[math.floor(i / 2)]
    p = 7 - 2 * math.floor(i / 2)
    for j in range(14):
        _ = classes.block.block(7.5 + j * ((windowWidth - 15) / 14), windowHeight - 160 - (i * 20), (windowWidth - 15) / 14, 15, c, p)
        blocos[i].append(_)

# Definindo variáveis funcionais do sistema
gm = 0  # GOD MODE
tela = 0
hits = 0
points = 0
gm_stt = 0
gm_run = 0
mod_vel = 1
checks = [0, 0, 0, 0, 0]  # tocar no topo, 4 hits, 12 hits, tocar laranja, tocar vermelho

# Definindo quantidade de vidas
lifes = []
for _ in range(3):
    lifes.append(classes.ball.ball(((windowWidth - 44) / 2) + (_ * 22), windowHeight - 80, 0, 0, 0, 0, 9, branco))


# Função do desenho
def desenha():
    global windowWidth, windowHeight, windowX, windowY, w1, h1
    global raquete, bola, points, lifes

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClear(GL_COLOR_BUFFER_BIT)

    if(gm_stt == 0):
        # Desenhando ambiente:
        env.dRetan(0, windowHeight, 10, windowHeight, cinza)
        env.dRetan(windowWidth - 10, windowHeight, 10, windowHeight, cinza)
        env.dRetan(0, 500, 10, 40, blocos_color[0])
        env.dRetan(windowWidth - 10, 500, 10, 40, blocos_color[0])
        env.dRetan(0, 460, 10, 40, blocos_color[1])
        env.dRetan(windowWidth - 10, 460, 10, 40, blocos_color[1])
        env.dRetan(0, 420, 10, 40, blocos_color[2])
        env.dRetan(windowWidth - 10, 420, 10, 40, blocos_color[2])
        env.dRetan(0, 380, 10, 40, blocos_color[3])
        env.dRetan(windowWidth - 10, 380, 10, 40, blocos_color[3])
        env.dRetan(0, 87.5, 10, 30, azul)
        env.dRetan(windowWidth - 10, 87.5, 10, 30, azul)
        env.dRetan(0, windowHeight - 20, windowWidth, 30, cinza)

        # Programa Principal
        desenhaPontos(points, (windowWidth - 58) / 2, int(windowHeight - 110), 2)
        desenhaTexto("Vidas extras:", 20, int(windowHeight - 85), branco)
        if(gm_run == 0):
            desenhaTexto("Clique na tela para começar.", 115, 180, branco)
        elif(gm_run == 1):
            desenhaTexto("Clique na tela para continuar.", 110, 180, branco)
        raquete.draw()
        bola.draw()

        for i in blocos:
            for j in i:
                j.draw()

        for _ in lifes:
            _.draw()
    elif(gm_stt == 1):
        desenhaTexto("Fim de jogo, obrigado por jogar!", int(windowWidth / 2 - 160), int(windowHeight / 2), branco)
        desenhaTexto("Pontuação final: " + str(points), int(windowWidth / 2 - 100), int(windowHeight / 2 - 50), branco)
    else:
        desenhaTexto("Jogo pausado.", int(windowWidth / 2 - 60), int(windowHeight / 2), branco)
        desenhaTexto("Retome a partir do menu.", int(windowWidth / 2 - 120), int(windowHeight / 2 - 50), branco)

    glutSwapBuffers()


# Função do timer
def timer(value):
    global windowWidth, windowHeight, windowX, windowY, w1, h1
    global tela, raquete, bola, oB, points, lifes, gm_stt, gm_run, mod_vel
    global hits, checks

    mod_vel = 1 + 0.25 * checks[1] + 0.25 * checks[2] + 0.25 * checks[3] + 0.25 * checks[4]

    for _, i in enumerate(blocos):
        if(i == []):
            del blocos[_]
    
    if(blocos == [] and tela == 0):
        for i in range(8):
            blocos.append([])
            c = blocos_color[math.floor(i / 2)]
            p = 7 - 2 * math.floor(i / 2)
            for j in range(14):
                _ = classes.block.block(7.5 + j * ((windowWidth - 15) / 14), windowHeight - 160 - (i * 20), (windowWidth - 15) / 14, 15, c, p)
                blocos[i].append(_)
        gm_run = 1
        tela = 1
        bola.y = 1000

    if(gm_stt == 0):
        if(gm_run == 2):
            # Verificação da raquete
            if(checks[0] == 1):
                raquete.w = 50
            if(raquete.x < 10):
                raquete.x = 10
            if(raquete.x + raquete.w > windowWidth - 10):
                raquete.x = windowWidth - raquete.w - 10

            # Verificação em X da bola
            if(bola.x - bola.r < 10):
                bola.x = bola.r + 10
                bola.dx = 1
            if(bola.x + bola.r > windowWidth - 10):
                bola.x = windowWidth - bola.r - 10
                bola.dx = -1

            # Verificação em Y da bola
            if(bola.y - bola.r < 0):
                bola.y = bola.r
                bola.dx = 0
                bola.dy = 0
                if(len(lifes) != 0):
                    lifes.pop()
                gm_run = 1
            if(bola.y + bola.r > windowHeight - 50):
                checks[0] = 1
                bola.y = windowHeight - bola.r - 50
                bola.dy = -1

            c = raquete.checkCollision(bola)
            if(c != 0):
                bola.dy = 1
                match c:
                    case -2:
                        bola.dx = -1
                        bola.vx = 2
                    case -1:
                        bola.dx = -1
                        bola.vx = 1
                    case 1:
                        bola.dx = 1
                        bola.vx = 1
                    case 2:
                        bola.dx = 1
                        bola.vx = 2

            bola.x += 5 * bola.dx * bola.vx * mod_vel
            bola.y += 5 * bola.dy * bola.vy * mod_vel

            for x, i in enumerate(blocos):
                for y, j in enumerate(i):
                    cout = j.checkCollision(bola, oB)
                    if(cout[1] == 1):
                        if(0 <= x <= 1):
                            checks[4] = 1
                        if(2 <= x <= 3):
                            checks[3] = 1
                        hits += 1
                        bola = cout[0]
                        oB.copy(bola)
                        points = points + cout[2]
                        del i[y]
                        if(hits >= 4):
                            checks[1] = 1
                        if(hits >= 12):
                            checks[2] = 1
            
            # Armazenando posição atual
            oB.copy(bola)

            # Verificação do estado do jogo
            if(len(lifes) == 0):
                gm_stt = 1

    # Redesenha o quadrado com as novas coordenadas
    glutPostRedisplay()
    glutTimerFunc(33, timer, 1)

# Função de mudar tamanho da janela
def gerenciaTamanhoJanela(w, h):
    global w1, h1, windowWidth, windowHeight

    if(w == 0):
        w = 1
    if(h == 0):
        h = 1

    # Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)

    # Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, windowWidth, 0.0, windowHeight)

    windowWidth = w
    windowHeight = h

    w1 = w
    h1 = h


def gerenciaTeclado(key, x, y):
    global windowWidth, windowHeight, windowX, windowY, w1, h1
    global raquete, bola, oR, oB, gm_stt, mod_vel
    
    if(key == b'\x1b'):
        glutLeaveMainLoop()

    glutPostRedisplay()


def gerenciaTeclasEspeciais(key, x, y):
    global windowWidth, windowHeight, windowX, windowY, w1, h1
    global raquete, bola, oR, oB

    if(key == GLUT_KEY_LEFT):
        raquete.x -= 15

    if(key == GLUT_KEY_RIGHT):
        raquete.x += 15

    glutPostRedisplay()


def gerenciaMouse(button, state, x, y):
    global windowWidth, windowHeight, windowX, windowY, w1, h1
    global raquete, bola, oR, oB, gm_run
    
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            if(gm_stt == 0):
                if(gm_run == 0 or gm_run == 1):
                    bola.x = windowWidth / 2
                    bola.y = 260
                    bola.vx = 1
                    bola.vy = 1
                    bola.dy = 1
                    _ = randrange(2)
                    if(_):
                        bola.dx = -1
                    else:
                        bola.dx = 1
                    gm_run = 2
    glutPostRedisplay()


def gerenciaMouseClicado(x, y):
    global windowWidth, windowHeight, windowX, windowY, w1, h1
    global raquete, bola, oR, oB, gm_run

    if(gm_run == 2):
        if((raquete.w / 2) <= x <= (windowWidth - (raquete.w / 2))):
            raquete.x = x - raquete.w / 2

    glutPostRedisplay()


def gerenciaMouseMovendo(x, y):
    global gm_stt, gm, blocos, windowHeight, points

    if(gm_stt == 0 and gm == 1):
        for i in blocos:
            for _, j in enumerate(i):
                c = j.godCollision(x, windowHeight - y)
                if(c[0]):
                    points += c[1]
                    del i[_]



def desenhaTexto(string, posX, posY, color):
    global windowWidth, windowHeight, windowX, windowY, w1, h1

    glPushMatrix()
    
    glColor3f(color[0], color[1], color[2])
    glRasterPos2f(posX, posY)

    # Exibe caracter a caracter
    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
    glPopMatrix()


def desenhaPontos(points, posX, posY, size):
    points = str(points).zfill(3)
    dist = 420 * size / 48
    x = 0
    for n in str(points):
        d.dno(int(n), posX + (x * (dist + size * 1.5)), posY, size)
        x += 1


def pausar():
    global bola, gm_run, gm_stt

    gm_stt = 2
    gm_run = 1
    bola.vx = 0
    bola.vy = 0


def despausar():
    global gm_stt
    gm_stt = 0


def restart():
    global tela, raquete, bola, oB, points, lifes, gm_stt, gm_run, mod_vel
    global hits, checks, blocos

    tela = 0
    hits = 0
    points = 0
    gm_stt = 0
    gm_run = 0
    mod_vel = 1
    checks = [0, 0, 0, 0, 0]

    raquete.x = int((windowWidth - 80) / 2)
    raquete.w = 100
    bola.x = int(windowWidth / 2)
    bola.y = 1000
    bola.vx = 0
    bola.vy = 0
    oB.copy(bola)

    blocos = []
    for i in range(8):
        blocos.append([])
        c = blocos_color[math.floor(i / 2)]
        p = 7 - 2 * math.floor(i / 2)
        for j in range(14):
            _ = classes.block.block(7.5 + j * ((windowWidth - 15) / 14), windowHeight - 160 - (i * 20), (windowWidth - 15) / 14, 15, c, p)
            blocos[i].append(_)

    lifes = []
    for _ in range(3):
        lifes.append(classes.ball.ball(((windowWidth - 44) / 2) + (_ * 22), windowHeight - 80, 0, 0, 0, 0, 9, branco))


def menuFunc(op):
    global gm

    if(op == 0):
        pausar()
    if(op == 1 ):
        despausar()
    if(op == 2):
        restart()
    if(op == 3):
        gm = int(not bool(gm))
    if(op == -1):
        glutLeaveMainLoop()
    menu()
    return 0


def menu():
    global gm_stt, gm

    glutCreateMenu(menuFunc)
    if(gm_stt == 2):
        glutAddMenuEntry("Retomar", 1)
    else:
        glutAddMenuEntry("Pausar", 0)
    glutAddMenuEntry("Reiniciar", 2)
    if(gm == 0):
        glutAddMenuEntry("Ativar GOD MODE", 3)
    else:
        glutAddMenuEntry("Desativar GOD MODE", 3)
    glutAddMenuEntry("Sair", -1)
    glutAttachMenu(GLUT_RIGHT_BUTTON)


def main():
    global windowWidth, windowHeight, windowX, windowY, w1, h1
    global raquete, bola, oR, oB
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(windowWidth, windowHeight)
    glutInitWindowPosition(windowX, windowY)
    glutCreateWindow(b'Atari Breakout')
    glutDisplayFunc(desenha)
    glutReshapeFunc(gerenciaTamanhoJanela)
    glutKeyboardFunc(gerenciaTeclado)
    glutSpecialFunc(gerenciaTeclasEspeciais)
    glutMouseFunc(gerenciaMouse)
    glutMotionFunc(gerenciaMouseClicado)
    glutPassiveMotionFunc(gerenciaMouseMovendo)
    glutTimerFunc(33, timer, 1)
    glClearColor(0, 0, 0, 1.0)
    menu()
    glutMainLoop()


if __name__ == "__main__":
    main()
