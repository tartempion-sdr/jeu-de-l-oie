![alt tag](https://github.com/tartempion-sdr/jeu-de-l-oie/blob/master/assets/capture-decran-de-2023-03-08-00-26-29.png)



		=:-jeu de l'oie les règle de base-:=
		
	   Pour gagner arriver le premier sur la case 63
	 
	     Celui qui est rejoint par un autre joueur 
		 sur la même case devra se rendre 
	sur la case ou l’autre joueur se situait avant de jouer.

    Si lors de la partie, le joueur tombe sur une oie(case[ 8,26,36 ])
	   avance de nouveau du nombre de points réalisés. 
	    
	      =:-Le joueur qui tombe sur la case:-:=
	    
	     8  Oie                             
	    19  correspondant a l'hôtel 
			recommencez la partie depuis le début
	    26  Oie 
	    27 -> 57  echelles  
	    31  correspondant au puits 
			recommencez la partie depuis le début
	    36 Oie
	    40 -> 62  echelles 
	    42 correspondant au labyrinthe 
	       retournez à la case 30.
	    46 -> 54  echelles 
	    52 correspondant a la prison 
	       recommencez la partie depuis le début
	    58 correspondant à la case Tête de mort 
	    recommencera la partie depuis le début
	    
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
git push origine master  