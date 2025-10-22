import pygame
from joueurclass import Joueur
import csv
from grille import Grille
pygame.init()


# future icone
pygame_icon = pygame.image.load("assets/plateau/oiecase.png")
pygame.display.set_icon(pygame_icon)

# titre
pygame.display.set_caption("  jeu de l'oie")
# generer la fenetre de notre jeu
    

# charger joueur

joueur = Joueur()

screen = pygame.display.set_mode((850,567)) 
        
pygame.mouse.set_cursor(*pygame.cursors.arrow)

mous = pygame.cursors.load_xbm("assets/dés/de.xbm", "assets/dés/de-mask.xbm")
# entrez votre nom

font = pygame.font.SysFont('Comic Sans MS,Arial',13)
entrezvotreprenom = font.render("ENTREZ VOTRE PRENOM :" ,True ,(0,0,0),(255,255,255))
prompt_rect = entrezvotreprenom.get_rect()
prompt_rect.x = 55
prompt_rect.y = 86

pasDePrenom  = font.render("vous n'avez rien ecrit banane !" ,True ,(0,0,0),(255,255,255))
pasDePrenom_rect = pasDePrenom.get_rect()
pasDePrenom_rect.x = 55
pasDePrenom_rect.y = 108

cliqpasDePrenom  = font.render("ecrit et cela s'affiche tout seul, pas besoin de cliqué quelque part pour écrire" ,True ,(0,0,0),(255,255,255))
cliqpasDePrenom_rect = pasDePrenom.get_rect()
cliqpasDePrenom_rect.x = 55
cliqpasDePrenom_rect.y = 108

user_input = font.render(joueur.nomjoueur, True, (0,0,0), (255,255,255))
user_input_rect = user_input.get_rect()
user_input_rect.x = 55
user_input_rect.y = 108

 # boucle tant que cette condition est vrai
while joueur.recommencer :

    while joueur.acceuil :
        
        jouezcliq = pygame.Rect((35, 40),(186, 44))
        reglescliq = pygame.Rect((35, 130),(186, 44))
        picturecliq = pygame.Rect((35, 295),(186, 234))

        # appliquer a l'arriere plan de notre jeu
        screen.blit(joueur.backgroundAcceuil,(0,0))
        screen.blit(joueur.messageAcceuil,(488,40))
        screen.blit(joueur.jouez,(35,40))
        screen.blit(joueur.regles,(35,130))
        screen.blit(joueur.pictureAcceuil,(35,295))

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

                        screen.blit(pasDePrenom,pasDePrenom_rect)
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
                user_input_rect.x = 55
                user_input_rect.y = 108
            screen.blit(entrezvotreprenom, prompt_rect)
            screen.blit(user_input, user_input_rect)     
            
            pygame.display.flip()
            
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if jouezcliq.collidepoint(event.pos):
                    
                    if len(joueur.nomjoueur)< 1:

                        screen.blit(cliqpasDePrenom,cliqpasDePrenom_rect)
                        pygame.display.flip()
                        
                    else:
                        joueur.sound_manager.play("pion") 
                        joueur.acceuil = False
                        joueur.running = True
                
                
                
            if event.type == pygame.MOUSEMOTION:
                if jouezcliq.collidepoint(event.pos):

                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    if len(joueur.nomjoueur)< 1:
                        screen.blit(pasDePrenom,pasDePrenom_rect)
                        pygame.display.flip()
                    
                
                elif reglescliq.collidepoint(event.pos): 
                
                    pygame.mouse.set_cursor(*pygame.cursors.ball)
                    screen.blit(joueur.reglestexte,(488,79))
                

                elif picturecliq.collidepoint(event.pos):
                        
                    pygame.mouse.set_cursor(*pygame.cursors.ball)
                    screen.blit(joueur.carreblanc,(587,100))
                    
                    # tableau des scores
                    with open("out_score_ordre_croissant.csv",) as fichier:
                        reader = csv.DictReader(fichier, delimiter=",")
                        titre = "Nom du joueur    Score   Place "
                        titreDesScore = font.render(str(titre), True, (0,0,0), (255,255,255))
                        ajoutTitreDesScore = screen.blit(titreDesScore, (587,100))                      
                        # faire quelque chose avec une ligne
                        l = 0
                        yy = 105
                    
                        for ligne in reader:
                             if l < 10:
                            
                                l = l + 1
                                yy += 25                     
                                lignesnom = font.render(str(ligne["nomjoueur"]), True, (0,0,0), (255,255,255))
                                ajoutUneLigne1 = screen.blit(lignesnom, (587, yy))
                                lignescore = font.render(str(ligne["score"]), True, (0,0,0), (255,255,255))
                                ajoutUneLigne2 = screen.blit(lignescore, (698, yy))
                                ligneclassement = font.render(str(l), True, (0,0,0), (255,255,255))
                                ajoutUneLigne3 = screen.blit(ligneclassement, (745, yy))
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                        
                pygame.display.flip()
         
    while joueur.running:

        
        

        joueur.toutAfficher()
        
        for event in pygame.event.get():
            # que l'evenement est fermeture de fenetre
            if event.type == pygame.QUIT:
                joueur.running = False

                pygame.quit()    
                            
        
        # lance le "de" avec le clic de la souris 
        
            if event.type == pygame.MOUSEBUTTONDOWN :
                
                
                    
                if joueur.joueur1peutjouer  == True:  
                    joueur.toutAfficher()
                    # 1 joueur 
                    if joueur.rect_joueur1 != 52 and joueur.rect_joueur1 != 31 :
                        joueur.printrandom1()
                        pygame.time.delay(1000)
                        
                        joueur.deplacementdupion1() 
                        joueur.toutAfficher()
                        
                        joueur.colision1() 
                        joueur.toutAfficher()

                        if joueur.position1 > 57 :
                            pygame.time.delay(500) 
                            joueur.verif1()
                            joueur.toutAfficher()
                            print("triple verification j1")  

                        joueur.verif1()
                        joueur.toutAfficher()

                        joueur.verif1()
                        pygame.time.delay(100)
                        joueur.toutAfficher()
                        print("double verification j1")  

                        joueur.joueur1peutjouer = False
                        joueur.joueurIApeutjouer = True
                        print("debloque jIA") 

                        
                    

                    # IA joueur    
                if joueur.joueurIApeutjouer  == True:  
                    joueur.toutAfficher()
                
                    if joueur.rect_joueurIA != 52 and joueur.rect_joueurIA != 31 :
                        pygame.time.delay(500)         
                        joueur.printrandomIA()

                        pygame.time.delay(1000)
                        joueur.deplacementdupionIA()
                        joueur.toutAfficher()

                        joueur.colisionIA() 
                        joueur.toutAfficher()

                        if joueur.positionIA > 57 :
                            pygame.time.delay(500) 
                            joueur.vefifIA()
                            joueur.toutAfficher()
                            print("triple verification jIA") 

                        joueur.vefifIA()
                        joueur.toutAfficher()                            
                         
                        joueur.vefifIA()
                        pygame.time.delay(100)    
                        joueur.toutAfficher()
                        print("double verification jIA")
                                               
                        joueur.joueur1peutjouer = True
                        joueur.joueurIApeutjouer = False
                        print("debloque j1") 

                        

                        pygame.event.clear()    
                            

    while joueur.findepartie :

             
        pygame.display.set_caption("  FIN")
        # appliquer a l'arriere plan de notre jeu
        # plateau et case affichage...
        
        
        
        enregistrercliq = pygame.Rect((300, 300),(440, 100))

        font = pygame.font.SysFont('Comic Sans MS,Arial',16)

        if joueur.position1 == 63 :
            screen.blit(joueur.findepartiegagner,(0,0))
            votreprenom = font.render(joueur.nomjoueur + " votre score est de: " + str(joueur.score) + " vous avez gagné ! ", True ,(0,0,0),(255,255,255))
            
    
            if joueur.sauvegarde == True:
                
                font5 = pygame.font.SysFont('Comic Sans MS,Arial',56)

                enregistrer = font5.render("SAUVEGARDER", True ,(0,0,0),(255,255,255))
                
            else:
                enregistrer = font.render(joueur.nomjoueur + " Votre partie a bien été enregistrer", True ,(0,0,0),(255,255,255))
                

            enregistrer_rect = enregistrer.get_rect()
            enregistrer_rect.x = 300
            enregistrer_rect.y = 300
            screen.blit(enregistrer, enregistrer_rect)

        else:
            screen.blit(joueur.findepartieperdu,(0,0))
            font4 = pygame.font.SysFont('Comic Sans MS,Arial',56)

            votreprenom = font.render(joueur.nomjoueur + " vous avez perdu !", True ,(0,0,0),(255,255,255))

            gameover1 = font4.render("GAME-OVER.", True ,(0,0,0),(255,255,255))
            gameover_rect = gameover1.get_rect()
            gameover_rect.x = 490
            gameover_rect.y = 0
            screen.blit(gameover1, gameover_rect)

        screen.blit(joueur.picturerecommencer,(35, 295))

        votreprenom_rect = votreprenom.get_rect()
        votreprenom_rect.x = 0
        votreprenom_rect.y = 0
        screen.blit(votreprenom, votreprenom_rect)
        
        
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
                        if joueur.sauvegarde == True:
                            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                            

                        else:

                            pygame.mouse.set_cursor(*pygame.cursors.arrow)

                    else:

                        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        #for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if picturecliq.collidepoint(event.pos):
                    joueur.sound_manager.play("oie") 
                    joueur.score = 0
                    joueur.position1 = 0
                    joueur.rect_joueur1.x = Grille[joueur.position1][1] 
                    joueur.rect_joueur1.y = Grille[joueur.position1][2]
                    joueur.positionIA = 0
                    joueur.rect_joueurIA.x = Grille[joueur.positionIA][1] + 30
                    joueur.rect_joueurIA.y = Grille[joueur.positionIA][2] 
                    joueur.nomjoueur = ""
                    joueur.hotelj1 = 0
                    joueur.hoteljIA = 0
                    user_input = font.render(joueur.nomjoueur, True, (0,0,0), (255,255,255))
                    joueur.joueur1peutjouer = True
                    joueur.joueurIApeutjouer = False
                    joueur.running = False
                    joueur.findepartie = False
                    joueur.acceuil = True
                    joueur.toutAfficher()

                if enregistrercliq.collidepoint(event.pos):
                    
                    ## enregistre le score en un clic.
                    if joueur.position1 == 63 : 
                        if joueur.sauvegarde == True:
                            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                            joueur.enregisterScore()
                            joueur.sauvegarde = False
                    else:
                        
                        pygame.mouse.set_cursor(*pygame.cursors.arrow) 
                        
            # si le joueur ferme cette fenetre
            if event.type == pygame.QUIT:
                
                joueur.sound_manager.play("oie") 
                joueur.findepartie = False
               
                pygame.quit()    
                    
        
                        
        
        
                    
                    
