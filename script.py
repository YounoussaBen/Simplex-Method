import cvxpy as cp
import numpy as np

# Obtenir le nombre de variables et de contraintes
num_vars = int(input("Entrez le nombre de variables : "))
num_constraints = int(input("Entrez le nombre de contraintes : "))

# Choisissez la direction de l'optimisation
optimization_direction = input("Voulez-vous maximiser ou minimiser ? Entrez 'max' ou 'min' : ")

# Définir les variables
x = cp.Variable(num_vars, nonneg=True)

# Obtenir les coefficients pour la fonction objectif
coefficients_objectif = []
for i in range(num_vars):
    coeff = float(input(f"Entrez le coefficient pour la variable x[{i}] : "))
    coefficients_objectif.append(coeff)

# Définir la fonction objectif en fonction du choix de l'utilisateur
if optimization_direction == 'max':
    objectif = cp.Maximize(cp.sum([coefficients_objectif[i] * x[i] for i in range(num_vars)]))
elif optimization_direction == 'min':
    objectif = cp.Minimize(cp.sum([coefficients_objectif[i] * x[i] for i in range(num_vars)]))
else:
    raise ValueError("Direction d'optimisation invalide. Veuillez entrer 'max' ou 'min'.")

# Ajouter des contraintes
contraintes = []
for _ in range(num_constraints):
    coefficients_contrainte = []
    for i in range(num_vars):
        coeff = float(input(f"Entrez le coefficient pour x[{i}] dans la contrainte : "))
        coefficients_contrainte.append(coeff)
    valeur_contrainte = float(input("Entrez la valeur de la contrainte : "))
    contraintes.append(cp.sum([coefficients_contrainte[i] * x[i] for i in range(num_vars)]) <= valeur_contrainte)

# Créer et résoudre le problème
prob = cp.Problem(objectif, contraintes)
prob.solve(solver=cp.ECOS)

print("\n\n***********************************************************\n\n")

# Afficher les résultats
if optimization_direction == 'max':
    print("Valeur maximale :", prob.value)
elif optimization_direction == 'min':
    print("Valeur minimale :", prob.value)

print("Solution optimale :", x.value)

print("\n\n***********************************************************")
