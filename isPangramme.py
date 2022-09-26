'''
079 - Vérifier si une phrase est un pangramme
Notions abordées : les chaînes de caractères, les boucles.

Encore un exercice avec un mot barbare que vous n'avez peut-être jamais entendu de votre vie.
Un pangramme est une phrase qui contient toutes les lettres de l'alphabet au moins une fois.

La phrase que nous utiliserons dans cet exercice est la suivante :
"Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre".

Vous devez donc vérifier si cette phrase est bien un pangramme, et si c'est le cas, afficher la phrase :
"La phrase est un Pangramme".
'''

import string

phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"
phraseModified = phrase.lower()


alphabet = list(string.ascii_lowercase)

for i in phrase:
    if i in alphabet:
        alphabet.remove(i)
print(alphabet)

if alphabet:
    print("La phrase n'est pas un pangramme")
else:
    print("La phrase est un pangramme")




