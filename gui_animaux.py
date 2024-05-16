from time import *
import pygame

global inventaire
inventaire = {"herbe" : 10, "argent" : 200}

global dico_animaux
dico_animaux = {"vache" : ("lait",2), "poule" : ("oeuf",3),
                "mouton" : ("laine",4), "abeille" : ("miel",8),
                "chevre" : ("lait_chevre",3), "pommier" : ("pomme",2)}

pygame.init()
largeur = pygame.display.Info().current_w
hauteur = pygame.display.Info().current_h

ecran = pygame.display.set_mode([largeur,hauteur-60])
pygame.display.set_caption("jour du foin") 
ecran.fill((68, 189, 32))
pygame.display.flip()
img_enclos = pygame.image.load("enclos.png").convert_alpha()
img_crayon = pygame.image.load("crayon.png").convert_alpha()
img_crayon = pygame.transform.scale(img_crayon,(25,25))
img_poule = pygame.image.load("poule.png").convert_alpha()
img_poule2 = pygame.image.load("poule_oeuf.png").convert_alpha()
img_vache = pygame.image.load("vache.png").convert_alpha()
img_vache2 = pygame.image.load("vache_lait.png").convert_alpha()
img_mouton = pygame.image.load("mouton.png").convert_alpha()
img_mouton2 = pygame.image.load("mouton_laine.png").convert_alpha() 
img_ruche = pygame.image.load("ruche.png").convert_alpha()
img_ruche2 = pygame.image.load("ruche_miel.png").convert_alpha() 
img_chevre = pygame.image.load("chevre.png").convert_alpha()
img_chevre2 = pygame.image.load("chevre_lait.png").convert_alpha()

img_arbre = pygame.image.load("arbre.png").convert_alpha()
img_pommier = pygame.image.load("pommier.png").convert_alpha()

#img_pommier = pygame.transform.scale(img_pommier,(175,175))

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
        #self.velocity = 5

    def update(self,events):
        for event in events :
            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.rect.collidepoint(event.pos):
                    if self.etat == 0 :
                        self.produire()
                    elif self.etat == 2 :
                        self.recuperer()
                        
    def deplacer(self):
        pass

        
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
            if self.nom == "abeille" or self.nom == "pommier":
                ecran.fill((68, 189, 32),self.rect)
            else :
                ecran.fill((255,255,255),self.rect)
            self.image = self.img1
            self.rect = self.image.get_rect()
            self.rect.center = self.centre
        else :
            print("Pas de produit à récupérer")

def modifier(sprites):
    events = pygame.event.get()
    for event in events :
        if event.type == pygame.MOUSEBUTTONDOWN :
            if sprite.rect.collidepoint(event.pos):
                rect.move_ip(event.rel)

ecran.blit(img_enclos,(25,25))
ecran.blit(img_enclos,(25,225))
ecran.blit(img_enclos,(25,425))
ecran.blit(img_enclos,(250,225))
ecran.blit(img_crayon,(25,615))

all_sprites = pygame.sprite.Group()
p1 = Animaux("poule",img_poule,img_poule2,(80,80))
p2 = Animaux("poule",img_poule,img_poule2,(175,160))
p3 = Animaux("poule",img_poule,img_poule2,(80,160))
p4 = Animaux("poule",img_poule,img_poule2,(175,80))

v1 = Animaux("vache",img_vache,img_vache2,(165,285))
v2 = Animaux("vache",img_vache,img_vache2,(85,350))

m1 = Animaux("mouton",img_mouton,img_mouton2,(75,475))
m2 = Animaux("mouton",img_mouton,img_mouton2,(175,500))
m3 = Animaux("mouton",img_mouton,img_mouton2,(75,550))

a1 = Animaux("abeille",img_ruche,img_ruche2,(300,75))
a2 = Animaux("abeille",img_ruche,img_ruche2,(300,175))

c1 = Animaux("chevre",img_chevre,img_chevre2,(300,275))

pommier1 = Animaux("pommier",img_arbre,img_pommier,(410,120))

all_sprites.add(p1,p2,p3,p4,v1,v2,m1,m2,m3,a1,a2,c1,pommier1)
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
        """
        elif event.type == pygame.MOUSEBUTTONDOWN :
            position = pygame.mouse.get_pos()
            rect = img_crayon.get_rect()
            if rect.x <= position[0] <= rect.x+rect.width:
                print("oui")
                if rect.y <= position[1] <= rect.y+rect.height:
                    print("Mode modification")
                    modifier(all_sprites)
                else :
                    print("non")
            
            if img_crayon.get_rect().collidepoint(event.pos):
                print("Mode modification")
                modifier(all_sprites)
        """

    all_sprites.update(events)
    all_sprites.draw(ecran)
    pygame.display.flip()


pygame.quit()

    




















            
        
