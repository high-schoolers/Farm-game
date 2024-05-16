## Version sans interface

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
    'lait_chevre': 0,
    'pomme' : 0
    }
    
global dico_animaux
dico_animaux = {
    "vache" : ("lait",5),
    "poule" : ("oeuf",5),
    "mouton" : ("laine",5),
    "abeille" : ("miel",8),
    "chevre" : ("lait_chevre",5),
    "pommier" : ("pomme",5)
    }

global dico_arbres
dico_arbres = {
    "pommier" :("pomme",5),
    "oranger" : ("orange",6),
    "cerisier" : ("cerise",8)
    }

class Produit:
    def __init__(self, nom, ingredient, nbingredient):
        self.nom = nom
        self.ingredient = ingredient
        self.qte = nbingredient
    
    def transfo(self):
        """Transforme des ressources d'animal ou des plantes en un produit

        Paramètre:
        ----------
        self = instance de la classe Produit
        """
        if self.qte <= inventaire[self.ingredient] :
            print("Transformation de", self.ingredient, "en", self.nom, "en cours...")
            sleep(5)
            print(self.nom, "prêt!")
            
            if self.nom in inventaire :
                inventaire[self.nom] += 1
                inventaire[self.ingredient] -= self.qte
            elif self.nom not in inventaire :
                inventaire[self.nom] = 1
                inventaire[self.ingredient] -= self.qte
            print(inventaire)
        else :
            print("Pas assez de",self.ingredient,"pour produire",self.nom)


class Arbres:
    def __init__(self,nom,etat = 0):
        self.nom = nom
        self.fruit = dico_arbres[nom][0]
        self.temps = dico_arbres[nom][1]

    def pousser(self):
        """Faire pousser les fruits de l'arbre

        Paramètre
        ---------
        self : instance de la classe Arbre
        """
        print("Pousse de",self.fruit,"en cours...")
        sleep(self.temps)
        print(self.fruit,"récoltée !")
        if self.fruit in inventaire :
            inventaire[self.fruit] += 1
        else :
            inventaire[self.fruit] = 1


class Animaux:
    def __init__(self,nom,etat = 0):
        self.nom = nom
        self.produit = dico_animaux[nom][0]
        self.temps = dico_animaux[nom][1]
        self.etat = etat
        # etat : 0 si affamé, 1 si en production, 2 si produit prêt                   
        
    def produire(self):
        """Nourrir l'animal et changer son état après quelques secondes

        Paramètre
        ---------
        self : instance de de la classe Animaux
        """
        if self.etat == 0 :
            if inventaire["herbe"] > 0 :
                inventaire["herbe"] -= 1
                print(self.nom,"a été nourri")
                self.etat = 1
                print("Production de",self.produit,"en cours...")
                sleep(self.temps)
                print(self.produit,"prêt !")
                self.etat = 2
                
            else :
                print("Plus d'herbe pour nourrir l'animal !")
                
        elif self.etat == 2 :
            print("Veuillez d'abord récupérer",self.produit)
        

    def recuperer(self):
        """Récupérer le produit de l'animal

        Paramètre
        ---------
        self : instance de la classe Animaux
        """
        if self.etat == 2 :
            if self.produit in inventaire :
                inventaire[self.produit] += 1
            else :
                inventaire[self.produit] = 1
            print(self.produit,"récupéré !")
            self.etat = 0
        else :
            print("Pas de produit à récupérer")

class Champ:
    def __init__(self):
        self.crop = None
        self.vide = True

    def plantation(self, crop):
        """Plante la graine choisie dans le champ

        Paramètres
        ----------
        self : instance de la classe Champ
        crop : str
            la plante choisie
        """
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
            print(crop,'planté !')

        sleep(5)
        if crop in inventaire :
            inventaire[crop] += 2
        else :
            inventaire[crop] = 2
        self.crop = None
        self.vide = False
        print(crop,'récolté !')

# Initialisation des instances

# Les différents produits et les ingrédients nécesssaires
pain = Produit('pain', 'ble', 2)
popcorn = Produit('popcorn', 'mais', 4)
sucre = Produit('sucre', 'canne', 2)
steak_soja = Produit('steak_soja', 'soja', 5)

omelette = Produit('omelette', 'oeuf', 2)
beurre = Produit('beurre', 'lait', 1)
pull = Produit('pull', 'laine', 3)
bonbons = Produit('bonbons', 'miel', 2)
fromage_chevre = Produit('fromage_chevre', 'lait_chevre', 2)
jus_pomme = Produit('jus_pomme', 'pomme', 4)
jus_orange = Produit("jus_pomme","orange",3)

# Les animaux
vache = Animaux('vache')
poule = Animaux('poule')
mouton = Animaux('mouton')
abeille = Animaux('abeille')
chevre = Animaux('chevre')

# Les arbres fruitiers
pommier = Arbres('pommier')
oranger = Arbres('oranger')
cerisier = Arbres("cerisier")

# Les champs
champ1 = Champ()
champ2 = Champ()
champ3 = Champ()
champ4 = Champ()
champ5 = Champ()
champ6 = Champ()

# Démonstration
"""
print(inventaire)
champ1.plantation("ble")
champ2.plantation("ble")
pain.transfo()
sleep(2)
print()

for i in range(2):
    chevre.produire()
    chevre.recuperer()
fromage_chevre.transfo()
sleep(2)
print()

vache.produire()
vache.recuperer()
beurre.transfo()
sleep(2)
print()

jus_pomme.transfo()
"""




