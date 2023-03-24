import pygame
import random

from grille import Grille
from sounds import SoundManager
import csv
import pandas

# cree une class qui representera notre joueur

class Joueur(pygame.sprite.Sprite):
    
    
    
    def __init__(self):
        super().__init__()
        self.nomjoueur = ""
       
        self.hotelj1 = 0
        self.hoteljIA = 0

        self.valeurdude_joueur1 = 0
        self.valeurdude_joueurIA = 0

        self.score = 0  
         

        
        self.position1 = 0
        self.positionIA = 0
        self.pionBlanc = pygame.image.load("assets/blanc-chess-mini.png")
        self.pionNoir = pygame.image.load("assets/noir-chess-mini.png")

        self.joueur1peutjouer = True
        self.joueurIApeutjouer = False
        
        self.sauvegarde = True
        
        self.sound_manager = SoundManager()

        self.image_joueur1 = pygame.image.load("assets/blanc-chess-mini.png")
        self.rect_joueur1 = self.image_joueur1.get_rect()
        self.rect_joueur1.x =  Grille[self.position1][1]
        self.rect_joueur1.y = Grille[self.position1][2]

        self.image_joueurIA = pygame.image.load("assets/noir-chess-mini.png")
        self.rect_joueurIA = self.image_joueurIA.get_rect()
        self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
        self.rect_joueurIA.y = Grille[self.positionIA][2]

        self.recommencer = True
        self.acceuil = True
        self.running = False
        self.findepartie = False
        

   


    def enregisterScore(self):

        
        enTete = ["nomjoueur", "score"]

        with open("in_score.csv", "w") as fichier_in: 

            writer = csv.writer(fichier_in, delimiter=",")
            writer.writerow(enTete)
            lignescore = [self.nomjoueur]+[str(self.score)]  
            writer.writerow(lignescore)

            
        with open("out_score.csv", "a") as fichier_out: 

            fichier_in = open('in_score.csv') 
            reader = csv.DictReader(fichier_in, delimiter=",")
            writer2 = csv.writer(fichier_out, delimiter=",")
            for line in reader:
  
                writer2.writerow([line["nomjoueur"]]+[line["score"]])
            
        df = pandas.read_csv("out_score.csv", sep=",")
        df1 = df.sort_values(by=['score'], ascending=True)
        df1.to_csv("out_score_ordre_croissant.csv")
        
            
    def printrandom1(self):  

        de = int(random.randint(1, 6))
        deresultat = de       
        self.valeurdude_joueur1 = deresultat
        self.score += self.valeurdude_joueur1
        self.sound_manager.play("de")
       
    def deplacementdupion1(self):

        
        self.position1 += self.valeurdude_joueur1
        self.sound_manager.play("pion") 
        self.rect_joueur1.x = Grille[self.position1][1] 
        self.rect_joueur1.y = Grille[self.position1][2]
        print("de : " + str(self.valeurdude_joueur1) + " joueur1 case : " + str(self.position1)) 
           
    def colision1(self):
        
        if self.position1 == self.positionIA and self.position1 != 0:
            pygame.time.delay(1000)
            self.sound_manager.play("pion")
            self.positionIA -= self.valeurdude_joueur1
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            
    def verif1(self):

        
        
        # out of range > 
        if self.position1 == 69:
            
            pygame.time.delay(1000)
            self.position1  = 63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            

           
        if self.position1 == 68:
            
            pygame.time.delay(1000)
            self.position1  =  63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            
        
        if self.position1 == 67:
            
            pygame.time.delay(1000)
            self.position1   =  63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
           
       
        if self.position1 == 66:
            
            pygame.time.delay(1000)
            self.position1  =  63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            
        if self.position1 == 65: 

            pygame.time.delay(1000)
            self.position1  =  63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            

        if self.position1 == 64:

            pygame.time.delay(1000)
            self.position1 =  63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            

        if self.position1 == 63:

            pygame.time.delay(1000)
            print("JOUEUR1 A GAGNER !!!!!!") 
            self.sound_manager.play("pion")
            self.running = False
            self.findepartie = True
            

        if self.position1 == 62:
            
            pygame.time.delay(1000)
            self.position1 = 40
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            

        if self.position1 == 58:
            
            pygame.time.delay(1000)
            self.joueur1peutjouer = False
            self.joueurIApeutjouer = True
            self.position1 = 0
            self.sound_manager.play("mort")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            
        if self.position1 == 52:
            
            pygame.time.delay(1000)
            self.sound_manager.play("prison")

        if self.position1 == 46:

            pygame.time.delay(1000)
            self.position1 = 54
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            

        if self.position1 == 42:
            pygame.time.delay(1000)
            self.position1 = 30
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            

        if self.position1 == 36:
            
            pygame.time.delay(1000)
            self.position1 += self.valeurdude_joueur1
            self.sound_manager.play("oie")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            

        if self.position1 == 31:
            
            pygame.time.delay(1000)
            self.sound_manager.play("plouf")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]

        if self.position1 == 27:

            pygame.time.delay(1000)
            self.position1 = 57
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            

            
                 
            

        if self.position1 == 26:
            
            pygame.time.delay(1000)
            self.position1 += self.valeurdude_joueur1
            self.sound_manager.play("oie")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            
        if self.position1 == 19:
            
            pygame.time.delay(1000)
            self.sound_manager.play("hotel")
        
        if self.position1 == 8:
            
            pygame.time.delay(1000)
            self.position1 += self.valeurdude_joueur1
            self.sound_manager.play("oie")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            
            


    def printrandomIA(self):

        deIA = int(random.randint(1, 6))
        deresultatIA = deIA 
        self.valeurdude_joueurIA = deresultatIA
        self.sound_manager.play("de")
              
    def deplacementdupionIA(self): 

        
        self.positionIA += self.valeurdude_joueurIA
        self.sound_manager.play("pion")
        self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
        self.rect_joueurIA.y = Grille[self.positionIA][2] 
        print("de : " + str(self.valeurdude_joueurIA)+ " joueurIA case : " + str(self.positionIA))
        
    def colisionIA(self):


        if self.positionIA == self.position1 and self.position1 != 0:
            pygame.time.delay(1000)    
            self.position1 -= self.valeurdude_joueurIA
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2] 
                   
    def vefifIA(self):
            
        
        # out of range > 
        if self.positionIA == 69:
            
            pygame.time.delay(1000)
            self.positionIA  =  63 - (self.positionIA - 63)
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            

        # out of range > 
        if self.positionIA == 68:
            
            pygame.time.delay(1000)
            self.positionIA  =  63 - (self.positionIA - 63)
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
           

        # out of range > 
        if self.positionIA == 67:
            
            pygame.time.delay(1000)
            self.positionIA  =  63 - (self.positionIA - 63)
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            
            

        # out of range > 
        if self.positionIA == 66:
            
            pygame.time.delay(1000)
            self.positionIA  =  63 - (self.positionIA - 63)
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            

        # out of range > 
        if self.positionIA == 65:
            
            pygame.time.delay(1000)
            self.positionIA =  63 - (self.positionIA - 63)
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            

        # out of range > 
        if self.positionIA == 64:
            
            pygame.time.delay(1000)
            self.positionIA =  63 - (self.positionIA - 63)
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            

        if self.positionIA == 63:

            pygame.time.delay(1000)
            print("JOUEUR-IA A GAGNER !!!!!!")
            #acceuil = True
            self.sound_manager.play("pion")
            self.findepartie = True
            self.running = False

        if self.positionIA == 62:
            
            pygame.time.delay(1000)
            self.positionIA = 40
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            
         

        if self.positionIA == 58:
            

            pygame.time.delay(1000)
            self.joueurIApeutjouer = False
            self.joueur1peutjouer = True
            self.positionIA = 0
            self.sound_manager.play("mort")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            
        if self.position1 == 52:

            pygame.time.delay(1000)
            self.sound_manager.play("prison")

        if self.positionIA == 46:
            
            pygame.time.delay(1000)
            self.positionIA = 54
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            
        if self.positionIA == 42:
            
            pygame.time.delay(1000)
            self.positionIA = 30
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            

        if self.positionIA == 36:
           
            pygame.time.delay(1000)
            self.positionIA += self.valeurdude_joueurIA
            self.sound_manager.play("oie")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            
        if self.positionIA == 31:

            pygame.time.delay(1000)
            self.sound_manager.play("plouf")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]

        if self.positionIA == 27:
            
            pygame.time.delay(1000)
            self.positionIA = 57
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            
        

        if self.positionIA == 26:
            
            pygame.time.delay(1000)
            self.positionIA += self.valeurdude_joueurIA
            self.sound_manager.play("oie")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            

        if self.positionIA == 19:

            pygame.time.delay(1000)     
            self.sound_manager.play("hotel")

        if self.positionIA == 8:
            
            pygame.time.delay(1000)
            self.positionIA += self.valeurdude_joueurIA
            self.sound_manager.play("oie")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            
   
