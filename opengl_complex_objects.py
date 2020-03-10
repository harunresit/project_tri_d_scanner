import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices= (
        (0, 0, 0),    #0
        (1, 0, 0),    #1
        (0.5, 0, 1),      #2
        (0, 2, 0),    #3
        (1, 2, 0),    #4
        (0.5, 2, 1)      #5
    )

edges = (
        (0,1),
        (0,2),
        (1,2),
        (0,3),
        (1,4),
        (2,5),
        (3,4),
        (3,5),
        (5,4)
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    glRotatef(0,0,0,0)

    while True:
    	for event in pygame.event.get():
    	    if event.type == pygame.QUIT:
    	        pygame.quit()
    	        quit()
	
    	glRotatef(1, 3, 1, 1)
    	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    	Cube()
    	pygame.display.flip()
    	pygame.time.wait(10)

main()