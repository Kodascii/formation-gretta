<link rel="stylesheet" href="../stylesheet.css">

# Python: Conditions et Booléens

## Contexte
> Se familiariser avec les conditions et les booléens.

## Mots clefs
- **Bloc de code :** *Section de code source dans un programme informatique qui est regroupée ensemble et exécutée comme une unité.* 
- **Condition :** *Expression qui peut-être évalué vraie ou fausse.* 
- **Alternative :** *Bifurcation dans l'exécution d'un programme en fonction d'une condition.* 
- **Structure de contrôle :** *Ensemble d'instructions qui détermine l'ordre d'exécution des instructions dans un programme.*
- **Structure conditionnelle :** *Construction qui permet d'exécuter des blocs de code en fonction de conditions spécifiques.* 
- **Structure de boucle :** *Construction de programmation qui permet d'exécuter un bloc de code de manière répétée tant qu'une certaine condition est vraie (boucle `while`) ou pour un nombre prédéterminé d'itérations (boucle `for`).* 
- **Variable booléen :** *Type de variable en programmation informatique qui peut avoir deux valeurs distinctes : `true` ou `false`.* 
- **Opérateurs booléens :** *Symbole ou mot-clef utilisé pour effectuer des opérations logiques entre des expressions booléennes* 
- **Opérateurs de comparaison :** *Symboles ou mot-clef, utilisés en programmation pour comparer deux valeurs et produire un résultat booléen (vrai ou faux) en fonction de la relation entre ces valeurs.* 
- **Test :** *Fait généralement référence à l'évaluation d'une condition ou d'un ensemble de conditions pour déterminer si une certaine partie du code doit être exécutée.* 
- **Tests imbriqués :** *Référence à l'utilisation de tests à l'intérieur d'autres tests, créant ainsi une structure hiérarchique de tests. Cette approche est souvent utilisée dans le contexte des tests unitaires.* 
- **Tests multiples :** *Référence à l'exécution de plusieurs cas de test dans le cadre d'une suite de tests. Dans le contexte des tests logiciels, une suite de tests est un ensemble organisé de cas de test qui vise à vérifier le bon fonctionnement d'un logiciel dans différentes situations.* 

## Problématiques
1. Dans quel contexte utiliser les booléens? 
1. Comment construire une structure conditionnelle? 
1. Comment modéliser les problèmes en termes de tests et d’alternatives?

## Hypothèses
- <u>`match` est une structure condtionnelle</u>: <p-r>(F)</p-r> *Correspondance des modèles structurels*
- <u>Il est possible d’avoir une condition sans les booléens.</u>: <p-g>(V)</p-g> *!*
- <u>Le nombre d’imbrications dans les conditions est infinie.</u>: <p-r>(F)</p-r> *!*
- <u>On ne peut avoir d’opérateurs de comparaison dans une condition</u>: <p-g>(V)</p-g> *!*
- <u>Le ternaire existe en python.</u>: <p-g>(V)</p-g> *!*
- <u>Il existe d’autres structures conditionnelles autres que if, elif and else.</u>: <p-g>(V)</p-g> *!*
- <u>Une condition ne peut avoir qu’une instruction (`if`). </u>: <p-r>(F)</p-r> *!*
- <u>Une condition est une variable.</u>: <p-r>(F)</p-r> *!*
- <u>L’évaluation d’une condition ne peut avoir qu’une seule valeur.</u>: <p-g>(V)</p-g> *!*
- <u>On peut mettre deux conditions dans une même ligne.</u>: <p-g>(V)</p-g> *!*
- <u>`False == 0`</u>: <p-g>(V)</p-g> *!*
- <u>Une condition peut être assigné avec une variable</u>: <p-g>(V)</p-g> *!*


## Plan d'action
1. Explorer les ressources.
1. Définir les mots clés.
1. Vérifier les hypothèses.
1. Utiliser Jupyter Notebook pour tester toutes les notions abordées.
1. Faire les exercices dans le fichier : Booléens et les [`conditions.ipynb`](02_Conditions.ipynb).
1. Finaliser le RER.