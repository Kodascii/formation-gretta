<link rel="stylesheet" href="../../stylesheet.css">

# Story_01 — Merise & MCD/MPD

## Contexte
> Concevoir et réaliser une base de données, ainsi que comprendre les modèles MCD, MLD et MPD.

## Mots clefs
- <def-of>Attribut</def-of> : *Les entités sont caractérisées par des attributs qui décrivent différentes propriétés ou caractéristiques de l'entité. (Par exemple, un client pourrait avoir des attributs tels que "Nom", "Adresse", et "Numéro de téléphone".)*
- <def-of>Entité</def-of> : *Objet ou un concept distinct du monde réel, pouvant être identifié et différencié des autres objets.*
- <def-of>Cardinalité</def-of> : *Couples de valeur qui apportent des contraintes sur le MCD. Elles traduisent des règles de gestion — Dans le modèle UML on parle alors de multiplicité : c’est le nombre de relations possibles entre types. Si une classe « ville » peut avoir 10 « structures », il y a multiplicité 0..10.*
- <def-of>Dépendance Fonctionnelle</def-of> : *Formellement, dans une table relationnelle, une dépendance fonctionnelle est notée comme A → B, où A et B sont des ensembles d'attributs (colonnes). Cela signifie que, pour chaque combinaison unique de valeurs dans les colonnes A, il existe une seule valeur correspondante dans la colonne B.*
    - <def-of>— Complète</def-of> : *A → B, où B dépend entièrement de A, et si nous retirons n'importe quel attribut de A, la dépendance fonctionnelle ne tiendra plus.*
    - <def-of>— Transitive</def-of> : *Si A → B et B → C, alors A → C. Cela signifie que la dépendance fonctionnelle se propage à travers une autre colonne.*
    - <def-of>— Partielle</def-of> : *Si A → B, mais B dépend également d'un autre attribut C, alors il y a une dépendance fonctionnelle partielle.*
- <def-of>Dictionnaire de données</def-of> : *Ensemble organisé d'informations détaillées sur les données utilisées dans un système d'information ou une base de données. Il s'agit d'une documentation qui fournit une description détaillée de chaque élément de données, y compris sa signification, sa source, son format, sa relation avec d'autres données, etc. Ce dictionnaire joue un rôle essentiel dans la gestion des données et la communication entre les équipes techniques et non techniques au sein d'une organisation.*
- <def-of>Héritage</def-of> : **
- <def-of>Looping</def-of> : *Lociel de modélisation conceptuelle de données (*entièrement gratuit et libre d'utilisation*).*
- <def-of>Merise</def-of> : *Méthode pour rassembler les idées sans effort, ou encore, vient du merisier qui est un porte-greffe.*
- <def-of>PowerAMC</def-of> : *Outil, utilisé pour concevoir et modéliser des bases de données, ainsi que d'autres éléments tels que des architectures d'entreprise, des modèles UML, etc.*
- <def-of>Règle de gestion</def-of> : **
- <def-of>Relation</def-of> : *Référence à une table spécifique qui stocke des données structurées.*
- <def-of>Sémantique</def-of> : *La sémantique concerne la manière dont les données représentent le monde réel et la façon dont elles sont interprétées par les utilisateurs et les applications.*
- <def-of>[1] MCD (Modèle Conceptuel des Données)</def-of> : *Représentation graphique de haut niveau qui permet facilement et simplement de comprendre comment les différents éléments sont liés entre eux.*
- <def-of>[2] MLD (Modèle Logique des Données)</def-of> : *Représentation textuelle du MCD (*usage de SQL*).*
- <def-of>[3] MPD (Modèle Physique des Données)</def-of> : *Étape permettant de construire la structure finale de la base de données avec les différents liens entre les éléments qui la composent (*dépendant du logiciel utilisé*).*
- <def-of>MER (Modèle Entité-Relation)</def-of> : *Modèle conceptuel qui utilise des entités, des relations et des attributs pour représenter graphiquement la structure d'une base de données.*
- <def-of>UML (Unified Modeling Language)</def-of> : *Langage de modélisation visuelle utilisé pour concevoir, spécifier et documenter les systèmes logiciels.*
- <def-of>Normalisation</def-of> : *Processus de conception qui vise à organiser les données de manière efficace pour réduire la redondance et améliorer l'intégrité des données.*
    - <def-of>— Première Forme Normale (1NF)</def-of> : *Une table est en 1NF si elle ne contient pas de valeurs répétées ou de groupes de valeurs atomiques. Chaque colonne de la table doit contenir une seule valeur et ne doit pas être une liste ou un ensemble de valeurs.*
    - <def-of>— Deuxième Forme Normale (2NF)</def-of> : *Une table est en 2NF si elle est en 1NF et si toutes ses dépendances fonctionnelles dépendent de la totalité de la clé primaire. Cela signifie qu'il ne doit pas y avoir de dépendance partielle de la clé primaire.*
    - <def-of>— Troisième Forme Normale (3NF)</def-of> : *Une table est en 3NF si elle est en 2NF et si elle ne contient pas de dépendances transitives entre les colonnes non clés. En d'autres termes, toutes les colonnes non clés doivent dépendre uniquement de la clé primaire.*

## Problématiques
1. Comment concevoir une base de donnés avec la méthode Merise ?
1. Comment stucturé les données et construire le MCD ?

## Hypothèses
- <u>Une base de données contient forcément plusieurs fichiers</u> <h-t/> : *!;*
- <u>On se passer de la méthode Merise pour créer une base de données</u> <h-t/> : *!;*
- <u>Une table peut avoir plusieurs clefs étrangères</u> <h-t/> : *!;*
- <u>On peut créer un MPD avant un MCD</u> <h-t/> : *!;*
- <u>Le MPD est identique au MCD </u> <h-t/> : *!;*
- <u>La méthode Merise est la meilleure méthode pour concevoir une base de données</u> <h-t/> : *!;*
- <u>Il est possible de relier une entité a elle-même</u> <h-t/> : *!;*
- <u>La phase de modélisation d’une BDD est facultative</u> <h-t/> : *!;*
- <u>Modifier le schéma d’une BDD peut permettre d’ajouter une couche de sécurité</u> <h-t/> : *!;*
- <u>Pour faire une relation entre 2 tableaux il n’est pas nécessaire d’avoir une clef étrangère</u> <h-t/> : *!;*

## Plan d'action
1. Investigation des ressources
1. Définitions des mots clefs;
1. Vérifier les hypothèses;
1. Faire le workshop;
1. Répondre aux questions.

# Extras
- *Intégrité référentielle*

## Lecture MLD
- Chaque ligne représente une table ;
- C’est toujours le nom de la table qui est écrit en premier ;
- Les champs sont listés entre parenthèses et séparés par des virgules ;
- Les clés primaires sont soulignées et placées au début de la liste des champs ;
- Les clés étrangères sont préfixées par un dièse.

## Changement de vocabulaire entre MCD et MPD
- Les entités se transforment en tables ;
- Les propriétés se transforment en champs (ou attributs) ;
- Les propriétés se trouvant au milieu d’une relation génèrent une nouvelle table ou glissent vers la table adéquate en fonction des cardinalités de la relation ;
- Les identifiants se transforment en clés et se retrouvent soulignés. Chaque table dispose d’au minimum 1 clé dite primaire ;
- Les relations et les cardinalités se transforment en champs parfois soulignés : il s’agit de créer des « clés étrangères » reliées à une « clé primaire » dans une autre table.