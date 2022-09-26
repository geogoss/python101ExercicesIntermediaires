'''
075 - Compter le nombre d'occurrence d'un mot dans un texte
Notions abordées : les chaînes de caractères.

Dans cet exercice, nous allons compter le nombre d'occurrences du mot 'elit' dans
le texte en Lorem Ipsum contenu dans la variable lorem.

Dans cet extrait de texte, le mot apparaît une seule fois, votre script doit donc retourner le nombre 1.
'''

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore " \
        "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi " \
        "ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit " \
        "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, " \
        "sunt in culpa qui officia deserunt mollit anim id est laborum."

lorem = lorem.replace(",", "").replace(".", "")
elit = lorem.split()

t = 0
for i in elit:
    if i == "elit":
        t += 1
print(t)

# Ceci fait moins de ligne de code !!!
print(elit.count("elit"))
