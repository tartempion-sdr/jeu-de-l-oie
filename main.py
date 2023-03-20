import pygame
import random
from joueurclass import Joueur
import csv
from grille import Grille



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
carreblanc = pygame.image.load("assets/carre-blanc.png")

background = pygame.image.load("assets/verdure-rogner2-850x567.png")

mous = pygame.cursors.load_xbm("assets/de.xbm", "assets/de-mask.xbm")
sablier = pygame.cursors.load_xbm("assets/sablier.xbm", "assets/sablier-mask.xbm")

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

pasDePrenom  = font.render("vous n'avez rien ecrit banane !" ,True ,(0,0,0),(255,255,255))
pasDePrenom_rect = pasDePrenom.get_rect()
pasDePrenom_rect.x = 0
pasDePrenom_rect.y = 40

cliqpasDePrenom  = font.render("ecrit et cela s'affiche tout seul, pas besoin de cliqué quelque part pour écrire" ,True ,(0,0,0),(255,255,255))
cliqpasDePrenom_rect = pasDePrenom.get_rect()
cliqpasDePrenom_rect.x = 0
cliqpasDePrenom_rect.y = 40

user_input = font.render(joueur.nomjoueur, True, (0,0,0), (255,255,255))
user_input_rect = user_input.get_rect()
user_input_rect.x = 0
user_input_rect.y = 20

 # boucle tant que cette condition est vrai
while joueur.recommencer :
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
            
            if event.type == pygame.QUIT:
                joueur.acceuil = False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN :    
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    
                    if len(joueur.nomjoueur)< 1:

                        joueur.screen.blit(pasDePrenom,pasDePrenom_rect)
                        pygame.display.flip()

                        
                    else: 
                        joueur.acceuil = False
                        joueur.running = True
                        joueur.sauvegarde = True
                    break    
                    
                if event.key == pygame.K_BACKSPACE:
                    joueur.nomjoueur = joueur.nomjoueur[:-1]
                else:
                    if len(joueur.nomjoueur) <= 9:
                        joueur.nomjoueur += event.unicode
                user_input = font.render(joueur.nomjoueur, True, (0,0,0), (255,255,255))
                user_input_rect.x = 0
                user_input_rect.y = 40
            joueur.screen.blit(entrezvotreprenom, prompt_rect)
            joueur.screen.blit(user_input, user_input_rect)     
            
            pygame.display.flip()
            
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if jouezcliq.collidepoint(event.pos):
                    
                    if len(joueur.nomjoueur)< 1:

                        joueur.screen.blit(cliqpasDePrenom,cliqpasDePrenom_rect)
                        pygame.display.flip()
                        
                    else:
                        joueur.sound_manager.play("pion") 
                        joueur.acceuil = False
                        joueur.running = True
                
                # debug
                # if picturecliq.collidepoint(event.pos):    
                #     joueur.sound_manager.play("pion") 
                #     joueur.acceuil = False
                #     joueur.findepartie = True
                
            if event.type == pygame.MOUSEMOTION:
                if jouezcliq.collidepoint(event.pos):

                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    if len(joueur.nomjoueur)< 1:
                        joueur.screen.blit(pasDePrenom,pasDePrenom_rect)
                        pygame.display.flip()
                    
                
                elif reglescliq.collidepoint(event.pos): 
                
                    pygame.mouse.set_cursor(*pygame.cursors.ball)
                    joueur.screen.blit(reglestexte,(232,0))
                

                elif picturecliq.collidepoint(event.pos):
                        
                    pygame.mouse.set_cursor(*pygame.cursors.ball)
                    joueur.screen.blit(carreblanc,(232,0))
                    
                   
                    with open("out_score_ordre_croissant.csv",) as fichier:
                        reader = csv.DictReader(fichier, delimiter=",")
                        titre = "Nom du joueur    Score   Place "
                        titreDesScore = font.render(str(titre), True, (0,0,0), (255,255,255))
                        ajoutTitreDesScore = joueur.screen.blit(titreDesScore, (240, 0))                      
                        # faire quelque chose avec une ligne
                        l = 0
                        yy = 20
                    
                        for ligne in reader:
                             if l < 10:
                            
                                l = l + 1
                                yy += 25                     
                                lignesnom = font.render(str(ligne["nomjoueur"]), True, (0,0,0), (255,255,255))
                                ajoutUneLigne1 = joueur.screen.blit(lignesnom, (250, yy))
                                lignescore = font.render(str(ligne["score"]), True, (0,0,0), (255,255,255))
                                ajoutUneLigne2 = joueur.screen.blit(lignescore, (400, yy))
                                ligneclassement = font.render(str(l), True, (0,0,0), (255,255,255))
                                ajoutUneLigne3 = joueur.screen.blit(ligneclassement, (450, yy))
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                        
                pygame.display.flip()
         
    while joueur.running:


        

        
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
        
        font = pygame.font.SysFont('Comic Sans MS,Arial',16)
        votreprenom = font.render("case " + str(joueur.position1) + " : " + joueur.nomjoueur + " votre score est de: " + str(joueur.score), True ,(0,0,0),(255,255,255))
        prompt_rect = votreprenom.get_rect()
        prompt_rect.x = 0
        prompt_rect.y = 0
        joueur.screen.blit(votreprenom, prompt_rect)
        
        
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
                    
                if joueur.cestaujoueur1dejouer == True :                
                    # 1 joueur 
                    

                    joueur.printrandom1()
                    pygame.time.delay(1000)
                    joueur.deplacementdupion1() 
                    
                    joueur.colision1()                   
                    joueur.verif1()  
                    joueur.cestaujoueur1dejouer = False    
                    

            elif joueur.cestaujoueur1dejouer == False:
                
                
                # IA joueur
                pygame.time.delay(500)         
                joueur.printrandomIA()
                pygame.time.delay(1000)
                joueur.deplacementdupionIA()
                
                joueur.colisionIA()     
                joueur.vefifIA()            
                joueur.cestaujoueur1dejouer = True
        
                
    while joueur.findepartie :

             
        pygame.display.set_caption("  FIN")
        # appliquer a l'arriere plan de notre jeu
        joueur.screen.blit(backgroundAcceuil,(0,0))
        joueur.screen.blit(pictureAcceuil,(0,333))
        
        enregistrercliq = pygame.Rect((0, 0),(215, 60))

        font = pygame.font.SysFont('Comic Sans MS,Arial',16)

        if joueur.position1 == 63 :
            votreprenom = font.render(joueur.nomjoueur + " votre score est de: " + str(joueur.score) + " vous avez gagné ! ", True ,(0,0,0),(255,255,255))
            
    
            if joueur.sauvegarde == True:
                enregistrer = font.render(" Cliquez ICI pour enregistrez Votre score", True ,(0,0,0),(255,255,255))
                
            else:
                enregistrer = font.render(" Votre partie a bien été enregistrer", True ,(0,0,0),(255,255,255))

            enregistrer_rect = enregistrer.get_rect()
            enregistrer_rect.x = 0
            enregistrer_rect.y = 30
            joueur.screen.blit(enregistrer, enregistrer_rect)

        else:
            votreprenom = font.render(joueur.nomjoueur + " vous avez perdu", True ,(0,0,0),(255,255,255))
        
        
       

        votreprenom_rect = votreprenom.get_rect()
        votreprenom_rect.x = 0
        votreprenom_rect.y = 0
        joueur.screen.blit(votreprenom, votreprenom_rect)
        
        #mettre à jour l'arriere plan
        pygame.display.flip()


        # si le joueur clic , le joueur passe au jeu
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                if picturecliq.collidepoint(event.pos):
                    pygame.mouse.set_cursor(*mous)
                    pygame.display.flip()
                else :
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                if enregistrercliq.collidepoint(event.pos):
                    if joueur.position1 == 63 : 
                        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                        pygame.display.flip()

        #for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if picturecliq.collidepoint(event.pos):
                    joueur.sound_manager.play("oie") 
                    joueur.score = 0
                    
                    joueur.acceuil = True
                    joueur.findepartie = False
                    pygame.display.flip()

                if enregistrercliq.collidepoint(event.pos):
                    
                    ## enregistre le score en un clic.
                    if joueur.position1 == 63 : 
                        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                        joueur.enregisterScore()
                        joueur.sauvegarde = False
                        
                        
            # si le joueur ferme cette fenetre
            if event.type == pygame.QUIT:
                
                joueur.sound_manager.play("oie") 
                joueur.findepartie = False
               
                pygame.quit()    
                    
        
                        
        
        
                    
                    
