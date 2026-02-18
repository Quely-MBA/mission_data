
import os 
import json 




## 🟢 Tâche 1 — Lecture de fichiers texte : Le journal de bord

# Ouvre le fichier `mission_data/journal_bord.txt` en lecture.Ouvre le fichier `mission_data/journal_bord.txt` en lecture.

# Ouvrir le fichier en lecture
with open(r"C:\Users\DELL\Downloads\mission_data\journal_bord.txt", 'r', encoding='utf-8') as fichier:
#Affiche le nombre total de lignes (entrées du journal)
    lignes = fichier.readlines()
    nbre_lignes = len(lignes)
    print(f"Nbre total de lignes : {nbre_lignes}")
    lignes_alerte = []
    for ligne in lignes:
        if "alerte" in ligne.lower():
            lignes_alerte.append(ligne)
            print(ligne.strip()) #Affiche **uniquement les lignes contenant le mot Alerte
            lignes_alerte.append(ligne)

#Écrit ces lignes d'alerte dans un nouveau fichier
with open(r"C:\Users\DELL\Downloads\mission_data\alertes.txt", 'w', encoding='utf-8') as fichier_sortie:
    for ligne in lignes_alerte:
        fichier_sortie.write(ligne + '\n')

print(f"\n {len(lignes_alerte)} lignes d'alerte écrites dans le fichier")


## 🟢 Tâche 2 — Le module `os` : Exploration du dossier mission


# Vérifie que le dossier `mission_data/` existe. Si non, affichez une erreur.

if not os.path.exists(r"C:\Users\DELL\Downloads\mission_data"):
    print(" ERREUR : Le dossier Mission_data n'existe pas ")
else:
    print("Le dossier Mission_data existe")
    
# Liste **tous les fichiers** du dossier avec leur taille en Ko.

fichiers = os.listdir(r"C:\Users\DELL\Downloads\mission_data")
for fichier in fichiers:
    chemin_du_fichier = os.path.join(r"C:\Users\DELL\Downloads\mission_data", fichier)
    if os.path.isfile(chemin_du_fichier):
        taille_octets = os.path.getsize(chemin_du_fichier)
        taille_ko = taille_octets / 1024
        print(f"{fichier} - {taille_ko:.2f} Ko")

#Crée un sous-dossier `mission_data/rapports/` s'il n'existe pas déjà

chemin_d_acces_mission_data = r"C:\Users\DELL\Downloads\mission_data"
  
chemin_d_acces_rapports = os.path.join(chemin_d_acces_mission_data, "rapports")
if not os.path.exists(chemin_d_acces_rapports):
    os.makedirs(chemin_d_acces_rapports)
    print(" Dossier rapports  vients d'etre créé")
else:
    print(" Dossier rapports existe déjà")  
     
#Crée un sous-dossier `mission_data/archives/` s'il n'existe pas déjà.

chemin_d_acces_archives = os.path.join(chemin_d_acces_mission_data, "archives")
if not os.path.exists(chemin_d_acces_archives): 
    os.makedirs(chemin_d_acces_archives)
    print(" le dossier archive vients d'etre créé")
else:
    print("le dossier archives existe déjà")
    
#Affiche l'arborescence résultante 
    

elements = os.listdir(chemin_d_acces_mission_data)
for element in elements:
    chemin_element = os.path.join(chemin_d_acces_mission_data, element)
    if os.path.isdir(chemin_element):
        print(f" 📁{element}/")
    else:
        print(f"  📄{element}")
        
print(" Arborescence de mission data :")

## 🟢 Tâche 3 — JSON basique : Charger et afficher les missions

chemin_d_acces_missions = r"C:\Users\DELL\Downloads\mission_data\mission_data_missions.json"

# Charge le fichier missions.json
# Charge le fichier missions.json
with open(chemin_d_acces_missions, 'r', encoding='utf-8') as fichier:
    data = json.load(fichier)
    missions = data
   
print("📋 Résumé des missions :")
print("-" * 80)

for mission in missions:
    code = mission["code"]
    nom = mission["nom"]
    destination = mission["destination"]
    duree = mission["duree_jours"]
    equipage = mission["equipage"]
    budget = mission["budget_millions"]
    
    