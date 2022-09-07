symbole = "$"

taille = 5

for i in range(1, taille + 1):
    espaces = " " * (taille - i)
    print(espaces + (symbole + " ") * i)

