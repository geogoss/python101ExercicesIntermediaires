import os
from pathlib import Path
import time

dossier = Path.cwd()
dossier = dossier.parent
print(dossier)

dossier_a_surveiller = "python"


attente = input("Entrez un temps de rafraichissement :")

while dossier_a_surveiller not in os.listdir(dossier):
    print("Dossier introuvable ...")
    time.sleep(int(attente))
print("trouvé")





