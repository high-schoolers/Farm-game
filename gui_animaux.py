from time import *
import pygame

global inventaire
inventaire = {"herbe" : 10}

global dico_animaux
dico_animaux = {"vache" : ("lait",2), "poule" : ("oeuf",3),
                "mouton" : ("laine",3)}

pygame.init()
largeur = pygame.display.Info().current_w
hauteur = pygame.display.Info().current_h

ecran = pygame.display.set_mode([largeur,hauteur-60])
pygame.display.set_caption("jour du foin") 
ecran.fill((68, 189, 32))
pygame.display.flip()
img_poule = pygame.image.load("poule.png").convert_alpha()
img_poule2 = pygame.image.load("poule_oeuf.png").convert_alpha()
img_enclos = pygame.image.load("enclos.png").convert_alpha()
img_vache = pygame.image.load("vache.png").convert_alpha()
img_vache2 = pygame.image.load("vache_lait.png").convert_alpha()

class Animaux(pygame.sprite.Sprite):
    def __init__(self,nom,img,img2,centre,etat = 0):
        self.nom = nom
        self.produit = dico_animaux[nom][0]
        self.temps = dico_animaux[nom][1]
        self.etat = etat
        self.img1 = img
        self.img2 = img2
        self.centre = centre
        # etat : 0 si affamé, 1 si en production, 2 si produit prêt
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = centre
        self.velocity = 5

    def update(self,events):
        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.rect.collidepoint(event.pos):
                    if self.etat == 0 :
                        self.produire()
                    elif self.etat == 2 :
                        self.recuperer()
        
    def produire(self):
        if self.etat == 0 :
            if inventaire["herbe"] > 0 :
                inventaire["herbe"] -= 1
                print(self.nom,"a été nourri")
                self.etat = 1
                print("Production de",self.produit,"en cours...")
                sleep(self.temps)
                print(self.produit,"prêt !")
                self.etat = 2
                self.image = self.img2
                self.rect = self.image.get_rect()
                self.rect.center = self.centre
                
            else :
                print("Plus d'herbe pour nourrir l'animal !")
                
        elif self.etat == 2 :
            print("Veuillez d'abord récupérer",self.produit)
        

    def recuperer(self):
        if self.etat == 2 :
            if self.produit in inventaire :
                inventaire[self.produit] += 1
            else :
                inventaire[self.produit] = 1
            print(self.produit,"récupéré !")
            self.etat = 0
            ecran.fill((255,255,255),self.rect)
            self.image = self.img1
            self.rect = self.image.get_rect()
            self.rect.center = self.centre
        else :
            print("Pas de produit à récupérer")

ecran.blit(img_enclos,(50,50))
ecran.blit(img_enclos,(50,200))
ecran.blit(img_enclos,(50,350))

all_sprites = pygame.sprite.Group()
p1 = Animaux("poule",img_poule,img_poule2,(100,100))
p2 = Animaux("poule",img_poule,img_poule2,(150,150))
v1 = Animaux("vache",img_vache,img_vache2,(125,275))
all_sprites.add(p1)
all_sprites.add(p2)
all_sprites.add(v1)
all_sprites.draw(ecran)
pygame.display.flip()

running = True

while running :

    events = pygame.event.get()
    
    for event in events :
        
        if event.type == pygame.QUIT :
            # si on touche la petite croix
            pygame.quit()
            running = False
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # si on appuie sur la touche echap
            pygame.quit()
            running = False

    all_sprites.update(events)
    all_sprites.draw(ecran)
    pygame.display.flip()


pygame.quit()

    




















            
        
