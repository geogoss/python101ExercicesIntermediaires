'''
age du chien
si chien a moins ou 2ans alors  age * 10.5
si chien a plus de  2 ans alors  21 + (age - 2) * 4
'''


while True:
    age_chien = int(input("Quel age a le chien ?"))
    if age_chien <= 0:
        print("Donnez une valeur positive !!!")
        continue
    if age_chien <= 2:
        print(f"Votre chien a {age_chien*10.5} ans jeunes ")
    elif age_chien > 2:
        print(f"Votre chien a {21 + (age_chien-2)*4} ans vieux ")
    break


