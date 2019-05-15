import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Graficador:
    def __init__(self):
        pygame.init()
        display = (800, 800)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(45, 1, 0.5, 50)
        glTranslatef(0, -0.5, -3)

        self.clock = pygame.time.Clock()

    def graf(self, obj):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        self.clock.tick(10)

        corrimiento_x = -0.4

        for torre in obj.torres:
            glColor3f(0.5, 0.35, 0.1)
            glBegin(GL_LINES)
            glVertex3fv((corrimiento_x, 0 ,0))
            glVertex3fv((corrimiento_x, 0.8, 0))
            glEnd()

            glColor3f(1, 1, 1)
            glBegin(GL_QUADS)
            for i, elem in enumerate(torre):
                ancho = 0.4 * float(elem) / obj.nro_piezas
                bloque = [
                    (corrimiento_x - ancho/2, i*0.1, 0),
                    (corrimiento_x + ancho/2, i*0.1, 0),
                    (corrimiento_x + ancho/2, (i+1)*0.1, 0),
                    (corrimiento_x - ancho/2, (i+1)*0.1, 0)
                ]

                for vertex in bloque:
                    glVertex3fv(vertex)
            glEnd()

            corrimiento_x += 0.4

        pygame.display.flip()
