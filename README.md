![alt tag](https://github.com/tartempion-sdr/jeu-de-l-oie/blob/master/assets/capture-decran-de-2023-03-08-00-26-29.png)


jeu de l'oie: les règles de base.

Si lors de la partie, le joueur tombe sur une oie, il avance de nouveau du nombre de points réalisés. 8,26,36



les echelles:   27 -> 57
                62 -> 40 
                46 -> 54

Le joueur qui tombe sur la case 19 correspondant à un hôtel devra passer son tour durant 2 tours.


Le joueur qui tombe sur la case 31 correspondant au puits attendra qu’un autre joueur arrive au même numéro et prendra sa place.


Celui qui tombe sur la case 42 correspondant au labyrinthe retournera obligatoirement à la case 30.


Qui ira en 52 correspondant la prison attendra qu’un autre joueur vienne au même numéro pour repartir.


Le joueur qui va sur la case 58 correspondant à la case Tête de mort recommencera la partie depuis le début


Celui qui est rejoint par un autre joueur sur la même case devra se rendre sur la case ou l’autre joueur se situait avant de jouer.

Comment gagner une partie de jeu de l’Oie :

Pour gagner une partie de jeu de l’Oie, il faut être le premier à arriver sur la dernière case 63, mais avec l’obligation d’arriver pile sur cette case. Au cas où le joueur réaliserait un score aux dés supérieur au nombre de case le séparant de la victoire, il devra reculer d’autant de cases supplémentaires.

    install

sudo apt-get install git

git clone https://github.com/tartempion-sdr/jeu-de-l-oie.git

    install pré-requis

pip3 install pygame
Ou
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