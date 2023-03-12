import pygame
import random
import time
from grille import Grille
from sounds import SoundManager

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
        self.cestaquidejouer = True  
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

    def deplacementdupion1(self):
        
        self.position1 += self.valeurdude_joueur1
        self.rect_joueur1.x = Grille[self.position1][1] 
        self.rect_joueur1.y = Grille[self.position1][2]
        time.sleep(1)
        self.sound_manager.play("pion")

    def collision1(self):
        
        # Celui qui est rejoint par un autre joueur sur la même case devra se rendre sur la case ou l’autre joueur se situait avant de jouer.      
    
        self.positionIA -= self.valeurdude_joueur1
        
        print("ok")

    def reverif1(self):
        
        # out of range > 
        if self.position1 == 69:
            self.position1 -= self.valeurdude_joueur1 -5
            

        # out of range > 
        if self.position1 == 68:
            self.position1 -= self.valeurdude_joueur1 -4
            

        # out of range > 
        if self.position1 == 67:
            self.position1 -= self.valeurdude_joueur1 -3
            
                
        # out of range > 
        if self.position1 == 66:
            self.position1 -= self.valeurdude_joueur1 -2
            
                
        # out of range > 
        if self.position1 == 65:
            self.position1 -= self.valeurdude_joueur1 -1
            
                
        # out of range > 
        if self.position1 == 64:
            self.position1 -= self.valeurdude_joueur1 
            
                
        if self.position1 == 63:
            print("l'IA HALLL 9000 A GAGNER !!!!!!")
            #acceuil = True

        if self.position1 == 62:
            self.position1 = 40
            
        if self.position1 == 58:
            self.position1 = 0
            

        if self.position1 == 46:
            self.position1 = 54
            

        if self.position1 == 42:
            self.position1 = 30
            


        if self.position1 == 36:
            self.position1 += self.valeurdude_joueur1
            

        if self.position1 == 27:
            self.position1 = 57
                 

        if self.position1 == 26:
            self.position1 += self.valeurdude_joueur1
            

        if self.position1 == 8:
            self.position1 += self.valeurdude_joueur1
                            
    def redeplacementdupion1(self):
        self.rect_joueur1.x = Grille[self.position1][1] 
        self.rect_joueur1.y = Grille[self.position1][2]
        #time.sleep(1)
        #self.sound_manager.play("pion")



    def printrandomIA(self):
        deIA = int(random.randint(1, 6))
        deresultatIA = deIA 
        self.valeurdude_joueurIA = deresultatIA
        time.sleep(0.5)
        self.sound_manager.play("de")
         
    def deplacementdupionIA(self): 
        
        self.positionIA += self.valeurdude_joueurIA
        self.rect_joueurIA.x = int(Grille[self.positionIA][1]) +30
        self.rect_joueurIA.y = Grille[self.positionIA][2]
        time.sleep(1)
        self.sound_manager.play("pion")

    def collisionIA(self):
        # Celui qui est rejoint par un autre joueur sur la même case devra se rendre sur la case ou l’autre joueur se situait avant de jouer.      
        
           
        self.position1 -= self.valeurdude_joueurIA
        
        print("ok")

    def revefifIA(self):
            
            
        
       
        
        # out of range >
        if self.positionIA == 69:
            self.positionIA -= self.valeurdude_joueurIA -5
            
        # out of range >
        if self.positionIA == 68:
            self.positionIA -= self.valeurdude_joueurIA -4
            
        
        # out of range >
        if self.positionIA == 67:
            self.positionIA -= self.valeurdude_joueurIA -3
            

        # out of range > 
        if self.positionIA == 66:
            self.positionIA -= self.valeurdude_joueurIA -2
            self.redeplacementdupionIA()

        # out of range > 
        if self.positionIA == 65:
            self.positionIA -= self.valeurdude_joueurIA -1
            self.redeplacementdupionIA()    

        if self.positionIA == 64:
            self.positionIA -= self.valeurdude_joueurIA 
            self.redeplacementdupionIA()            

        if self.positionIA == 63:
            print("vous avez GAGNER !!!!!!")
            #acceuil = True
        
        if self.positionIA == 62:
            self.positionIA = 40
            self.redeplacementdupionIA()

        if self.positionIA == 58:
            self.positionIA = 0
            self.redeplacementdupionIA()

        if self.positionIA == 46:
            self.positionIA = 8
            self.redeplacementdupionIA()

        if self.positionIA == 42:
            self.positionIA = 30
            self.redeplacementdupionIA()

        if self.positionIA == 62:
            self.positionIA = 40
            self.redeplacementdupionIA()

        if self.positionIA == 36:
            self.positionIA += self.valeurdude_joueurIA
            self.redeplacementdupionIA()


        if self.positionIA == 27:
            self.positionIA = 57
            self.redeplacementdupionIA()

        if self.positionIA == 26:
            self.positionIA += self.valeurdude_joueurIA
            self.redeplacementdupionIA()

        if self.positionIA == 8:
            self.positionIA += self.valeurdude_joueurIA
            self.redeplacementdupionIA()
        
    def redeplacementdupionIA(self):   

        self.rect_joueurIA.x = int(Grille[self.positionIA][1]) +30
        self.rect_joueurIA.y = Grille[self.positionIA][2]
        
        #self.sound_manager.play("pion")    
        