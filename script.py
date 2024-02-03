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
print("\nRésultat de l'optimisation :")
print(f"Équation : {obj[0]}*x1", end="")
for i in range(1, num_variables):
    print(f" + {obj[i]}*x{i + 1}", end="")
print("\nContraintes :")
for i in range(num_constraints):
    print(f"{lhs[i][0]}*x1", end="")
    for j in range(1, num_variables):
        print(f" + {lhs[i][j]}*x{j + 1}", end="")
    print(f" <= {rhs[i]}")
print("Conditions : x1, x2, x3, ... >= 0")

print("\nOptimisation terminée avec succès.")
print(f"La valeur optimale de la fonction objectif est {optimiser.fun}.")

# Afficher les résultats détaillés
print("\nDétails de l'optimisation :")
print(optimiser)
