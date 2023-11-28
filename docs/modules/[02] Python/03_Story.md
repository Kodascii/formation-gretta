<link rel="stylesheet" href="../stylesheet.css">

# Python: [Les Boucles](https://courspython.com/boucles.html)

## Contexte
> Se familiariser avec les différents types de boucles.

## Mots clefs
- **Boucle :** *Structure de contrôle permettant d'itérer l'exécution d'un bloc tant qu'une condition est respecté. (Boucle bornée, ou non bornée.)*
- **Boucle bornée :** *Boucle permettant d'itérer sur une séquence prédéfinie d'éléments.*
- **Boucle non bornée :** *Boucle permettant de répéter l'exécution d'un bloc, tant qu'un condition est vraie.*
- **Boucle imbriqué :** *Boucle à l'intérieur d'une autre boucle.*
- **Liste en compréhension :** *Manière concise de créer des listes. Elle permet de générer des listes en une seule ligne de code en utilisant une syntaxe compacte et expressive.*
- **Itération :** *Répétition d'un bloc d'instructions ou d'une séquence de code plusieurs fois.*
- **Pas :** *Quantité d'incrémentation.*
- **Récursivité :** *Capacité d'une fonction ou d'un algorithme à s'appeler elle-même.*
- **`def ` :** *Mot-clef python, désignant le début de la déclaration d'une fonction.*
- **`range()` :** *Fonction pré-définie générant une séquence de nombres contenue dans l'interval donné.*
- **`None` :** *Type d'objet spécial qui représente l'abscence de valeur dans la variable. C'est un singleton, il n'existe qu'une seule instance dans un programme python.*
- **`for` :** *Mot-clef python, désignant le début d'une boucle bornée.*
- **`while` :** *Mot-clef python, désignant le début d'une boucle non bornée.*
- **`pass` :** *Insstruction python, ne faisant rien.*
- **`return` :** *Utilisé dans une fonction pour renvoyer une valeur spécifique.*
- **`break` :** *Instruction python, permettant de sortir d'une boucle.*
- **`continue` :** *Instruction python, permettant de passer à l'itération suivante de la boucle.*

## Problématiques
1. Comment utiliser les boucles pour résoudre un problème ? 
1. Comment choisir la boucle adéquate ? 
1. Comment faire pour qu’une boucle ne tourne pas à l’infini ? 
1. Comment connaitre le nombre d’itération pour une boucle ? 

## Hypothèses
- **Hadjer :** <u>Il n’y a que 2 types de boucles </u> <p-g>(V)</p-g> *!*
- **Salah:** <u>Il faut indenter les structures de boucle</u> <p-g>(V)</p-g> *!*
- **Rafael :** 
    - <u>On peut faire une boucle qui se décrémente</u> <p-g>(V)</p-g> *!*
    - <u>On peut mettre un `for` dans un `while` et inversement</u> <p-g>(V)</p-g> *!*
- **Thibaut :** <u>`match` est un type de boucle </u> <p-r>(F)</p-r> *!*
- **Alexis :** <u>Une boucle bornée peut s’écrire comme une boucle non bornée</u> <p-g>(V)</p-g> *!*
- **Hassan :** <u>Toutes les boucles sont infinies </u> <p-r>(F)</p-r> *!*
- **Alexandre :** <u>On peut sortir d’une boucle quand l’on veut </u> <p-g>(V)</p-g> - *en utilistant `break`*
- **Ahmed :** <u>La fonction `range()` est importante pour la boucle `for`</u> <p-g>(V)</p-g> *!*
- **Philippe :** <u>Imbriqué des boucles n’a pas d’impact sur la lourdeur du programme</u> <p-g>(V)</p-g> *!*
- **Bart :**
    - <u>Il n'existe pas de `do-while` en python</u> <p-g>(V)</p-g> *!*
    - <u>On peut annoter les boucles en python</u> <p-r>(F)</p-r> *!*
- **Paul :** <u>On peut utiliser des opérateurs de comparaisons dans les boucles</u> <p-g>(V)</p-g> *!*

## Plan d'action
1. Investigation des ressources
1. Définitions des mots clefs;
1. Vérifier les hypothèses;
1. Répondre aux questions.