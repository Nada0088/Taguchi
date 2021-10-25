### Organisation des paramètre IHSA

En HSA, il existe peu de paramètres importants - HMCR, PAR, bw, mais les 
paramètres PAR et bw sont des paramètres très importants pour le réglage 
précis des vecteurs de solution optimisés. L'algorithme HS traditionnel utilise 
une valeur fixe pour PAR et bw.
Dans l’AHS, les valeurs PAR et bw ajustées à l'étape 1(initialisation) ne 
peuvent pas être modifiées lors des nouvelles générations. L’inconvénient 
principal de cette méthode est que le nombre d’itérations augmente, ce qui en 
fait une solution optimale.
Pour améliorer les performances de l’algorithme HS et éliminer les 
inconvénients, IHSA utilise les variables PAR et bw dans l’improvisation (étape 3).
PAR et bw changent dynamiquement avec le numéro de génération

## La méthode de Taguchi
L’objectif général de la méthode Taguchi est de produire un produit de 
haute qualité à faible coût pour le fabricant. Cette méthode a été 
développée par Genichi Taguchi. Le plan expérimental proposé par 
Taguchi consiste à utiliser des tableaux orthogonaux pour organiser les 
paramètres affectant le processus et les niveaux auxquels ils doivent être 
modifiés. Au lieu de devoir tester toutes les combinaisons possibles. Cela 
permet de collecter les données nécessaires pour déterminer les facteurs 
qui affectent le plus la qualité du produit avec un nombre minimum 
d'essais, permettant ainsi d'économiser du temps et des ressources (Moins 
d'essais impliquent que le temps et les coûts sont réduits). 
Dans une conception factorielle complète avec plus de facteurs et 
plusieurs niveaux de chaque facteur, le nombre total d'essais (N) peut être 
obtenu en utilisant l'égalité de la manière suivante :
- k N = L
- Où L est le nombre de niveaux et k le nombre de plans les facteurs.
Alors qu’en en utilisant Taguchi le nombre minimal d’expériences à réaliser le 
doit être fixé sur la base de la formule ci-dessous :
N Taguchi = 1+ NV (L - 1)
N Taguchi = Nombre d'expériences à mener
NV = Nombre de paramètres
L = nombre niveaux
Dans ce travail on a 
NV = 6 et L = 5, donc
N Taguchi = 1+ 6 (5-1) = 25.
Par conséquent, au moins 9 expériences doivent être menées (9 essais)

## Analyse de la performance d’IHSA

La méthode classique fait intervenir pour chaque essai .la valeur moyenne 
des différentes mesures faites et ne tient pas directement compte de la 
dispersion des mesures. La supériorité de la méthode Taguchi, par rapport à la 
méthode classique des plans d’expériences, résulte de l’utilisation d’un 
indicateur de performance : le ratio signal / bruit

# Ratio signal/bruit (s/n ratio)
Taguchi divise les facteurs en deux catégories : facteurs contrôlables et 
facteurs de bruit. Ils sont considérés comme influençant de la qualité du produit.
Le rapport signal sur bruit (S / N ratio) est utilisé dans cette analyse
Il prend simultanément en compte :
• d’une part : l’objectif recherché (le signal), 
• d’autre part : la dispersion de cette valeur (le bruit). 
Dans tous les cas, on retiendra que la performance est d’autant plus grande que 
le ratio signal / bruit est élevé.

# Les fonctions de test
Des fonctions de test appropriées sont indispensables au développement 
d'algorithmes d'optimisation, car les problèmes d'optimisation pratiques sont 
souvent coûteux en calcul. Cependant, les conclusions que l'on peut tirer sur les 
capacités d'un algorithme sont limitées par la connaissance des défis posés par 
une fonction de test particulière. Par conséquent, nous utiliserons deux fonctions 
de test : Rosenbrock et Wood-Colville.
· Fonction de Rosenbrock :
La fonction Rosenbrock est définie comme
𝑚𝑖𝑛𝑓(𝑥) = ∑(100(𝑥(𝑖 + 1) − 𝑥 2 (𝑖)) 2 + (𝑥(𝑖) − 1) 2 )
où l'optimum global est : 𝑥 ∗ = (1,1, … . .1) and 𝑓(𝑥 ∗ ) = 0 for −30 ≤ 𝑥(𝑖) ≤ 30.
· Fonction Wood-Colville:
cette fonction ressemble à celle de Rosenbrock mais elle prend quatre variables au lieu de 
deux : 
(X)=[100(x2−x21)]2+(1−x1)2+90(x4−x23)2+(1−x3)2+10.1[(x2−1)2+(x4−1)2]+19.8(x2−1)(x4−1)
