import pygame, sys
from pygame.locals import *
pygame.init()
WIDTH = 385
HEIGHT = 385
WINDOW = pygame.display.set_mode([WIDTH,HEIGHT])
CAPTION = pygame.display.set_caption('Test')
SCREEN = pygame.display.get_surface()
TRANSPARENT = pygame.Surface([WIDTH,HEIGHT])
TRANSPARENT.set_alpha(255)
TRANSPARENT.fill((255,255,255))
image = pygame.image.load('moon.png')
rect1 = pygame.draw.rect(SCREEN, (255, 255, 255), (0,0, 50, 50))
rect2 = pygame.draw.rect(SCREEN, (255, 255, 255), (0,55, 50, 50))
rect3 = pygame.draw.rect(SCREEN, (255, 255, 255), (55,0, 50, 50))
rect4 = pygame.draw.rect(SCREEN, (255, 255, 255), (55,55, 50, 50))
rect5 = pygame.draw.rect(SCREEN, (255, 255, 255), (110,0, 50, 50))
rect6 = pygame.draw.rect(SCREEN, (255, 255, 255), (110,55, 50, 50))
rect7 = pygame.draw.rect(SCREEN, (255, 255, 255), (165,0, 50, 50))
rect8 = pygame.draw.rect(SCREEN, (255, 255, 255), (165,55, 50, 50))
rect9 = pygame.draw.rect(SCREEN, (255, 255, 255), (220,0, 50, 50))
rect10 = pygame.draw.rect(SCREEN, (255, 255, 255), (220,55, 50, 50))
rect11 = pygame.draw.rect(SCREEN, (255, 255, 255), (275,0, 50, 50))
rect12 = pygame.draw.rect(SCREEN, (255, 255, 255), (275,55, 50, 50))
rect13 = pygame.draw.rect(SCREEN, (255, 255, 255), (330,0, 50, 50))
rect14 = pygame.draw.rect(SCREEN, (255, 255, 255), (330,55, 50, 50))
rect15 = pygame.draw.rect(SCREEN, (255, 255, 255), (385,0, 50, 50))
rect16 = pygame.draw.rect(SCREEN, (255, 255, 255), (385,55, 50, 50))

rectW11 = pygame.draw.rect(SCREEN, (255, 255, 255), (0,110, 50, 50))
rectW12 = pygame.draw.rect(SCREEN, (255, 255, 255), (0,165, 50, 50))
rectW13 = pygame.draw.rect(SCREEN, (255, 255, 255), (0,220, 50, 50))
rectW14 = pygame.draw.rect(SCREEN, (255, 255, 255), (0,275, 50, 50))
rectW15 = pygame.draw.rect(SCREEN, (255, 255, 255), (0,330, 50, 50))
rectW16 = pygame.draw.rect(SCREEN, (255, 255, 255), (0,385, 50, 50))

rectW21 = pygame.draw.rect(SCREEN, (255, 255, 255), (55,110, 50, 50))
rectW22 = pygame.draw.rect(SCREEN, (255, 255, 255), (55,165, 50, 50))
rectW23 = pygame.draw.rect(SCREEN, (255, 255, 255), (55,220, 50, 50))
rectW24 = pygame.draw.rect(SCREEN, (255, 255, 255), (55,275, 50, 50))
rectW25 = pygame.draw.rect(SCREEN, (255, 255, 255), (55,330, 50, 50))
rectW26 = pygame.draw.rect(SCREEN, (255, 255, 255), (55,385, 50, 50))

rectW31 = pygame.draw.rect(SCREEN, (255, 255, 255), (110,110, 50, 50))
rectW32 = pygame.draw.rect(SCREEN, (255, 255, 255), (110,165, 50, 50))
rectW33 = pygame.draw.rect(SCREEN, (255, 255, 255), (110,220, 50, 50))
rectW34 = pygame.draw.rect(SCREEN, (255, 255, 255), (110,275, 50, 50))
rectW35 = pygame.draw.rect(SCREEN, (255, 255, 255), (110,330, 50, 50))
rectW36 = pygame.draw.rect(SCREEN, (255, 255, 255), (110,385, 50, 50))

rectW41 = pygame.draw.rect(SCREEN, (255, 255, 255), (165,110, 50, 50))
rectW42 = pygame.draw.rect(SCREEN, (255, 255, 255), (165,165, 50, 50))
rectW43 = pygame.draw.rect(SCREEN, (255, 255, 255), (165,220, 50, 50))
rectW44 = pygame.draw.rect(SCREEN, (255, 255, 255), (165,275, 50, 50))
rectW45 = pygame.draw.rect(SCREEN, (255, 255, 255), (165,330, 50, 50))
rectW46 = pygame.draw.rect(SCREEN, (255, 255, 255), (165,385, 50, 50))

rectW51 = pygame.draw.rect(SCREEN, (255, 255, 255), (220,110, 50, 50))
rectW52 = pygame.draw.rect(SCREEN, (255, 255, 255), (220,165, 50, 50))
rectW53 = pygame.draw.rect(SCREEN, (255, 255, 255), (220,220, 50, 50))
rectW54 = pygame.draw.rect(SCREEN, (255, 255, 255), (220,275, 50, 50))
rectW55 = pygame.draw.rect(SCREEN, (255, 255, 255), (220,330, 50, 50))
rectW56 = pygame.draw.rect(SCREEN, (255, 255, 255), (220,385, 50, 50))

rectW61 = pygame.draw.rect(SCREEN, (255, 255, 255), (275,110, 50, 50))
rectW62 = pygame.draw.rect(SCREEN, (255, 255, 255), (275,165, 50, 50))
rectW63 = pygame.draw.rect(SCREEN, (255, 255, 255), (275,220, 50, 50))
rectW64 = pygame.draw.rect(SCREEN, (255, 255, 255), (275,275, 50, 50))
rectW65 = pygame.draw.rect(SCREEN, (255, 255, 255), (275,330, 50, 50))
rectW66 = pygame.draw.rect(SCREEN, (255, 255, 255), (275,385, 50, 50))

rectW71 = pygame.draw.rect(SCREEN, (255, 255, 255), (330,110, 50, 50))
rectW72 = pygame.draw.rect(SCREEN, (255, 255, 255), (330,165, 50, 50))
rectW73 = pygame.draw.rect(SCREEN, (255, 255, 255), (330,220, 50, 50))
rectW74 = pygame.draw.rect(SCREEN, (255, 255, 255), (330,275, 50, 50))
rectW75 = pygame.draw.rect(SCREEN, (255, 255, 255), (330,330, 50, 50))
rectW76 = pygame.draw.rect(SCREEN, (255, 255, 255), (330,385, 50, 50))

rectW81 = pygame.draw.rect(SCREEN, (255, 255, 255), (385,110, 50, 50))
rectW82 = pygame.draw.rect(SCREEN, (255, 255, 255), (385,165, 50, 50))
rectW83 = pygame.draw.rect(SCREEN, (255, 255, 255), (385,220, 50, 50))
rectW84 = pygame.draw.rect(SCREEN, (255, 255, 255), (385,275, 50, 50))
rectW85 = pygame.draw.rect(SCREEN, (255, 255, 255), (385,330, 50, 50))
rectW86 = pygame.draw.rect(SCREEN, (255, 255, 255), (385,385, 50, 50))


while True :
    WINDOW.blit(image, (0, 0))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        pygame.display.update() 
             




pygame.display.flip()

