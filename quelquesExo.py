
'''065 - Trouvez tous les diviseurs d'un nombre
Notions abordées : les boucles, les opérateurs mathématiques.

Dans cet exercice, nous cherchons tous les diviseurs d'un nombre, dans ce cas-ci, le nombre 50.

Les diviseurs du nombre 50 correspondent à tous les nombres par lesquels on peut diviser 50 sans qu'il n'y ait de reste à la division.

Par exemple, 25 est un diviseur de 50 (car 50 / 25 = 2, et il reste 0).'''


nombre = 50

a = 50 % 2
print(a)
diviseurs = []
for i in range(1, 51):
    if 50 % i == 0:
        diviseurs.append(i)
print(diviseurs)

'''066 - Trouver les nombres divisibles par 7 mais qui ne sont pas des multiples de 3
Notions abordées : les boucles, les opérateurs mathématiques, les structures conditionnelles

Le but de cet exercice est de trouver tous les nombres de 0 à 1000 qui sont divisibles par 7 mais ne sont pas des multiples de 3.

Par exemple, le nombre 14 est divisible par 7 (car 14 / 7 = 2, il reste 0), mais n'est pas un multiple de 3 (car 14 / 3 ne retourne pas un nombre entier).

Pour valider l'exercice, vous devez récupérer tous ces nombres dans la liste nombres.'''

nombres = []

for i in range(1, 1001):
    if i % 7 == 0 and i % 3 != 0:
        nombres.append(i)
print(nombres)

print(959/3)

'''067 - Calculer la factorielle d'un nombre
Notions abordées : les boucles.

Dans cet exercice, nous cherchons la factorielle d'un nombre, dans ce cas-ci le nombre 5.

La factorielle de 5 est égal à 120 (car 1 x 2 x 3 x 4 x 5 = 120).

Votre script doit aussi gérer le cas dans lequel le nombre de départ est 0 (la factorielle de 0 est égale à 1).'''

nombre = 5
def fact(n):
    if n == 0:
        f = 1
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
    print(f)

fact(5)
