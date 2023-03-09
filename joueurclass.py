import pygame
import random
import time
from grille import Grille
from sounds import SoundManager
#from game import Game
# cree une class qui representera notre joueur

class Joueur(pygame.sprite.Sprite):
    
    
    def __init__(self):
        super().__init__()
        # self.nomjoueur = ""
        
        # self.grille = list
        self.valeurdude_joueur1 = 0
        self.valeurdude_joueurIA = 0
        self.position1 = 0
        self.positionIA = 0
        
        self.sound_manager = SoundManager()

        self.image_joueur1 = pygame.image.load("assets/blanc-chess-mini.png")
        self.rect_joueur1 = self.image_joueur1.get_rect()
        
        self.rect_joueur1.x = 18
        self.rect_joueur1.y = 22
        
        
        

        self.image_joueurIA = pygame.image.load("assets/noir-chess-mini.png")
        self.rect_joueurIA = self.image_joueurIA.get_rect()
        self.rect_joueurIA.x = 48
        self.rect_joueurIA.y = 22


    def entrez_votre_nom(self):
        
        while self.nomjoueur == str(""):
       
            self.nomjoueur = input("veuillez entrer votre nom : ")
            if self.nomjoueur != str(""):
                print("Vous Vous appellez : " + self.nomjoueur)
                print("\n" + self.nomjoueur + " appuyer sur la touche a pour lancé le dé\n")
    
    
  

    def printrandom1(self):  

        de = int(random.randint(1, 6))
        deresultat = de 
        self.valeurdude_joueur1 = deresultat
        self.sound_manager.play("de")
        time.sleep(0.5)

    def deplacementdupion1(self):
        
        self.position1 += self.valeurdude_joueur1
        self.rect_joueur1.x = Grille[self.position1][1] 
        self.rect_joueur1.y = Grille[self.position1][2]
        time.sleep(1)
        self.sound_manager.play("pion")

    def redeplacementdupion1(self):

        self.rect_joueur1.x = Grille[self.position1][1] 
        self.rect_joueur1.y = Grille[self.position1][2]
        time.sleep(1)
        self.sound_manager.play("pion")


    def printrandomIA(self):
        deIA = int(random.randint(1, 6))
        deresultatIA = deIA 
        self.valeurdude_joueurIA = deresultatIA
        self.sound_manager.play("de")
        time.sleep(0.5)
             
    def deplacementdupionIA(self): 
        
        self.positionIA += self.valeurdude_joueurIA
        self.rect_joueurIA.x = int(Grille[self.positionIA][1]) +30
        self.rect_joueurIA.y = Grille[self.positionIA][2]
        time.sleep(1)
        self.sound_manager.play("pion")

    def redeplacementdupionIA(self):   

        self.rect_joueurIA.x = int(Grille[self.positionIA][1]) +30
        self.rect_joueurIA.y = Grille[self.positionIA][2]
        time.sleep(1)
        self.sound_manager.play("pion")    