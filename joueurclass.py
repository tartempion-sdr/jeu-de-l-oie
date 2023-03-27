import pygame
import random
from grille import Grille
from sounds import SoundManager
import csv
import pandas



de0 = "assets/dés/de.png"   
de1 = "assets/dés/64px-Dice-1-b.svg.png"
de2 = "assets/dés/64px-Dice-2-b.svg.png"
de3 = "assets/dés/64px-Dice-3-b.svg.png"
de4 = "assets/dés/64px-Dice-4-b.svg.png"
de5 = "assets/dés/64px-Dice-5-b.svg.png"
de6 = "assets/dés/64px-Dice-6-b.svg.png"

depart =       pygame.image.load("assets/plateau/depart.png")            
oie =          pygame.image.load("assets/plateau/oiecase.png")
prison =       pygame.image.load("assets/plateau/prison.png")
hotel =        pygame.image.load("assets/plateau/hotel.png") 
labyrinth =    pygame.image.load("assets/plateau/labyrinth.png")
puit =         pygame.image.load("assets/plateau/puit.png")
tetedemort =   pygame.image.load("assets/plateau/tetedemort.png")
arriver =      pygame.image.load("assets/plateau/arriver.png")
basechelle2 =  pygame.image.load("assets/plateau/basechelle2.png") 
longechelle1 = pygame.image.load("assets/plateau/longechelle1.png")
pattedoie1 =       pygame.image.load("assets/plateau/pattedoie1.png") 
pattedoie2 =       pygame.image.load("assets/plateau/pattedoie2.png") 
pattedoie3 =       pygame.image.load("assets/plateau/pattedoie3.png") 
pattedoie4 =       pygame.image.load("assets/plateau/pattedoie4.png") 




# cree une class qui representera notre joueur
class Joueur(pygame.sprite.Sprite):
    
    
    
    def __init__(self):
        super().__init__()

        self.screen = pygame.display.set_mode((850,567)) 
        self.nomjoueur = ""
       
        self.hotelj1 = 0
        self.hoteljIA = 0
        
        self.valeurdude_joueur1 = 0
        self.valeurdude_joueurIA = 0

        self.score = 0  
         
        self.backgroundAcceuil = pygame.image.load("assets/verdure850x567.jpg")
        self.backgroundfin = pygame.image.load("assets/verdure850x567.png")
        self.pictureAcceuil = pygame.image.load("assets/oie2.jpeg")
        self.messageAcceuil = pygame.image.load("assets/message-acceuil.png")
        self.jouez = pygame.image.load("assets/jouez.png")
        self.regles = pygame.image.load("assets/regles.png")
        self.reglestexte = pygame.image.load("assets/regles-texte2.png")
        self.carreblanc = pygame.image.load("assets/carre-blanc.png")
        
        
        self.background = pygame.image.load("assets/plateau/beige.png")
        self.deListe = [de0, de1, de2, de3, de4, de5, de6] 
        self.casedup = pygame.Surface(size = (53, 53))
         
        self.decliquable = pygame.image.load("assets/dés/de.png")

        self.findepartiegagner = pygame.image.load("assets/findepartiegagner.jpg")
        self.findepartieperdu = pygame.image.load("assets/findepartieperdu.jpg")
        self.picturerecommencer = pygame.image.load("assets/recommencer.jpg")
        
        self.caseliste = {8:oie, 19:hotel, 26:oie, 27:basechelle2, 31:puit, 36:oie, 42:labyrinth, 46:basechelle2, 52:prison, 58:tetedemort, 62:basechelle2}


        self.position1 = 0
        self.positionIA = 0
        self.pionBlanc = pygame.image.load("assets/plateau/blanc-chess-mini.png")
        self.pionNoir = pygame.image.load("assets/plateau/noir-chess-mini.png")

        self.joueur1peutjouer = True
        self.joueurIApeutjouer = False
        
        self.sauvegarde = True
        
        self.sound_manager = SoundManager()

        self.image_joueur1 = pygame.image.load("assets/plateau/blanc-chess-mini.png")
        self.rect_joueur1 = self.image_joueur1.get_rect()
        self.rect_joueur1.x =  Grille[self.position1][1] 
        self.rect_joueur1.y = Grille[self.position1][2] 

        self.image_joueurIA = pygame.image.load("assets/plateau/noir-chess-mini.png")
        self.rect_joueurIA = self.image_joueurIA.get_rect()
        self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
        self.rect_joueurIA.y = Grille[self.positionIA][2] 

        self.recommencer = True
        self.acceuil = True
        self.running = False
        self.findepartie = False
        

    def toutAfficher(self):
            # - generer dé, pion, face123456

            

            mous = pygame.cursors.load_xbm("assets/dés/de.xbm", "assets/dés/de-mask.xbm")
            sablier = pygame.cursors.load_xbm("assets/dés/sablier.xbm", "assets/dés/sablier-mask.xbm")
            pygame.display.set_caption("  jeu de l'oie")

            if self.joueur1peutjouer  == True:
                        
                pionAQuiLeTour = self.pionBlanc
                pygame.mouse.set_cursor(*mous)
            else:
                pionAQuiLeTour = self.pionNoir
                pygame.mouse.set_cursor(*sablier)

            faceDuDejoueur1 = pygame.image.load(self.deListe[self.valeurdude_joueur1])

            faceDuDejoueurIA = pygame.image.load(self.deListe[self.valeurdude_joueurIA])
            
            # plateau et case affichage...
            beige = (225,210,184)
            blanc = (250,250,250)
            self.screen.fill(beige)

            #self.screen.blit(self.background, (0,0))
            for caseplateau in range(0,64):
                
                
                
                pygame.draw.rect(self.screen, blanc, pygame.Rect(Grille[caseplateau][1], Grille[caseplateau][2], 57, 54))
            
                font = pygame.font.SysFont('Comic Sans MS,Arial',18)
                numcaseplateau = font.render(str(Grille[caseplateau][0]) ,True ,(0,0,0),(255,255,255))
                numcaseplateau_rect = numcaseplateau.get_rect()
                numcaseplateau_rect.x = Grille[caseplateau][1]
                numcaseplateau_rect.y = Grille[caseplateau][2]
                self.screen.blit(numcaseplateau, numcaseplateau_rect)

            for caseplateauoie in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 62) :

                casepattedoie_rect = pattedoie1.get_rect()
                casepattedoie_rect.x = Grille[caseplateauoie][1]
                casepattedoie_rect.y = Grille[caseplateauoie][2]
                self.screen.blit(pattedoie1, casepattedoie_rect)
                
            for caseplateauoie in (13, 14, 15, 16, 17, 18, 19, 46, 49, 50, 51):

                casepattedoie_rect = pattedoie1.get_rect()
                casepattedoie_rect.x = Grille[caseplateauoie][1]
                casepattedoie_rect.y = Grille[caseplateauoie][2]
                self.screen.blit(pattedoie2, casepattedoie_rect)

                
            for caseplateauoie in (20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 53, 54, 55, 56, 57, 58, 59, 60):

                casepattedoie_rect = pattedoie1.get_rect()
                casepattedoie_rect.x = Grille[caseplateauoie][1]
                casepattedoie_rect.y = Grille[caseplateauoie][2]
                
                self.screen.blit(pattedoie3, casepattedoie_rect)

            for caseplateauoie in (27, 33, 34, 35, 36, 37, 61, 62):

                casepattedoie_rect = pattedoie1.get_rect()
                casepattedoie_rect.x = Grille[caseplateauoie][1]
                casepattedoie_rect.y = Grille[caseplateauoie][2]
                
                self.screen.blit(pattedoie4, casepattedoie_rect)    

            self.screen.blit(depart,        (18, 22))
            self.screen.blit(oie,          (514, 22))
            self.screen.blit(hotel,       (763, 429))
            self.screen.blit(oie,         (390, 488))                
            self.screen.blit(basechelle2, (328, 429))
            self.screen.blit(puit,         (80, 488))                
            self.screen.blit(oie,          (18, 256))             
            self.screen.blit(labyrinth,   (266, 139))     
            self.screen.blit(longechelle1,(514, 197))
            self.screen.blit(prison,      (638, 372))
            self.screen.blit(tetedemort,  (266, 372))                
            self.screen.blit(basechelle2, (142, 197))
            self.screen.blit(arriver,     (204, 256))
            
           


            # case spéciale!
            if int(self.position1) in (8, 19, 26, 27, 31, 36, 42, 46, 52, 58, 62):
                #print(caseliste[8])
                casespeciale1 = self.caseliste[self.position1]
                self.screen.blit(casespeciale1,(452,258))
                

            if self.positionIA in (8, 19, 26, 27, 31, 36, 42, 46, 52, 58, 62):

                casespecialeIA = self.caseliste[self.positionIA]
                self.screen.blit(casespecialeIA,(452,315))
           
            if self.hotelj1 == 1 or self.hotelj1 == 2 :
                
                front3 =  pygame.font.SysFont('Comic Sans MS,Arial',39)
                casehotel1 = front3.render(str(self.hotelj1), True ,(0,0,0),(255,255,255))
                casehotel1_rect1 = casehotel1.get_rect()
                casehotel1_rect1.x = 426
                casehotel1_rect1.y = 258
                self.screen.blit(casehotel1, casehotel1_rect1)

            if self.hoteljIA == 1 or self.hoteljIA == 2 : 

                front3 =  pygame.font.SysFont('Comic Sans MS,Arial',39)
                casehotelIA = front3.render(str(self.hoteljIA), True ,(0,0,0),(255,255,255))
                casehotelIA_rect1 = casehotelIA.get_rect()
                casehotelIA_rect1.x = 426
                casehotelIA_rect1.y = 315
                self.screen.blit(casehotelIA, casehotelIA_rect1)

            # nom du joueur1, valeur du dé
            font = pygame.font.SysFont('Comic Sans MS,Arial',15)
            votreprenom = font.render("  " + self.nomjoueur + " votre score est de: " + str(self.score), True ,(0,0,0),(255,255,255))
            prompt_rect = votreprenom.get_rect()
            prompt_rect.x = 266
            prompt_rect.y = 197
            self.screen.blit(votreprenom, prompt_rect)
            
            # police et taille
            front2 =  pygame.font.SysFont('Comic Sans MS,Arial',39)

            # affiche n°case pour joueur1
            case1 = front2.render(str(self.position1), True ,(0,0,0),(255,255,255))
            case_rect1 = case1.get_rect()
            case_rect1.x = 266
            case_rect1.y = 256
            self.screen.blit(case1, case_rect1)

             # affiche n°case pour joueurIA
            case2 = front2.render(str(self.positionIA), True ,(0,0,0),(255,255,255))
            case_rect2 = case2.get_rect()
            case_rect2.x = 266
            case_rect2.y = 314
            self.screen.blit(case2, case_rect2)
            
            
           
        
            # applique l'image de mon joueur1  !!!!!! 

            self.screen.blit(self.image_joueur1, self.rect_joueur1)
            
            self.screen.blit(self.image_joueurIA, self.rect_joueurIA)
            
            # pion qui indique les des
            self.screen.blit(self.pionBlanc,(390,258))
            self.screen.blit(self.pionNoir,(390,315))
            
            #pion a qui le tour
            self.screen.blit(pionAQuiLeTour,(18,82))
            #de cliquable , pas encors
            self.screen.blit(self.decliquable,(80,82))

            #des
            self.screen.blit(faceDuDejoueur1,(328,256))
            self.screen.blit(faceDuDejoueurIA,(328,314))

            

            #mettre à jour l'arriere plan    
            pygame.display.update()      


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
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            
    def verif1(self):

        
        
        # out of range > 
        if self.position1 == 69:
            
            pygame.time.delay(1000)
            self.position1  = 63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2] 
            self.toutAfficher()

           
        if self.position1 == 68:
            
            pygame.time.delay(1000)
            self.position1  =  63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2] 
            self.toutAfficher()
        
        if self.position1 == 67:
            
            pygame.time.delay(1000)
            self.position1   =  63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2] 
            self.toutAfficher()
       
        if self.position1 == 66:
            
            pygame.time.delay(1000)
            self.position1  =  63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2] 
            self.toutAfficher()

        if self.position1 == 65: 

            pygame.time.delay(1000)
            self.position1  =  63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2] 
            self.toutAfficher()

        if self.position1 == 64:

            pygame.time.delay(1000)
            self.position1 =  63 - (self.position1 - 63)
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2] 
            self.toutAfficher()

        if self.position1 == 63:

            pygame.time.delay(1000)
            print("JOUEUR1 A GAGNER !!!!!!") 
            self.sound_manager.play("pion")
            self.running = False
            self.findepartie = True
            self.toutAfficher()

        if self.position1 == 62:
            
            pygame.time.delay(1000)
            self.position1 = 40
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2] 
            self.toutAfficher()

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
            
    def casespeciale1(self):
        # regle pour joueur1 casespeciale
        if 19 == self.positionIA or 31 == self.positionIA or 52 == self.positionIA :

            self.joueurIApeutjouer = False
            self.joueur1peutjouer = True
            print("interdit a jIA de jouer tout seul ") 

        if 19 == self.positionIA :
            self.hoteljIA += 1
            print("jIA " + str(self.hoteljIA) + " jour d hotel")
            
            front3 =  pygame.font.SysFont('Comic Sans MS,Arial',39)
            casehotelIA = front3.render(str(self.hoteljIA), True ,(0,0,0),(255,255,255))
            casehotelIA_rect1 = casehotelIA.get_rect()
            casehotelIA_rect1.x = 473
            casehotelIA_rect1.y = 315
            self.screen.blit(casehotelIA, casehotelIA_rect1)

        if self.hoteljIA > 2 :
            self.joueurIApeutjouer = True
            self.hotelj1 = 0
            print("jIA est partis de l hotel")
        
        
        # regle pour joueurIA casespeciale 31 == 31 et 52 == 52
        if  31 == self.position1 and 31 == self.positionIA :

            self.joueur1peutjouer = False
            self.joueurIApeutjouer = True

            pygame.time.delay(500)         
            self.printrandomIA()
            pygame.time.delay(1000)
            self.deplacementdupionIA()
            self.toutAfficher()
            print("jIA est sortie du puit")

        if  52 == self.position1 and 52 == self.positionIA :
            
            self.joueur1peutjouer = False
            self.joueurIApeutjouer = True

            pygame.time.delay(500)         
            self.printrandomIA()
            pygame.time.delay(1000)
            self.deplacementdupionIA()
            self.toutAfficher()

            print("jIA est sortie de prison")

        if  19 == self.position1 and 19 == self.positionIA :
            
            self.joueur1peutjouer = False
            self.joueurIApeutjouer = True
            self.hoteljIA = 0
            print("jIA est partis de l hotel sans payer")
            


    def printrandomIA(self):

        deIA = int(random.randint(1, 6))
        deresultatIA = deIA 
        self.valeurdude_joueurIA = deresultatIA
        self.sound_manager.play("de")
              
    def deplacementdupionIA(self): 

        
        self.positionIA += self.valeurdude_joueurIA
        self.sound_manager.play("pion")
        self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
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
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            self.toutAfficher()

        # out of range > 
        if self.positionIA == 68:
            
            pygame.time.delay(1000)
            self.positionIA  =  63 - (self.positionIA - 63)
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            self.toutAfficher()

        # out of range > 
        if self.positionIA == 67:
            
            pygame.time.delay(1000)
            self.positionIA  =  63 - (self.positionIA - 63)
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            self.toutAfficher()
            

        # out of range > 
        if self.positionIA == 66:
            
            pygame.time.delay(1000)
            self.positionIA  =  63 - (self.positionIA - 63)
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            self.toutAfficher()

        # out of range > 
        if self.positionIA == 65:
            
            pygame.time.delay(1000)
            self.positionIA =  63 - (self.positionIA - 63)
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            self.toutAfficher()

        # out of range > 
        if self.positionIA == 64:
            
            pygame.time.delay(1000)
            self.positionIA =  63 - (self.positionIA - 63)
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            self.toutAfficher()

        if self.positionIA == 63:

            pygame.time.delay(1000)
            print("JOUEUR-IA A GAGNER !!!!!!")
            #acceuil = True
            self.sound_manager.play("pion")
            self.findepartie = True
            self.running = False
            self.toutAfficher()

        if self.positionIA == 62:
            
            pygame.time.delay(1000)
            self.positionIA = 40
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            self.toutAfficher()
         

        if self.positionIA == 58:
            

            pygame.time.delay(1000)
            self.joueurIApeutjouer = False
            self.joueur1peutjouer = True
            self.positionIA = 0
            self.sound_manager.play("mort")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            
        if self.position1 == 52:

            pygame.time.delay(1000)
            self.sound_manager.play("prison")

        if self.positionIA == 46:
            
            pygame.time.delay(1000)
            self.positionIA = 54
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            
        if self.positionIA == 42:
            
            pygame.time.delay(1000)
            self.positionIA = 30
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            

        if self.positionIA == 36:
           
            pygame.time.delay(1000)
            self.positionIA += self.valeurdude_joueurIA
            self.sound_manager.play("oie")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            
        if self.positionIA == 31:

            pygame.time.delay(1000)
            self.sound_manager.play("plouf")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 

        if self.positionIA == 27:
            
            pygame.time.delay(1000)
            self.positionIA = 57
            self.sound_manager.play("pion")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            
        

        if self.positionIA == 26:
            
            pygame.time.delay(1000)
            self.positionIA += self.valeurdude_joueurIA
            self.sound_manager.play("oie")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            

        if self.positionIA == 19:

            pygame.time.delay(1000)     
            self.sound_manager.play("hotel")

        if self.positionIA == 8:
            
            pygame.time.delay(1000)
            self.positionIA += self.valeurdude_joueurIA
            self.sound_manager.play("oie")
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 28
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            
    def casescpecialeIA(self):

    # regle pour joueurIA casespeciale
                        
            
        if 19 == self.position1 or 31 == self.position1 or 52 == self.position1 :

        
            self.joueur1peutjouer = False
            self.joueurIApeutjouer = True
            print("interdit a j1 de jouer tout seul") 

        if 19 == self.position1 :
            self.hotelj1 += 1
            print("j1 " + str(self.hotelj1) + " jour d hotel")
            
            front3 =  pygame.font.SysFont('Comic Sans MS,Arial',39)
            casehotel1 = front3.render(str(self.hotelj1), True ,(0,0,0),(255,255,255))
            casehotel1_rect1 = casehotel1.get_rect()
            casehotel1_rect1.x = 473
            casehotel1_rect1.y = 258
            self.screen.blit(casehotel1, casehotel1_rect1)

        if self.hotelj1 > 2 :

            self.joueur1peutjouer = True
            self.hotelj1 = 0
            print("j1 est partis de l hotel")

        # regle pour joueur1 casespeciale 31 == 31 et 52 == 52
        if  31 == self.position1 and 31 == self.positionIA :

            self.joueur1peutjouer = True
            self.joueurIApeutjouer = False
            print("j1 est sortie du puit")

        if  52 == self.position1 and 52 == self.positionIA :
            
            self.joueur1peutjouer = True
            self.joueurIApeutjouer = False
            print("j1 est sortie de prison")

        if  19 == self.position1 and 19 == self.positionIA :
            
            self.joueur1peutjouer = True
            self.joueurIApeutjouer = False
            self.hotelj1 = 0
            print("j1 est partis de l hotel sans payer")

        