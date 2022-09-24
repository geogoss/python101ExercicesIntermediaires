from glob import glob
from pathlib import Path

dossierDownloads = Path("C:/Users/Geoffrey/Downloads")
dossierDesktop = Path("C:/Users/Geoffrey/Desktop")

fichiers = glob(f"{dossierDownloads}/**", recursive=True)
print(len(fichiers))

fichiers2 = glob(f"{dossierDesktop}/**", recursive=True)
print(len(fichiers2))


