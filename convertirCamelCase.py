'''
076 - Convertir une chaîne de caractère en camelCase
Notions abordées : les boucles, les chaînes de caractères.

On continue avec les chaînes de caractères dans cet exercice dans lequel vous devez convertir
une phrase en un mot au format camelCase.

Le camelCase est une façon de formater une suite de mots pour que chaque mot soit séparé par une majuscule,
excepté le premier mot.

Dans ce cas-ci, votre script doit donc convertir la phrase 'Phrase en camel case' en 'phraseEnCamelCase'.
'''

phrase = "Le camelCase est une façon de formater une suite de mots pour que chaque mot soit séparé par une majuscule, excepté le premier mot"
phrase = phrase.title()
listePhrase = phrase.split()


mot = listePhrase.pop(0).lower()

listePhrase.insert(0, mot)
laPhrase = "".join(listePhrase)
print(laPhrase)

# Autre solution avec méthode capitalize et boucle for

phrase = "Phrase en camel case"
phrase_split = phrase.split()

resultat2 = [phrase_split.pop(0).lower()]

for mot in phrase_split:
    resultat2.append(mot.capitalize())

resultat_formate = "".join(resultat2)

print(resultat_formate)





