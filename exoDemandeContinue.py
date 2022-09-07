'''nbr_de_o = 0
while True:
    demande = input("Voulez-vous continuer ? o/n")

    if demande != "o" and demande != "n":
        print(f"Le compteur est maintenant à {nbr_de_o}")
        print("Répondre par o ou n !!!")
        continue
    if demande == "o":
        nbr_de_o += 1
        print(f"Le compteur est maintenant à {nbr_de_o}")
        continue
    else:
        print("Ok on arrête, merci d'avoir joué")
        print(f"Le compteur était à {nbr_de_o}")
        break'''

i = 0
continuer = "o"

while continuer == "o":
    print(f"Le compteur est maintenant à {i}")
    continuer = input("Voulez-vous continuer ? o/n ")
    i += 1




