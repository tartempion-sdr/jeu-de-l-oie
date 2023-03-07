import pygame
import random
# cree une class qui representera notre joueur

class Joueur1(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        # self.nomjoueur = ""
        # self.position = int()
        # self.grille = list
        self.valeurdude = int()
        self.image = pygame.image.load("assets/blanc-chess-mini.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        # -57 pour la hauteur du sprite car c'est calculer du coin droite en haut du sprit
        self.rect.y = 567-57


    def entrez_votre_nom(self):
        
        while self.nomjoueur == str(""):
       
            self.nomjoueur = input("veuillez entrer votre nom : ")
            if self.nomjoueur != str(""):
                print("Vous Vous appellez : " + self.nomjoueur)
                print("\n" + self.nomjoueur + " appuyer sur la touche a pour lancé le dé\n")
    
    
  

    def printrandom(self):
            
        de = int(random.randint(1, 6))
        deresultat = de
        self.valeurdude = deresultat
        print(self.valeurdude)
        return deresultat 
                
       
       
    def deplacementdupion(self):

        print(type(self.rect.x))
        print(type(self.valeurdude))
        self.rect.x += 5 *  self.valeurdude
                
    





