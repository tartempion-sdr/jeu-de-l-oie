import pygame
import random
import time
from grille import Grille
from sounds import SoundManager
pygame.init()
# cree une class qui representera notre joueur

class Joueur(pygame.sprite.Sprite):
    
    
    
    def __init__(self):
        super().__init__()
        self.nomjoueur = ""
        
        # self.grille = list
        self.valeurdude_joueur1 = 0
        self.valeurdude_joueurIA = 0

        self.score = 0        
        self.screen = pygame.display.set_mode((850,567))
        self.position1 = 0
        self.positionIA = 0

        self.cestaujoueur1dejouer = True
        
        
        self.sound_manager = SoundManager()

        self.image_joueur1 = pygame.image.load("assets/blanc-chess-mini.png")
        self.rect_joueur1 = self.image_joueur1.get_rect()
        self.rect_joueur1.x = 18
        self.rect_joueur1.y = 22

        self.image_joueurIA = pygame.image.load("assets/noir-chess-mini.png")
        self.rect_joueurIA = self.image_joueurIA.get_rect()
        self.rect_joueurIA.x = 48
        self.rect_joueurIA.y = 22

        self.acceuil = True
        self.running = False
        self.findepartie = False
        
    


    def entrez_votre_nom(self):
        
 
        clock = pygame.time.Clock()
        font = pygame.font.SysFont('Comic Sans MS,Arial',18)
        entrezvotreprenom = font.render("ENTREZ VOTRE PRENOM :" ,True ,(0,0,0),(255,255,255))
        prompt_rect = entrezvotreprenom.get_rect()
        prompt_rect.x = 0
        prompt_rect.y = 0
        user_input_value = ""
        user_input = font.render(user_input_value, True, (0,0,0), (255,255,255))
        user_input_rect = user_input.get_rect()
        user_input_rect.x = 0
        user_input_rect.y = 20

        continuer = True
         
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        continuer = False
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        user_input_value = user_input_value[:-1]
                    else:
                        if len(user_input_value) <= 9:
                            user_input_value += event.unicode
                    user_input = font.render(user_input_value, True, (0,0,0), (255,255,255))
                    user_input_rect.x = 0
                    user_input_rect.y = 40

            clock.tick(30)
        
            
            
            self.screen.blit(entrezvotreprenom, prompt_rect)
            self.screen.blit(user_input, user_input_rect)
            pygame.display.flip()
        
        print("Vous Vous appellez: ", str(user_input_value))
        self.nomjoueur = user_input_value
        #pygame.quit()

    def printrandom1(self):  

        de = int(random.randint(1, 6))
        deresultat = de 
        self.valeurdude_joueur1 = deresultat
        self.score += self.valeurdude_joueur1
        self.sound_manager.play("de")
        print("votre score est de: ", self.score)
    
    def deplacementdupion1(self):
        
        self.position1 += self.valeurdude_joueur1
        self.rect_joueur1.x = Grille[self.position1][1] 
        self.rect_joueur1.y = Grille[self.position1][2]
        time.sleep(1)
        self.sound_manager.play("pion")
          
    def colision1(self):
        
        if self.position1 == self.positionIA and self.positionIA != 0:
            
            print("1de ", int(self.valeurdude_joueur1))
            self.positionIA -= self.valeurdude_joueur1
            print("2de ",int(self.valeurdude_joueur1))
            self.rect_joueurIA.x = Grille[self.positionIA][1] + 30
            self.rect_joueurIA.y = Grille[self.positionIA][2] 
            time.sleep(1)
            self.sound_manager.play("pion")
            
    def reverif1(self):

        
         
        # out of range > 
        if self.position1 == 69:
            
            time.sleep(1)
            self.position1  = 63 - ((63 -(self.position1 - self.valeurdude_joueur1)))
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            self.sound_manager.play("pion")

        # out of range > 
        if self.position1 == 68:
            
            time.sleep(1)
            self.position1  = 63 - ((63 -(self.position1 - (self.valeurdude_joueur1 - 1))))
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            self.sound_manager.play("pion")

        # out of range > 
        if self.position1 == 67:
            
            time.sleep(1)
            self.position1   = 63 - ((63 -(self.position1 - (self.valeurdude_joueur1 - 1))))
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            self.sound_manager.play("pion")
                
        # out of range > 
        if self.position1 == 66:
            
            time.sleep(1)
            self.position1  = 63 - ((63 -(self.position1 - (self.valeurdude_joueur1 - 1))))
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]

        # out of range > 
        if self.position1 == 65:
            
            time.sleep(1)
            self.position1  = 63 - ((63 -(self.position1 - (self.valeurdude_joueur1 - 1))))
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]

        # out of range > 
        if self.position1 == 64:
            
            time.sleep(1)
            self.position1 = 63 - ((63 -(self.position1 - (self.valeurdude_joueur1 - 1))))
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]

        if self.position1 == 63:
            print("JOUEUR1 A GAGNER !!!!!!")
            
            self.sound_manager.play("pion")
            self.running = False
            self.findepartie = True
            

        if self.position1 == 62:
            
            time.sleep(3)
            self.position1 = 40
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]

        # out of range > 
        

        if self.position1 == 58:
            
            time.sleep(3)
            self.position1 = 0
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]

        if self.position1 == 46:
            
            time.sleep(3)
            self.position1 = 54
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]

        if self.position1 == 42:
            
            time.sleep(3)
            self.position1 = 30
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]

        if self.position1 == 36:
            
            time.sleep(3)
            self.position1 += self.valeurdude_joueur1
            self.sound_manager.play("oie")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]

        if self.position1 == 27:
            
            time.sleep(3)
            self.position1 = 57
            self.sound_manager.play("pion")     
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]

        if self.position1 == 26:
            
            time.sleep(3)
            self.position1 += self.valeurdude_joueur1
            self.sound_manager.play("oie")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]

        if self.position1 == 8:
            
            time.sleep(3)
            self.position1 += self.valeurdude_joueur1
            self.sound_manager.play("oie")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2]
            
      


    def printrandomIA(self):
        deIA = int(random.randint(1, 6))
        deresultatIA = deIA 
        self.valeurdude_joueurIA = deresultatIA
        time.sleep(0.5)
        self.sound_manager.play("de")
         
    def deplacementdupionIA(self): 
        
        self.positionIA += self.valeurdude_joueurIA
        self.rect_joueurIA.x = Grille[self.positionIA][1] +30
        self.rect_joueurIA.y = Grille[self.positionIA][2]
        time.sleep(1)
        self.sound_manager.play("pion")
        
    def colisionIA(self):
        
        if self.positionIA == self.position1 and self.position1 != 0:
            
          
            self.position1 -= self.valeurdude_joueurIA
            
            self.sound_manager.play("pion")
            self.rect_joueur1.x = Grille[self.position1][1] 
            self.rect_joueur1.y = Grille[self.position1][2] 
            time.sleep(1)
            
    def revefifIA(self):
            
            
       

        # out of range > 
        if self.positionIA == 69:
            
            time.sleep(1)
            self.positionIA  = 63 - ((63 -(self.positionIA - self.valeurdude_joueurIA))- 1)
            print(str(63 - ((63 -(self.positionIA - self.valeurdude_joueurIA))- 1)))
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("pion")

        # out of range > 
        if self.positionIA == 68:
            
            time.sleep(1)
            self.positionIA  = 63 - ((63 -(self.positionIA - self.valeurdude_joueurIA))- 1)
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("pion")

        # out of range > 
        if self.positionIA == 67:
            
            time.sleep(1)
            self.positionIA  = 63 - ((63 -(self.positionIA - self.valeurdude_joueurIA))- 1)
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("pion")
                
        # out of range > 
        if self.positionIA == 66:
            
            time.sleep(1)
            self.positionIA  = 63 - ((63 -(self.positionIA - self.valeurdude_joueurIA))- 1)
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("pion")

        # out of range > 
        if self.positionIA == 65:
            
            time.sleep(1)
            self.positionIA = 63 - ((63 -(self.positionIA - self.valeurdude_joueurIA))- 1)
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("pion")

        # out of range > 
        if self.positionIA == 64:
            
            time.sleep(1)
            self.positionIA = 63 - ((63 -(self.positionIA - self.valeurdude_joueurIA))- 1)
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("pion")

        if self.positionIA == 63:
            print("JOUEUR-IA A GAGNER !!!!!!")
            #acceuil = True
            self.sound_manager.play("pion")
            self.findepartie = True
            self.running = False

        if self.positionIA == 62:
            
            time.sleep(1)
            self.positionIA = 40
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("pion")

         

        if self.positionIA == 58:
            
            time.sleep(1)
            self.positionIA = 0
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("pion")

        if self.positionIA == 46:
            
            time.sleep(1)
            self.positionIA = 54
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("pion")

        if self.positionIA == 42:
            
            time.sleep(1)
            self.positionIA = 30
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("pion")
        
        if self.positionIA == 36:
           
            time.sleep(1)
            self.positionIA += self.valeurdude_joueurIA
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("oie")

        if self.positionIA == 27:
            
            time.sleep(1)
            self.positionIA = 57
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("pion")
        
        if self.positionIA == 26:
            
            time.sleep(1)
            self.positionIA += self.valeurdude_joueurIA
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("oie")

        if self.positionIA == 8:
            
            time.sleep(1)
            self.positionIA += self.valeurdude_joueurIA
            self.rect_joueurIA.x = Grille[self.positionIA][1] 
            self.rect_joueurIA.y = Grille[self.positionIA][2]
            self.sound_manager.play("oie")

    

        
   
