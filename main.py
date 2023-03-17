import pygame
import random
from joueurclass import Joueur

import time
from grille import Grille
pygame.init()


# future icone
pygame_icon = pygame.image.load("assets/oie-icon.png")
pygame.display.set_icon(pygame_icon)

# titre
pygame.display.set_caption("  jeu de l'oie")
# generer la fenetre de notre jeu




backgroundAcceuil = pygame.image.load("assets/verdure850x567.png")
pictureAcceuil = pygame.image.load("assets/oie2.jpeg")
messageAcceuil = pygame.image.load("assets/message-acceuil.png")
jouez = pygame.image.load("assets/jouez.png")
regles = pygame.image.load("assets/regles.png")
reglestexte = pygame.image.load("assets/regles-texte.png")

background = pygame.image.load("assets/verdure-rogner2-850x567.png")

# - generer dé, pion, face123456

de0 = "assets/de.png"   
de1 = "assets/64px-Dice-1-b.svg.png"
de2 = "assets/64px-Dice-2-b.svg.png"
de3 = "assets/64px-Dice-3-b.svg.png"
de4 = "assets/64px-Dice-4-b.svg.png"
de5 = "assets/64px-Dice-5-b.svg.png"
de6 = "assets/64px-Dice-6-b.svg.png"
deListe = [de0, de1, de2, de3, de4, de5, de6] 
    

decliquable = pygame.image.load("assets/de.png")

# charger joueur

joueur = Joueur()

joueur.screen   
        
pygame.mouse.set_cursor(*pygame.cursors.arrow)

# entrez votre nom

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


while joueur.acceuil :
 
    jouezcliq = pygame.Rect((0, 240),(216, 44))
    reglescliq = pygame.Rect((0, 284),(216, 44))
    picturecliq = pygame.Rect((0, 333),(215, 234))

    # appliquer a l'arriere plan de notre jeu
    joueur.screen.blit(backgroundAcceuil,(0,0))
    joueur.screen.blit(pictureAcceuil,(0,333))
    joueur.screen.blit(messageAcceuil,(0,188))
    joueur.screen.blit(jouez,(0,236))
    joueur.screen.blit(regles,(0,284))

    
    pygame.display.set_caption("  acceuil")
    
    
 
        # si le joueur clic , le joueur passe au jeu
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            if event.type == pygame.QUIT:
                    pygame.quit()
                    break
            
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                
                if len(user_input_value)< 1:
                    print("vous n'avez rien ecrit banane !")
                else: 
                    joueur.acceuil = False
                    joueur.running = True

                break    
                
            if event.key == pygame.K_BACKSPACE:
                user_input_value = user_input_value[:-1]
            else:
                if len(user_input_value) <= 9:
                    user_input_value += event.unicode
            user_input = font.render(user_input_value, True, (0,0,0), (255,255,255))
            user_input_rect.x = 0
            user_input_rect.y = 40
        joueur.screen.blit(entrezvotreprenom, prompt_rect)
        joueur.screen.blit(user_input, user_input_rect)     
        pygame.display.flip()
        
    
        if event.type == pygame.MOUSEBUTTONDOWN:

            if jouezcliq.collidepoint(event.pos):
                
                if len(user_input_value)< 1:
                    print("vous n'avez rien ecrit banane !")
                else:
                    joueur.sound_manager.play("pion") 
                    joueur.acceuil = False
                    joueur.running = True
            
                
        
            if picturecliq.collidepoint(event.pos):

                if len(user_input_value)< 1:
                    print("vous n'avez rien ecrit banane !")
                else:

                    joueur.sound_manager.play("pion") 
                    joueur.acceuil = False
                    joueur.running = True

         

 
      
        if event.type == pygame.MOUSEMOTION:
            if jouezcliq.collidepoint(event.pos): 
            
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)


        
            elif reglescliq.collidepoint(event.pos): 
            
                pygame.mouse.set_cursor(*pygame.cursors.ball)
                joueur.screen.blit(reglestexte,(232,0))
            

            elif picturecliq.collidepoint(event.pos):
                    
                pygame.mouse.set_cursor(*pygame.cursors.ball)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)

                      
            pygame.display.flip()
    

print("Vous Vous appellez: ", str(user_input_value))
joueur.nomjoueur = user_input_value  

# boucle tant que cette condition est vrai
while joueur.running:


    font = pygame.font.SysFont('Comic Sans MS,Arial',16)
    votreprenom = font.render(joueur.nomjoueur + " votre score est de: " + str(joueur.score), True ,(0,0,0),(255,255,255))
    prompt_rect = votreprenom.get_rect()
    prompt_rect.x = 0
    prompt_rect.y = 0
    joueur.screen.blit(votreprenom, prompt_rect)
    pygame.display.flip()

    mous = pygame.cursors.load_xbm("assets/de.xbm", "assets/de-mask.xbm")
    sablier = pygame.cursors.load_xbm("assets/sablier.xbm", "assets/sablier-mask.xbm")
    pygame.display.set_caption("  jeu de l'oie")
    
    faceDuDejoueur1 = pygame.image.load(deListe[joueur.valeurdude_joueur1])

    faceDuDejoueurIA = pygame.image.load(deListe[joueur.valeurdude_joueurIA])    
#  affiche le pion a qui le tour en bas a droite
# affiche valeur du dé pour joueur1 et joueurIA
    if joueur.cestaujoueur1dejouer  == True:
                
        pionAQuiLeTour = joueur.pionBlanc
        pygame.mouse.set_cursor(*mous)
    else:
        pionAQuiLeTour = joueur.pionNoir
        pygame.mouse.set_cursor(*sablier)
    
    
    
    # appliquer a l'arriere plan de notre jeu
    joueur.screen.blit(background,(0,0))
    
    # applique l'image de mon joueur1  !!!!!!  dé, pion, face123456
    joueur.screen.blit(joueur.pionBlanc, joueur.rect_joueur1)
    
    joueur.screen.blit(joueur.pionNoir, joueur.rect_joueurIA)
    
    # pion qui indique les des
    joueur.screen.blit(joueur.pionBlanc,(387,258))
    joueur.screen.blit(joueur.pionNoir,(387,315))
    
    #pion a qui le tour
    joueur.screen.blit(pionAQuiLeTour,(22,82))
    #de cliquable , pas encors
    joueur.screen.blit(decliquable,(79,82))

    #des
    joueur.screen.blit(faceDuDejoueur1,(330,258))
    joueur.screen.blit(faceDuDejoueurIA,(330,315))
    #mettre à jour l'arriere plan
    pygame.display.flip()
        
    # si le joueur ferme cette fenetre


    for event in pygame.event.get():
           # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            joueur.running = False
    
            pygame.quit()    
                          

    # lance le "de" avec le clic de la souris ou avec la touche d 
               
        
        if event.type == pygame.MOUSEBUTTONDOWN :
            if joueur.cestaujoueur1dejouer == True  :  
                # 1 joueur 
                joueur.printrandom1()
                joueur.deplacementdupion1() 
                joueur.colision1()              
                joueur.reverif1()  
                joueur.cestaujoueur1dejouer = False    
                print("faux")

        elif joueur.cestaujoueur1dejouer == False:
            
        
            # IA joueur
            time.sleep(1)                  
            joueur.printrandomIA()
            joueur.deplacementdupionIA()
        
            joueur.colisionIA()
                
            joueur.revefifIA()            
            joueur.cestaujoueur1dejouer = True
                        
while joueur.findepartie == True:
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
        
    pygame.display.set_caption("  FIN")
     # appliquer a l'arriere plan de notre jeu
    joueur.screen.blit(backgroundAcceuil,(0,0))
    joueur.screen.blit(pictureAcceuil,(0,333))
    
    
    #mettre à jour l'arriere plan
    pygame.display.flip()


    # si le joueur clic , le joueur passe au jeu
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            joueur.sound_manager.play("oie") 
            joueur.findepartie = False
            
            joueur.acceuil = True
        # si le joueur ferme cette fenetre
        elif event.type == pygame.QUIT:
            joueur.findepartie = False
            pygame.quit()    
                
     
                       
        
        
                    
                    
