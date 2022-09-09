import math

employes = sorted(["Pierre", "Marie", "Julien", "Astrid", "Zoé", "Geoffrey", "Gerard", "George", "Alain", "Bertrand"])


def compare(a, b):
    lettre_nom1 = list(a.lower())
    lettre_nom2 = list(b.lower())

    if len(lettre_nom1) > len(lettre_nom2):
        nombre_lettre_compare = len(lettre_nom2)
    else:
        nombre_lettre_compare = len(lettre_nom1)
    #print(nombre_lettre_compare)

    lettre_identique = []
    for i in range(nombre_lettre_compare):
        if lettre_nom1[i] == lettre_nom2[i]:
            lettre_identique.append(lettre_nom1[i])
        else:
            break
    nbr_lettre = len(lettre_identique)
    return nbr_lettre

def separation(employes):
    total = len(employes)
    firstMoitie = total//2 if total % 2 == 0 else math.ceil(total/2)
    #secondMoitie = total - firstMoitie

    #print(employes[0:firstMoitie])
    #print(employes[firstMoitie::])

    # on peut faire ceci
    dernier_employe_premiere_moitie = employes[0:firstMoitie][-1]
    premier_employe_deuxieme_moitie = employes[firstMoitie::][0]
    separateur_de_lettre = compare(dernier_employe_premiere_moitie, premier_employe_deuxieme_moitie) + 1

    print(f"Employés de A à {dernier_employe_premiere_moitie[0:separateur_de_lettre]} : {employes[:firstMoitie]} ")
    print(f"Employés de {premier_employe_deuxieme_moitie[0:separateur_de_lettre]} à {premier_employe_deuxieme_moitie[0:1]} : {employes[firstMoitie::]}")

    print("-"*100)

    # Ou on peut faire ceci mais c'est plus difficile de s'y retrouver
    print(f"Employés de A à {employes[0:firstMoitie][-1][0:compare(employes[0:firstMoitie][-1], employes[firstMoitie::][0]) + 1]} : {employes[:firstMoitie]}")
    print(f"Employés de {employes[firstMoitie::][0][0:compare(employes[0:firstMoitie][-1], employes[firstMoitie::][0]) + 1]} à {employes[firstMoitie::][-1][0:1]} : {employes[firstMoitie::]}")





separation(employes)


