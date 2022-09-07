'''058 - Calculer l'année de naissance à partir d'un âge donné
Notions abordées : le module datetime.

Dans cet exercice, nous allons utiliser le module datetime pour calculer l'année de naissance de quelqu'un, à partir de son âge.

Dans cet exemple, nous allons prendre un âge de 25 ans.

Afin de ne pas fausser les résultats, nous allons également indiquer le mois de naissance afin de vérifier si la date d'anniversaire de la personne est passée ou non.'''

from datetime import datetime

age = 25
mois_de_naissance = 10
annee_actuelle = datetime.today().year
mois_actuelle = datetime.today().month
print(mois_actuelle)
print(annee_actuelle)

resultat = annee_actuelle - age - (1 if mois_actuelle < mois_de_naissance else 0)

print(resultat)


# Juste pour essayer
hour = datetime.today().hour
min = datetime.today().minute
sec = datetime.today().second

print(hour)
print(min)
print(sec)
