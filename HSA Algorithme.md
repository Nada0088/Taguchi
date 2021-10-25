### Les démarches d’un algorithme de recherche harmonique
En HSA, chaque solution est appelée « harmonie » et représentée par un vecteur 
réel à n dimensions. Une population initiale de vecteurs d'harmonie est générée 
de manière aléatoire et stockée dans une mémoire d'harmonie (HM). Ensuite, 
une nouvelle harmonie candidate est générée à partir de toutes les solutions du 
HM en utilisant une règle de prise en compte de la mémoire, une règle de 
réglage de la hauteur et une initialisation aléatoire. Enfin, le HM est mis à jour 
en comparant la nouvelle harmonie candidate et le pire vecteur d’harmonie du 
HM. Le pire vecteur d'harmonie est remplacé par le nouveau vecteur candidat 
s'il est supérieur au pire vecteur d'harmonie du HM. Le processus ci-dessus est 
répété jusqu'à ce qu'un certain critère de terminaison soit rempli. La HSA 
comprend trois phases de base, à savoir l’initialisation, l’improvisation d’un 
vecteur d’harmonie et la mise à jour du HM, décrites ci-dessous.
L'algorithme RH comprend cinq étapes :
· Initialisation des paramètres 
· Initialisation de la mémoire harmonique 
· Improvisation d’une nouvelle harmonie,
· Mise à jour de la mémoire harmonique
· Vérification du critère d’arrêt.

La procédure de la recherche harmonique se résume dans la figure suivante :

![Picture1](https://user-images.githubusercontent.com/81916000/138622591-80d70754-dbf1-4841-873a-ddeecbf45116.png)

# Remarque : 
 - HMCR (Harmony Memory Considération Rate) est un taux de 
considération de la Mémoire harmonique qui varie entre 0 et 1. Il est 
généralement entre 70% et 99%.
 - PAR (PITCH ADJUST RATE) est le taux d’ajustement représentant la 
probabilité d'apporter quelque modification a un élément de la mémoire 
d'harmonie avec PAR Î [0,1].

Dénir la fonction objectif.
  2 : Générer des harmonies initiales (des tableaux de nombres entiers).
  3 : Dénir le taux d'ajustement de fréquence (rpa), ainsi que les fréquences limites et la bande passante.
  4 : Dénir le taux d'acceptation dans la mémoire (raccept).
  5 : Poser t = 1.
  6 : Tant que (t < Nombre_maximal_d'itérations) faire
    6.a : Générer de nouvelles harmonies en n'acceptant que les meilleures d'entre elles.
    6.b : Ajuster les fréquences pour obtenir de nouvelles harmonies (solutions).
    6.c : Choisir aléatoirement un nombre rand, compris entre 0 et 1.
    6.d : Si (rand > raccept) alors Choisir aléatoirement une harmonie parmi celles qui existent déjà.
    6.e : Sinon
 Si (rand > rpa) Ajuster aléatoirement les fréquences sans dépasser les limites.
 Sinon Générer de nouvelles harmonies via la randomisation.
    6.f : Accepter les nouvelles harmonies (solutions) si elles sont meilleures.
    6.g : Incrémenter le nombre d'itérations, (t = t + 1).
    6.h : Trouver les meilleures solutions de l'itération courante.
Fin tant que.
