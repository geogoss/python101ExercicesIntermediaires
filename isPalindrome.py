'''
078 - Vérifier si une phrase est un palindrome
Notions abordées : les chaînes de caractères.

Dans cet exercice, nous allons vérifier si une phrase est un palindrome ou non.
Un palindrome est un mot ou une phrase qui peut se lire de la même façon dans les deux sens.

Dans cet exemple-ci, nous avons le palindrome 'Un roc cornu'.
Votre script devra donc vérifier si cette phrase est un palindrome, et donc dans ce cas-ci,
retourner la valeur True.

Aller plus loin : Essayez cette fois-ci de ne pas utiliser la fonction reversed.
'''

mot = "Un roc cornu"
mot2 = "test pour le fun"
mot3 = "aca"
mot4 = "sfdretgchdkjnzfuib"
'''
mot2 = list(mot2.replace(" ",""))
print(mot2)
inverse = "".join(mot2)
print(inverse)
'''

def palindrome(mot):
    mot = list(mot.replace(" ","").lower())
    palin = "".join(mot)
    drome = "".join(mot[::-1])
    print(palin)
    print(drome)
    if palin == drome:
        return True
    return False


print(palindrome(mot))

# Façon bcp plus efficace :
mot_lower = mot.lower().replace(" ", "")

if mot_lower == mot_lower[::-1]:
    print(True)
else:
    print(False)









