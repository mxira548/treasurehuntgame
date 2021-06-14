import pygame 
import sys
import tkinter as tk
def close_windows():
    root.destroy()
pygame.init() 
size = (700,700)
startImg = pygame.image.load('gmesplshscreen.png')
screen = pygame.display.set_mode(size)
color = (255,28,28)
font = pygame.font.SysFont('calibri',30) 
color_light = (90,90,90)
color_light_1 = (170,170,170) 
color_dark = (255,100,255) 
fatness = screen.get_width() 
height = screen.get_height() 
def splshscren(x,y):
    gameDisplay.blit(startImg, (x,y))
x =  (height)
y = (fatness)
WINDOW = pygame.display.set_mode([fatness,height])
text = font.render(' START' , True , color)
text2 = font.render(' SETTINGS' , True , color)
text3 = font.render(' HOW TO PLAY' , True , color)
text4 = font.render(' EXIT' , True , color)
pos = pygame.mouse.get_pos()
while True:
    pos = pygame.mouse.get_pos()
    for i in pygame.event.get():
        pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pos()
        mouse1 = pygame.mouse.get_pos()
        mouse2 = pygame.mouse.get_pos() 
        if i.type == pygame.QUIT:
            pos = pygame.mouse.get_pos()
            pygame.quit()
            sys.exit()
        if i.type == pygame.mouse.get_pressed():
            pos = pygame.mouse.get_pos()
            if fatness/2.6 <= mouse[0] <= fatness/2.6+140 and height/2.4 <= mouse[1] <= height/2.4+40:
                pos = pygame.mouse.get_pos()
                print('click')
                exec(open('grid.py').read())
                print('click')
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if fatness/2.6 <= mouse2[0] <= fatness/2.6+140 and height/2 <= mouse2[1] <= height/2+40:
                pos = pygame.mouse.get_pos()
                print('ur nan')
        if i.type == pygame.MOUSEBUTTONDOWN:
            if fatness/2.6 <= mouse1[0] <= fatness/2.6+140 and height/1.8 <= mouse1[1] <= height/1.8+40:
                pos = pygame.mouse.get_pos()
                pygame.quit()
                sys.exit()

WINDOW.blit(startImg,(25,60)) 
mouse = pygame.mouse.get_pos()
  


if fatness/2.6 <= mouse[0] <= fatness/2.6+140 and height/2.4 <= mouse[1] <= height/2.4+40:
    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen,color_light_1,[fatness/2.5,height/2.4,140,40]) 

else:
    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen,color_light,[fatness/2.5,height/2.4,140,40]) 
#uzair btw blit requests pixels to buffer
screen.blit(text , (fatness/2.5+30,height/2.4)) 

pygame.display.update()
for ev in pygame.event.get():
    pos = pygame.mouse.get_pos()
      
    if ev.type == pygame.QUIT:
        pos = pygame.mouse.get_pos()
        pygame.quit()
          
    #checks if a mouse is clicked
    #if ev.type == pygame.MOUSEBUTTONDOWN:
          
        #if the mouse is clicked on the
        # button the game is terminated
        #if fatness/2 <= mouse[0] <= fatness/2+140 and height/2 <= mouse[1] <= height/2+40:
        #wot button will do goes here need to make splash
              

  
# stores the (x,y) coordinates into
# the variable as a tuple
    mouse = pygame.mouse.get_pos()
  
# if mouse is hovered on a button it
# changes to lighter shade 
if fatness/2.6 <= mouse2[0] <= fatness/2.6+140 and height/2 <= mouse2[1] <= height/2+40:
    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen,color_light_1,[fatness/2.5,height/2.05,140,40])
      
else:
    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen,color_light,[fatness/2.5,height/2.05,140,40])
  
# superimposing the text onto our button
screen.blit(text2 , (fatness/2.5+6,height/2))
  
# updates the frames of the game
pygame.display.update()
for v in pygame.event.get():
    pos = pygame.mouse.get_pos()
      
    if v.type == pygame.QUIT:
        pos = pygame.mouse.get_pos()
        pygame.quit()
          
    #checks if a mouse is clicked
    #if v.type == pygame.MOUSEBUTTONDOWN:
          
        #if the mouse is clicked on the
        # button the game is terminated
        #if fatness/2 <= mouse[0] <= fatness/2+140 and height/2 <= mouse[1] <= height/2+40:
        #wot button will do goes here need to make splash
              

  
# stores the (x,y) coordinates into
# the variable as a tuple
    mouse = pygame.mouse.get_pos()
  
# if mouse is hovered on a button it
# changes to lighter shade 
if fatness/2.6 <= mouse1[0] <= fatness/2.6+140 and height/1.8 <= mouse1[1] <= height/1.8+40:
    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen,color_light_1,[fatness/2.5,height/1.8,140,40])
  
else:
    pygame.draw.rect(screen,color_light,[fatness/2.5,height/1.8,140,40])
pos = pygame.mouse.get_pos()

if fatness/2.6 <= mouse1[0] <= fatness/2.6+140 and height/1.8 <= mouse1[1] <= height/1.8+40:
    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen,color_light_1,[fatness/2.5,height/1.8,140,40])
      
else:
    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen,color_light,[fatness/2.5,height/1.8,140,40])
  

pos = pygame.mouse.get_pos()
# superimposing the text onto our button
screen.blit(text3 , (fatness/2.8+6,height/1.8))
  
# updates the frames of the game
pygame.display.update()


    

