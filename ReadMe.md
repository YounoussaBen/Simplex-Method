# Programmation Linéaire avec l'Algorithme du Simplexe
---

## Introduction

Ce programme en Python utilise l'algorithme du simplexe pour résoudre des problèmes d'optimisation linéaire. L'optimisation linéaire est une méthode mathématique visant à maximiser ou minimiser une fonction linéaire tout en respectant un ensemble de contraintes linéaires.

---

## Comment Utiliser le Programme

1. **Saisie des Données du Problème** :
   - L'utilisateur est invité à entrer le nombre de variables, les coefficients de la fonction objectif, le nombre de contraintes, les coefficients de la matrice de contraintes, et les valeurs à droite des contraintes.

2. **Définition des Bornes pour Chaque Variable** :
   - Les bornes des variables sont définies par défaut à [0, infini). Les variables ne peuvent pas prendre des valeurs négatives.

3. **Installation des Dépendances** :
   - Assurez-vous d'avoir Python installé sur votre système.
   - Installez les bibliothèques NumPy et SciPy en utilisant les commandes suivantes :
     ```
     pip install numpy
     pip install scipy
     ```

4. **Résolution du Problème de Programmation Linéaire** :
   - L'algorithme du simplexe est appliqué en utilisant la bibliothèque SciPy. Le programme résout le problème d'optimisation linéaire en trouvant la solution optimale.

5. **Affichage des Résultats** :
   - Le programme affiche les résultats de l'optimisation, y compris la valeur optimale de la fonction objectif, les valeurs optimales des variables de décision, et d'autres informations pertinentes.
---

## Exemple d'Utilisation

```python
# Exemple d'utilisation avec les entrées de l'utilisateur et la sortie attendue
"""
Entrez le nombre de variables : 4
Entrez le coefficient pour la variable 1 : -5
Entrez le coefficient pour la variable 2 : 3
Entrez le coefficient pour la variable 3 : 4
Entrez le coefficient pour la variable 4 : -7
Entrez le nombre de contraintes : 3
Entrez le coefficient pour la variable 1 dans la contrainte 1 : 1
Entrez le coefficient pour la variable 2 dans la contrainte 1 : 1
Entrez le coefficient pour la variable 3 dans la contrainte 1 : 1
Entrez le coefficient pour la variable 4 dans la contrainte 1 : 1
Entrez le coefficient pour la variable 1 dans la contrainte 2 : 1
Entrez le coefficient pour la variable 2 dans la contrainte 2 : 0
Entrez le coefficient pour la variable 3 dans la contrainte 2 : 1
Entrez le coefficient pour la variable 4 dans la contrainte 2 : 0
Entrez le coefficient pour la variable 1 dans la contrainte 3 : 2
Entrez le coefficient pour la variable 2 dans la contrainte 3 : 1
Entrez le coefficient pour la variable 3 dans la contrainte 3 : 1
Entrez le coefficient pour la variable 4 dans la contrainte 3 : 0
Entrez la valeur du côté droit pour la contrainte 1 : 14
Entrez la valeur du côté droit pour la contrainte 2 : 7
Entrez la valeur du côté droit pour la contrainte 3 : 13
     con: array([], dtype=float64)  # Aucune violation de contrainte
     fun: -98.0  # Valeur optimale de la fonction objectif
 message: 'Optimization terminated successfully.'  # Le solveur a terminé avec succès
     nit: 7  # Nombre d'itérations effectuées
   slack: array([ 0.,  7., 13.])  # Variables d'écart (slack) pour chaque contrainte
  status: 0  # Code de statut 0 signifie une solution optimale trouvée
 success: True  # L'optimisation a réussi
       x: array([ 0.,  0.,  0., 14.])  # Valeurs optimales des variables
"""
```
---

## Exécution du Code

- Exécutez le fichier `script.py` dans votre terminal ou votre environnement de développement Python.

```
     python script.py

```



---
