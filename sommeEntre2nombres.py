'''059 - Calculer la somme des nombres entre deux nombres
Notions abordées : la fonction sum, la fonction range.

Dans cet exercice, nous allons calculer la somme des nombres entre deux nombres.

Dans cet exemple-ci, nous prenons les nombres 2 et 6, le résultat de votre script doit donc être 20 (2 + 3 + 4 + 5 + 6).

Attention : votre script doit fonctionner peu importe l'ordre dans lequel vous donnez les nombres : somme(2, 6) et somme(6, 2) doivent retourner le même résultat !'''


def somme(a, b):
    print(sum(range(min(a, b), max(a, b) + 1)))

print(somme(7, 6))
