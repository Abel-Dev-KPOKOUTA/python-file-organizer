import os 
import json 
import shutil 
from pathlib import Path 

path_downloads = str(Path.home() / 'Downloads')

with open('fichier.json','r', encoding='utf-8') as f :
    categories = json.load(f)


nbr_fichier=0
for file in os.listdir(path_downloads):
    path_file = os.path.join(path_downloads,file)
    
    if os.path.isdir(path_file):
        continue

    extension_file = os.path.splitext(file)[1].lower()

    file_categorie = None
    for categorie,extension in categories.items():
        if extension_file in extension :
            file_categorie = categorie
            break
    
    if file_categorie is None :
        print(f"La catégorie du fichier {file} n'a pas été retrouvé")
        continue

    dossier_destination = os.path.join(path_downloads,file_categorie)
    os.makedirs(dossier_destination, exist_ok=True)

    file_destination = os.path.join(dossier_destination,file)

    if os.path.exists(file_destination):
        base,ext = os.path.split(file)
        i=0
        while os.path.exists(file_destination):
            file_destination = os.path.join(dossier_destination,f"{base}_i{ext}")
            i+=1


    
