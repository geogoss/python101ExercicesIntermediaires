import math
import string


employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]

print(len(employes))

def separation(employes):
    total = len(employes)
    firstMoitie = total//2 if total % 2 == 0 else math.ceil(total/2)
    secondMoitie = total - firstMoitie

    print(employes[0:firstMoitie])
    print(employes[firstMoitie::])

separation(employes)