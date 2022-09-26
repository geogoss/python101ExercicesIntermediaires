'''Vérifier si le mot de passe créé dans l'exo juste avant contient bien :

>=2 nombres
>=1 majuscule
>=8 caractères
'''

import string
import random


# Code pour générer un mot de passe
taille = 8
Symbole = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
leMotDePasse = "".join(random.choice(Symbole) for _ in range(taille))
print(leMotDePasse)

# Code pour vérifier le mot de passe

def verificateur_mdp(mdp):
    if len(leMotDePasse) >=8:
        if any(l.isupper() for l in mdp):
            if len([n for n in mdp if n.isdigit()]) >=2:
                print("Le mot de passe contient bien les caractères demandés !")
            else:
                print(f"Ce mot de passe contient bien 8 caractères et 1 majuscule \nmais il doit contenir au moins 2 nombres")
        else:
            print(f"Ce mot de passe contient bien 8 caractères \nMais il doit contenir 1 majuscule")
    else:
        print(f"Ce mot de passe ne contient {len(leMotDePasse)} ! \nIl doit en contenir au moins 8")


verificateur_mdp(leMotDePasse)


# Version simplifiée :
def verificateur_mdp2(mdp):
    if len(mdp) >= 8 and any(l.isupper() for l in mdp) and len([n for n in mdp if n.isdigit()]) >= 2:
        return True
    return False


succes = verificateur_mdp2(leMotDePasse)
print(succes)
