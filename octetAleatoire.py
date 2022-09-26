import random

liste = []
for i in range(1, 9):
    nbrAl = random.randint(0, 1)
    liste.append(str(nbrAl))

octet = "".join(liste)

print(octet)





