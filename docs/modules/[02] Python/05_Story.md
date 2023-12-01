<link rel="stylesheet" href="../stylesheet.css">

# Python: Fichiers/Fonctions/Modules

## Contexte
> Ce familiariser avec l'utilisation des fichiers et les modules en python.

## Mots clefs
- **Bibliothèque :** *Collection de modules, conçues pour être réutilisables et fournissent un ensemble de fonctionnalités spécifiques pouvant être intégrées dans des programmes plus vastes..*
- **CSV (Comma Separated Values):** *Fichier composé de valeurs, dont chacune est séparée par une virgule.*
- **Dataframe :** *Structure de données bidimensionnelle.*
- **Framework :** *Infrastructure logicielle qui fournit des composants et des outils prédéfinis pour aider les développeurs à créer, organiser et maintenir des applications. Les frameworks sont conçus pour faciliter le développement en fournissant une structure et des abstractions qui permettent aux développeurs de se concentrer sur la résolution de problèmes spécifiques plutôt que sur des détails de bas niveau..*
- **Module :** *Unité de code indépendante et réutilisable dedié à des tâches particulières.*
- **Package :** *Moyen d'organiser les modules en utilisant une hiérarchie de répertoires. Un package Python est simplement un répertoire contenant un fichier spécial appelé `__init__.py` qui indique que le répertoire doit être traité comme un package.*
- **`import` :** *Mot-clef python, permettant d'accéder à un module.*

## Problématiques
1. Comment manipuler un fichier en utilisant des modules ?
1. Comment importer et installer des librairies ?
1. Comment créer des modules ?

## Hypothèses
- <u>Une bibliothèque est un ensemble de modules</u> : <p-g>(V)</p-g> *!;*
- <u>Une librairie est plus petite qu’une bibliothèque</u> : <p-r>(F)</p-r> *!;*
- <u>Il est possible d’ouvrir un fichier en lecture et écriture</u> : <p-g>(V)</p-g> *!;*
- <u>Certains modules s’appuient sur d’autres modules</u> : <p-g>(V)</p-g> *!;*
- <u>Une bibliothèque est une boite à outils</u> : <p-g>(V)</p-g> *!;*
- <u>Il faut effectuer plusieurs opérations pour écrire dans un fichier</u> : <p-g>(V)</p-g> *!;*
- <u>Il faut fermer un fichier pour éviter la corruption des données</u> : <p-g>(V)</p-g> *Calling `f.write()` without using the with keyword or without calling `f.close()` **might** result in the arguments of `f.write()` not being completely written to the disk, even if the program exits successfully;*
- <u>Une bibliothèque est un fichier python</u> : <p-g>(V)</p-g> *!;*
- <u>On peut importer une librairie partiellement</u> : <p-g>(V)</p-g> *!.*

## Plan d'action
1. Investigation des ressources;
1. Définitions des mots clefs;
1. Vérifier les hypothèses;
1. Tester toutes les notions abordées sur un fichier Jupyter Notebook à rendre sur GitHub;
1. Répondre aux questions.