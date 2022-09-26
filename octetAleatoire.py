import random

liste = []
for i in range(1, 9):
    nbrAl = random.randint(0, 1)
    liste.append(str(nbrAl))

octet = "".join(liste)

print(octet)

# Solution plus adaptée (1 ligne) :

liste_random = [str(random.choice(range(2))) for _ in range(8)]

print("".join(liste_random))




