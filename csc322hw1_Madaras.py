### 
### Adopted from https://stackabuse.com/brief-introduction-to-opengl-in-python-with-pyopengl/
### CSC 322 Fall 2020

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0
width,height= 500,500 			# window size

def drawSquare(x,y,width,height):
 glBegin(GL_QUADS) 			# start drawing a square
 glVertex2f(x,y) 			# bottom left point
 glVertex2f(x + width,y)		# bottom right point
 glVertex2f(x + width,y + height)	# top right point
 glVertex2f(x, y + height)		# top left point
 glEnd()				# done drawing

def drawTriangle(x,y,width,height):
 glBegin(GL_TRIANGLES)
 glVertex2f(x,y)
 glVertex2f(x + width/2,y + height)
 glVertex2f(x + width,y)
 glEnd()

def drawScene():
 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 	# clear the screen
 glLoadIdentity() 					# reset position
 refresh2d(width, height)

 glColor3f(0.0,0.0,1.0) 				# set color to blue 
 drawSquare(50,50,200,200) 				# draw a square at (50,50) with width 200, height 200
 
 glColor3f(1.0,0.0,0.0) 				# set color to red
 drawTriangle(25,250,250,100) 				# draw a triangle at (300,50)

 glColor3f(0.0,1.0,0.0)
 drawSquare(125,50,50,80)

 glColor3f(1.0,0.0,0.0)
 drawSquare(200,250,50,100)

 glutSwapBuffers() # important for double buffering

def refresh2d(width, height):
 glViewport(0,0, width, height)
 glMatrixMode(GL_PROJECTION)
 glLoadIdentity()
 glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
 glMatrixMode (GL_MODELVIEW)
 glLoadIdentity()


# initialization
glutInit() 							#initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(width, height) 				#set window size
glutInitWindowPosition(0, 0) 					#set window position
wind = glutCreateWindow("CSC 322 Fall 2020 HW1") 		#create window with title
glutDisplayFunc(drawScene) 						#set showScreen function callback
glutIdleFunc(drawScene) 						#draw all the time
glutMainLoop() 							#start everything
