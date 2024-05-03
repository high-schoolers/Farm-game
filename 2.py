from time import *

global inventaire
inventaire = {
    'herbe': 100,
    
    'ble': 1,
    'mais': 1,
    'canne': 1,
    'soja': 1,
    
    
    'oeuf': 0,
    'lait': 0,
    'laine': 0,
    'abeille': 0,
    'lait_chevre': 0
    }

global dico_animaux
dico_animaux = {
    "vache" : ("lait",5),
    "poule" : ("oeuf",5),
    "mouton" : ("laine",5),
    "abeille" : ("miel",8),
    "chevre" : ("lait_chevre",5)
    }

class Produit:
    def __init__(self, nom, ingredient, nbingredient):
        self.nom = nom
        self.ingredient = ingredient
        self.qte = nbingredient
    
    def transfo(self):
        print("transformation de", self.ingredient, "en", self.nom, "en cours...")
        sleep(5)
        print(self.nom, "prêt!")
        
        if self.nom in inventaire and self.qte <= inventaire[self.ingredient]:
            inventaire[self.nom] += 1
            inventaire[self.ingredient] -= self.qte
        elif self.nom not in inventaire and self.qte <= inventaire[self.ingredient]:
            inventaire[self.nom] = 1
            inventaire[self.ingredient] -= self.qte
        print(inventaire)

class Animaux:
    def __init__(self,nom):
        self.nom = nom
        self.produit = dico_animaux[nom][0]
        self.temps = dico_animaux[nom][1]


    def produire(self):
        if inventaire["herbe"] > 0 :
            inventaire["herbe"] -= 1
            print(self.nom,"a été nourri")
            print("Production de",self.produit,"en cours...")
            sleep(self.temps)
            print(self.produit,"prêt !")
        else :
            print("Plus d'herbe pour nourrir l'animal !")
        

    def recuperer(self):
        if self.produit in inventaire :
            inventaire[self.produit] += 1
        else :
            inventaire[self.produit] = 1
            print(self.produit,"récupéré !")

class Champ:
    def __init__(self):
        self.crop = None
        self.vide = True

    def plantation(self, crop):
        if inventaire[crop] == 0:
            print("Quantité insuffisante.")
            return False
        elif self.vide == False:
            print("Champ déjà occupé.")
            return False
        else:
            self.crop = crop
            self.vide = False
            inventaire[crop] -=1
            print(crop,'planté!')

        sleep(10)

        inventaire[crop] += 2
        self.crop = None
        self.vide = False
        print(crop,'récolté!')
            
pain = Produit('pain', 'ble', 2)
popcorn = Produit('popcorn', 'mais', 4)
sucre = Produit('sucre', 'canne', 2)
steak_soja = Produit('steak_soja', 'soja', 5)

omelette = Produit('omelette', 'oeuf', 2)
beurre = Produit('beurre', 'lait', 1)
pull = Produit('pull', 'laine', 3)
bonbons = Produit('bonbons', 'miel', 2)
fromage_chevre = Produit('fromage_chevre', 'lait_chevre', 2)

vache = Animaux('vache')
poule = Animaux('poule')
mouton = Animaux('mouton')
abeille = Animaux('abeille')
chevre = Animaux('chevre')

champ1 = Champ()
champ2 = Champ()
champ3 = Champ()
champ4 = Champ()
champ5 = Champ()
champ6 = Champ()
