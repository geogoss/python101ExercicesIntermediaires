'''077 - Inverser l'ordre des mots dans une phrase
Notions abordées : les chaînes de caractères, les boucles.

On reprend un exercice que nous avons effectué plus tôt dans la formation mais cette fois-ci avec une phrase.

Il est question ici d'inverser l'ordre des mots dans la phrase. Votre phrase devra, comme une phrase normalement
construite, commencer par une majuscule.

Nous avons ici la phrase 'Bonjour tout le monde', votre script devra donc retourner la
phrase 'Monde le tout bonjour'.'''

phrase = "Bonjour tout le monde"

phraseSplit = phrase.lower().split()[::-1]
laPhrase = " ".join(phraseSplit).capitalize()
print(laPhrase)


# Avec une ligne de plus -> trop de lignes pfffff
'''
phraseSplit = phrase.lower().split()
inversePhrase = phraseSplit[::-1]
premierMot = inversePhrase.pop(0).capitalize()
inversePhrase.insert(0, premierMot)
laPhrase = " ".join(inversePhrase)
print(laPhrase)
'''





