
texte = "Bonjour Udemy"
size = len(texte)

symbole1 = "-"
symbole2 = "|"

print(symbole1*size)
for lettre in texte:
    print(f"{symbole2}{lettre:^{size - 2}}{symbole2}")
print(symbole1*size)
