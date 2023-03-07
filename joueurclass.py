import pygame
import random
import time
#from game import Game
# cree une class qui representera notre joueur

class Joueur(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        # self.nomjoueur = ""
        # self.position = int()
        # self.grille = list
        self.valeurdude_joueur1 = int()
        self.valeurdude_joueurIA = int()
        

        self.image_joueurIA = pygame.image.load("assets/noir-chess-mini.png")
        self.rect_joueurIA = self.image_joueurIA.get_rect()
        self.rect_joueurIA.x = 0
        self.rect_joueurIA.y = 567-57


        self.image_joueur1 = pygame.image.load("assets/blanc-chess-mini.png")
        self.rect_joueur1 = self.image_joueur1.get_rect()
        self.rect_joueur1.x = 57
        # -57 pour la hauteur du sprite car c'est calculer du coin droite en haut du sprit
        self.rect_joueur1.y = 567-57


    def entrez_votre_nom(self):
        
        while self.nomjoueur == str(""):
       
            self.nomjoueur = input("veuillez entrer votre nom : ")
            if self.nomjoueur != str(""):
                print("Vous Vous appellez : " + self.nomjoueur)
                print("\n" + self.nomjoueur + " appuyer sur la touche a pour lancé le dé\n")
    
    
  

    def printrandom(self):
            
        de = int(random.randint(1, 6))
        deresultat = de
        
        
        self.valeurdude_joueur1 = deresultat
        #print(self.valeurdude_joueur1)
        

        deIA = int(random.randint(1, 6))
        deresultatIA = deIA 
         
        self.valeurdude_joueurIA = deresultatIA
        #print(self.valeurdude_joueurIA)
        
            
       
       
    def deplacementdupion(self):

        
        self.rect_joueur1.x += 5 *  self.valeurdude_joueur1
        
        self.rect_joueurIA.x += 5 *  self.valeurdude_joueurIA
    





