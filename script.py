import numpy as np
from scipy.optimize import linprog

# Obtenir le nombre de variables de l'utilisateur
num_variables = int(input("Entrez le nombre de variables : "))

# Obtenir les coefficients de la fonction objectif de l'utilisateur
obj = [float(input(f"Entrez le coefficient pour la variable {i + 1} : ")) for i in range(num_variables)]

# Obtenir le nombre de contraintes de l'utilisateur
num_constraints = int(input("Entrez le nombre de contraintes : "))

# Obtenir les coefficients de la matrice de contraintes de l'utilisateur
lhs = []
for i in range(num_constraints):
    coefficients = [float(input(f"Entrez le coefficient pour la variable {j + 1} dans la contrainte {i + 1} : ")) for j in range(num_variables)]
    lhs.append(coefficients)

# Obtenir les valeurs du côté droit des contraintes de l'utilisateur
rhs = [float(input(f"Entrez la valeur du côté droit pour la contrainte {i + 1} : ")) for i in range(num_constraints)]

# Définir les bornes pour chaque variable
bnd = [(0, None) for _ in range(num_variables)]

# Résoudre le problème de programmation linéaire
optimiser = linprog(c=obj,
                   A_ub=lhs,
                   b_ub=rhs,
                   bounds=bnd,
                   method='simplex')

# Afficher le résultat de l'optimisation
print(optimiser)

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
