import pygame
from pygame.locals import*

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

champ = pygame.image.load("D:\Terminale NSI\Jour_du_Foin\\champs.png").convert()
maïs = pygame.image.load("D:\Terminale NSI\\maïs.png").convert()

rect = maïs.get_rect()
rect.center = WIDTH//2, HEIGHT//2
rect2 = maïs.get_rect()
rect.center = WIDTH//2, HEIGHT//2

def bouger(event,rect):
    pass
    
pygame.display.flip()
run = True
moving = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    screen.fill((255,255,255))
    screen.blit(maïs,rect)

    pygame.display.update()

pygame.quit()
