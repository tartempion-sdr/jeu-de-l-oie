![alt tag](https://github.com/tartempion-sdr/jeu-de-l-oie/blob/master/assets/Capture d’écran du 2025-11-04 18-13-28.png)



		=:-jeu de l'oie les règle de base-:=
		
	   Pour gagner arriver le premier sur la case 63
	 
	     Celui qui est rejoint par un autre joueur 
		 sur la même case devra se rendre 
	sur la case ou l’autre joueur se situait avant de jouer.

    Si lors de la partie, le joueur tombe sur une oie(case[ 8,26,36 ])
	   avance de nouveau du nombre de points réalisés. 
	    
	    
	      =:-Le joueur qui tombe sur la case:-:=
	    
	     8   Oie double votre deplacement                            
	    19  correspondant au coups de fusil 
			recommencez la partie depuis le début
	    26  Oie double votre deplacement
	    27 -> 57  echelle  
	    31  correspondant au coups de fusil 
			recommencez la partie depuis le début
	    36 Oie double votre deplacement
	    40 -> 62  echelle 
	    42 correspondant au labyrinthe 
	       retournez à la case 30.
	    46 -> 54  echelle 
	    52 correspondant au coups de fusil  
	       recommencez la partie depuis le début
	    
		si le joueur réalise un score aux dés 
	supérieur au nombre de case le séparant de la case 63 
	 il devra reculer d’autant de cases supplémentaires.
		    

    install

sudo apt-get install git

git clone https://github.com/tartempion-sdr/jeu-de-l-oie.git

    install pré-requis

pip3 install pygame  
ou  
sudo apt-get install python3-pygame  


pip3 install pandas  
ou  
sudo apt-get install python3-pandas

pip3 install csv

    lancez le jeu de l'oie

cd jeu-de-l-oie

python3 main.py

   mise a jour

git pull

    mise a jour du repository

git add .  
git commit -m "go pygame"   
git push origin master  