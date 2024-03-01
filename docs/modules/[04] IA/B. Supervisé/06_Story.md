<link rel="stylesheet" href="../../../stylesheet.css">

# Story_00 — Support Vector Machines (SVC & SVR)

## Contexte
> .

## Mots clefs
- <def-of>SVM</def-of> : *Ensemble de méthodes d’apprentissage supervisé utilisées pour la classification, la régression et la détection des valeurs aberrantes.*
- <def-of>SVC (Support Vector Classification)</def-of> : *visent à trouver un hyperplan optimal pour séparer les différentes classes dans l'espace des caractéristiques.*
- <def-of>SVR (Support Vector Regression)</def-of> : *Vise à trouver un hyperplan optimal qui maximise la marge tout en minimisant l'erreur de prédiction.*
- <def-of>Vecteur Support</def-of> : *point de données d'entraînement qui se trouve le plus près de l'hyperplan de décision.*
- <def-of>[RBF](https://fr.wikipedia.org/wiki/Fonction_de_base_radiale) (Radial Basis Function)</def-of> : **
    $$K(x, y) = \exp(-\gamma||x - y||^2$$
- <def-of>Hyperplan</def-of> : *Objet mathématique qui définit une séparation dans un espace de dimension supérieure. Dans le contexte des SVM, il est utilisé pour délimiter les classes et maximiser la marge entre elles.*
- <def-of>[MAE](https://en.wikipedia.org/wiki/Mean_absolute_error) (Mean Absolute Error)</def-of> : *Evalue la performance d'un modèle de régression, en quantifiant la différence moyenne entre les valeurs prédites par le modèle et les valeurs réelles de la variable cible.*
    $$MAE = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|$$
- <def-of>MSE (Mean Squared Error)</def-of> : *Quantifie la moyenne des carrés des différences entre les valeurs prédites par le modèle et les valeurs réelles de la variable cible.*
    $$MSE = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$$
- <def-of>RMSE (Root Mean Squared Error)</def-of> : **
    $$RMSE = \sqrt{MSE}$$
- <def-of>R²</def-of> : *Le coefficient de détermination, mesure la qualité de la prédiction d'une régression linéaire.*
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y}_i)^2}$$
- <def-of>Marge Maximale</def-of> : **
- <def-of>Epsilon</def-of> : **
- <def-of>`C`</def-of> : *Paramètre de régularisation; Compromis entre les violations de marges et l'augmentation de la marge.*
- <def-of>`kernel`</def-of> : **
- <def-of>`gamma`</def-of> : **
- <def-of></def-of> : **

## Problématiques
1. Comment mettre en place une SVM ?

## Hypothèses
- <u>Le choix du kernel est le plus important pour avoir un bon critère de performance</u> <h-t/> :
    *il influence directement la capacité du modèle à représenter la relation entre les données d'entrée et la variable cible.*
- <u>SVR est robuste aux valeurs aberrantes</u> <h-t/> : *!;*
- <u>Pour définir un noyaux personalisé il faut une excellente connaissance à la fois du domaine d'application et à la fois du problème.</u> <h-t/> : *!;*
- <u>Dans la SVM, tous les points de données ne sont pas traités de manière égale</u> <h-t/> : *!;*
- <u>SVM n'est efficace que dans le cas des données linéairement séparables</u> <h-f/> : *!;*

## Plan d'action
1. Explorer les ressources
1. Définir et comprendre les mots clefs
1. Faire les Workshops
1. Utilisation du gridsearch et validation croisée pour trouver les hyperparamètres optimaux
1. Finaliser le RER


# RER

### Correlation
> Correlation measures the strength and direction of a linear relationship between two variables. It quantifies how changes in one variable correspond to changes in another. The correlation coefficient, typically denoted as “r” ranges from -1 to 1, where -1 indicates a perfect negative correlation, 1 signifies a perfect positive correlation, and 0 implies no correlation.

### Regression
> Regression, on the other hand, aims to predict the value of one variable based on the values of one or more other variables. It establishes an equation that describes the relationship between the variables. In simple linear regression, there is one predictor variable, while multiple linear regression involves more than one predictor.