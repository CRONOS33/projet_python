# projet_python
#Bonjour ce projet a été fait par Antony.Guillot et Alexandre.Jolin
Pour lancer le jeu à ce jeu il suffit de lancer le code nomé game puis de cliquer sur start game
Pour jouer de vous deplacer avec les touche directoinelle de votre clavier et de tirer avec la touche espace.Pour gagner vos lasers devront detruire la ligne d'ennemis ce deplacant vers vous.
Vous avez trois vies que vous perdez si vous vous faites toucher par les lasers ennemies.
Vous perdez si vous n'avez plus de vie, si vous touchez un ennemi classique (pas l'ennemi bonus) ou si les ennemis reussisent à descendre trop bas.

les scores:
    100 points un ennemi classique
    500 la premiere phase de l'ennemi bonus
    250 la deuxieme
    100 la troisieme

Attention lors d'une win ou d'une lose la fenêtre se ferme apres 2s.

Lorsque que vous lancer une partie un menu d'option apparaît:
    -le restart ferme le jeu en cour et le réouvre,
    -le Cheat1 permet de mettre vous points de vie a 500 (oui c'est largement assez mais vous vous faites toujour one shoot si vous touchez un ennemie)
    -le Cheat2 permet à votre navire de ce deplacer verticalement
    -le Cancelcheat permet de mettre vos pv à 3 vous empecher de vous deplacer verticalement , et vous téléporte à la position de début de jeu

Consernant les Codes les fichier .py commençant par une Majuscule contienent une classe du même nom Ou pour Interface la fonction qui créer l'interface graphique du jeu.
La classe Monde contient les fonction de gestion de trajet des ennemy , de collision

Finalement une liste se trouve dans Monde ligne 27
           une pile de trouve dans Interface ligne 61
           une file se trouve dans Monde ligne 29

voici le lien du depots git :https://github.com/CRONOS33/projet_python.git