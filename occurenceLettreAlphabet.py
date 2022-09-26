import string

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum."""


alphabet = string.ascii_lowercase
resultat = dict(zip(alphabet, [0] * len(alphabet)))
print(resultat)

for lettre in lorem.lower():
    if resultat.get(lettre) is not None:
        resultat[lettre] += 1

print(resultat)


