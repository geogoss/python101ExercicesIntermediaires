'''
073 - Créer un générateur de mot de passe
Notions abordées : le module string, le module random.

Dans cet exercice, nous allons créer un générateur de mot de passe aléatoire.

À l'aide du module string et du module random, vous allez devoir générer un mot de passe aléatoire de la
longueur spécifiée dans la variable taille (ici, 8).

Votre mot de passe doit pouvoir contenir des lettres minuscules, majuscules, n'importe quel chiffre
de 0 à 9 et n'importe quel caractère spécial (!"#$%&' etc...).
'''

import string
import random


taille = 8

motDePasse = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

print("".join(random.choice(motDePasse) for _ in range(taille)))

# souvent, il faut récupérer le mot de passe :

Symbole = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
leMotDePasse = "".join(random.choice(Symbole) for _ in range(taille))
print(leMotDePasse)





