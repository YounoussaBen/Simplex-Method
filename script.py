# Importer la bibliothèque numpy pour les opérations matricielles
import numpy as np

# Définir la fonction objective et les contraintes sous forme de matrices
# Par exemple, pour le problème suivant:
# Maximiser z = 30x + 50y
# Sous les contraintes:
# 3x + 2y <= 1800
# x <= 400
# y <= 600
# x, y >= 0
# La fonction objective est:
c = np.array([30, 50])  # Un vecteur de taille n, où n est le nombre de variables

# Les contraintes sont:
A = np.array([[3, 2], [1, 0], [0, 1]])  # Une matrice de taille m x n, où m est le nombre de contraintes

b = np.array([1800, 400, 600])  # Un vecteur de taille m
signes = np.array(["<=", ">=", "<="])  # Un vecteur de taille m, contenant les signes des contraintes

# Définir le type de problème: maximisation ou minimisation
type = "max"  # Une chaîne de caractères, "max" pour maximisation, "min" pour minimisation

# Déterminer les dimensions des matrices
m, n = A.shape[0], len(c)

# Ecrire le système sous forme standard en ajoutant des variables d'écart
# 3x + 2y + s1 = 1800
# x + s2 = 400
# y + s3 = 600
# z, s1, s2, s3 >= 0

# La nouvelle fonction objective est:
if type == "max":  # Si on veut maximiser, on prend l'opposé de la fonction objective
    c = -c
c = np.append(c, np.zeros(m))  # On ajoute des zéros pour les variables d'écart

# Les nouvelles contraintes sont:
A = np.hstack((A, np.eye(m)))  # On ajoute des colonnes pour les variables d'écart

for i in range(m):
    if signes[i] == ">=":  # Si le signe est >=, on change le signe de la contrainte
        A[i, :] = -A[i, :]
        b[i] = -b[i]

b = b.reshape((m, 1))  # On transforme le vecteur b en une matrice colonne

# Construire le premier tableau correspondant à la forme standard
# Le tableau contient la fonction objective, les contraintes, et les variables de base
tableau = np.zeros((m + 1, n + m + 1))  # On crée une matrice de zéros de taille (m+1) x (n+m+1)
tableau[0, :-1] = c  # On met la fonction objective dans la première ligne, sauf la dernière colonne
tableau[1:, :-1] = A  # On met les contraintes dans les lignes suivantes, sauf la dernière colonne
tableau[1:, -1] = b.ravel()  # or b.ravel() # On met les termes constants dans la dernière colonne
base = list(range(n, n + m))  # On initialise la liste des variables de base (les variables d'écart)

# Définir une fonction pour afficher le tableau de façon lisible
def afficher_tableau(tableau, base):
    # On crée une liste des noms des variables
    variables = ["x" + str(i + 1) for i in range(n)] + ["s" + str(i + 1) for i in range(m)]

    # On affiche la fonction objective
    print("z = ", end="")
    for j in range(n + m):
        if tableau[0, j] != 0:  # On ignore les coefficients nuls
            print(f"{tableau[0, j]}{variables[j]} ", end="")  # On affiche le coefficient et le nom de la variable
    print()

    # On affiche les contraintes
    for i in range(1, m + 1):
        print(f"{variables[base[i - 1]]} = {tableau[i, -1]} ", end="")  # On affiche le nom de la variable de base et le terme constant
        for j in range(n + m):
            if tableau[i, j] != 0:  # On ignore les coefficients nuls
                print(f"- {tableau[i, j]}{variables[j]} ", end="")  # On affiche le coefficient et le nom de la variable avec un signe moins
        print()
    print()

# Afficher le premier tableau
print("Premier tableau:")
afficher_tableau(tableau, base)

# Définir une fonction pour effectuer une itération de l'algorithme du simplexe
def iteration(tableau, base):
    # Choisir la variable à introduire dans la base
    # On choisit la variable qui a le coefficient le plus négatif dans la fonction objective
    entrante = np.argmin(tableau[0, :-1])  # On récupère l'indice de la colonne correspondante

    # Choisir la variable à enlever de la base
    # On choisit la variable qui minimise le rapport entre le terme constant et le coefficient de la variable entrante
    # On ignore les coefficients négatifs ou nuls
    rapport = np.divide(tableau[1:, -1], tableau[1:, entrante])  # On calcule le rapport pour chaque contrainte
    rapport = np.where(tableau[1:, entrante] > 0, rapport, np.inf)  # On remplace les valeurs invalides par l'infini
    sortante = np.argmin(rapport) + 1  # On récupère l'indice de la ligne correspondante (en ajoutant 1 car on a ignoré la première ligne)

    # Encadrer le pivot
    # Le pivot est l'élément à l'intersection de la ligne sortante et de la colonne entrante
    sortante = np.argmin(rapport) + 1  # On récupère l'indice de la ligne correspondante (en ajoutant 1 car on a ignoré la première ligne)
    pivot = tableau[sortante, entrante]

    # Diviser la ligne du pivot par le pivot
    tableau[sortante, :] = tableau[sortante, :] / pivot

    # Calculer les valeurs des autres lignes
    for i in range(m + 1):
        if i != sortante:  # On ignore la ligne du pivot
            tableau[i, :] = tableau[i, :] - tableau[i, entrante] * tableau[sortante, :]  # On soustrait un multiple de la ligne du pivot

    # Mettre à jour la liste des variables de base
    base[sortante - 1] = entrante  # On remplace la variable sortante par la variable entrante

    # Retourner le nouveau tableau et la nouvelle base
    return tableau, base

# Tant que les coefficients de la fonction objective sont tous nuls ou négatifs, pour un problème de maximisation
# Ou tant que les coefficients de la fonction objective sont tous nuls ou positifs, pour un problème de minimisation
while (type == "max" and np.any(tableau[0, :-1] < 0)) or (type == "min" and np.any(tableau[0, :-1] > 0)):
    # Effectuer une itération de l'algorithme du simplexe
    tableau, base = iteration(tableau, base)

    # Afficher le tableau courant
    print("Tableau courant:")
    afficher_tableau(tableau, base)

# Afficher la solution optimale
print("Solution optimale:")
variables = ["x" + str(i + 1) for i in range(n)] + ["s" + str(i + 1) for i in range(m)]

for i in range(n + m):
    if i in base:  # Si la variable est dans la base, on affiche sa valeur
        print(f"{variables[i]} = {tableau[base.index(i) + 1, -1]}")
    else:  # Sinon, on affiche zéro
        print(f"{variables[i]} = 0")

if type == "max":  # Si on a maximisé, on change le signe de la valeur optimale de la fonction objective
    print(f"z = {-tableau[0, -1]}")
else:  # Sinon, on garde le même signe
    print(f"z = {tableau[0, -1]}")
