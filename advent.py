#!/usr/bin/python3
import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
<<<<<<< HEAD
=======
from energenie import switch_on, switch_off
>>>>>>> 42aea1da50644bbb020b88f1633701f8a4c6d338
import io
import socket
import struct
from PIL import Image
import string
import pygame.gfxdraw

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()

pygame.display.set_caption("DeskMate2000")

#define function that checks for mouse location
def on_click():
	click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
	#now check to see if refresh  was pressed
	
	date_list=[3,11,23,1,16,13,6,10,21,17,22,12,24,15,5,4,18,9,8,19,14,7,20,2]
	xcord_list=[30,155,280,405,530,655,30,155,280,405,530,655,30,155,280,405,530,655,30,155,280,405,530,655]
	ycord_list=[20,20,20,20,20,20,105,105,105,105,105,105,190,190,190,190,190,190,275,275,275,275,275,275]

	for i in range(len(xcord_list)):
		date=date_list[i]
		x=xcord_list[i]
		y=ycord_list[i]
		if x <= click_pos[0] <= x+100  and y <= click_pos[1] <=y+60:
			button(date)

def make_button(text, xpo, ypo, colour):
	font=pygame.font.Font(None,24)
	label=font.render(str(text), 1, (colour))
	#pygame.draw.rect(screen, cream, (xpo,ypo,100,60),0)
	pygame.gfxdraw.box(screen, pygame.Rect(xpo,ypo,100,60),(254,255,250,127))
	screen.blit(label,(xpo+45,ypo+20))


#define action on pressing buttons
def button(number):
	pygame.draw.rect(screen, black, (390,390,100,50),0)
	pygame.display.update()
	font=pygame.font.Font(None,24)
	label=font.render(str(number), 1, (cream))
	screen.blit(label,(400,400))
	image = '/home/pi/Documents/advent/photos/' + str(number) + '.tiff'
	new_image = pygame.image.load(image)
	screen.blit(new_image,(0,0))
	pygame.display.update()
	time.sleep(5)
	refresh()

#Add buttons and labels

def refresh():

	background ='/home/pi/Documents/advent/photos/bg.tiff'
	bg = pygame.image.load(background)
	screen.blit(bg,(0,0))
	pygame.display.update()
	date_list=[3,11,23,1,16,13,6,10,21,17,22,12,24,15,5,4,18,9,8,19,14,7,20,2]
	xcord_list=[30,155,280,405,530,655,30,155,280,405,530,655,30,155,280,405,530,655,30,155,280,405,530,655]
	ycord_list=[20,20,20,20,20,20,105,105,105,105,105,105,190,190,190,190,190,190,275,275,275,275,275,275]

	for i in range(len(xcord_list)):
		date=date_list[i]
		x=xcord_list[i]
		y=ycord_list[i]
		make_button(date,x,y,red)


#set size of the screen
size = width, height = 800, 480

#define colours
blue = 26, 0, 255
cream = 254, 255, 250
cream2 = 254,255,250,0
black = 0, 0, 0
white = 255, 255, 255
red = 255,0,0
green = 0,255,0
yellow = 255, 255, 224

screen = pygame.display.set_mode(size)
pygame.display.set_mode((800,480),pygame.FULLSCREEN)

#set up the fixed items on the menu
screen.fill(blue) #change the colours if needed
pygame.draw.rect(screen, white, (0,5,799,475),1)
pygame.display.update()

refresh()

#While loop to manage touch screen inputs
while 1:

        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                        on_click()

        #ensure there is always a safe way to end the program if the touch screen fails

                if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                                sys.exit()
        pygame.display.update()
refresh_menu_screen()  #refresh the menu interface


main()