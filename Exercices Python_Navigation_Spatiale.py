
import os 
import json 
import shutil




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


M = open(chemin_d_acces_missions, "r", encoding="utf-8")
data = json.load(M)
M.close()
#Affiche un résumé de chaque mission
if isinstance(data, dict):
    for valeur in data.values():
        if isinstance(valeur, list):
            data = valeur
            break
#Parcourt chaque mission et affiche ses informations
for m in data:
    id_m  = m.get("id")
    nom   = m.get("nom", m.get("name"))
    dest  = m.get("destination", "N/A")
    duree = m.get("duree_jours", m.get("duration_days"))
    eq    = m.get("equipage", m.get("crew_size"))
    bud   = m.get("budget_millions", m.get("budget"))
    print(f"[{id_m}] {nom} → {dest} | {duree} jours | Équipage : {eq} | Budget : {bud} M$")
    
#initialisation de la variable budget toutal
budget_total = 0

# Calcule  le **budget total** de toutes les missions
for m in data:
    budget = m.get("budget_millions", m.get("budget", 0))
    budget_total = budget_total + budget
#affiche le **budget total** de toutes les missions
print(f"\nBudget total de toutes les missions : {budget_total} M$")
 

#on part de None, la première mission trouvée servira de référence
mission_longue = None
mission_courte = None

for m in data:
    duree = m.get("duree_jours", m.get("duration_days", 0))

    # Première mission
    if mission_longue is None:
        mission_longue = m
        mission_courte = m

    elif duree > mission_longue.get("duree_jours", mission_longue.get("duration_days", 0)):
        mission_longue = m

    elif duree < mission_courte.get("duree_jours", mission_courte.get("duration_days", 0)):
        mission_courte = m


# Affichage des résultats
nom_long  = mission_longue.get("nom", mission_longue.get("name"))
duree_long = mission_longue.get("duree_jours", mission_longue.get("duration_days"))

nom_court  = mission_courte.get("nom", mission_courte.get("name"))
duree_court = mission_courte.get("duree_jours", mission_courte.get("duration_days"))

print(f"\nMission la plus longue : {nom_long} → {duree_long} jours")
print(f"Mission la plus courte : {nom_court} → {duree_court} jours")  


## 🟡 Tâche 4 — Gestion des exceptions : Chargement robuste  


def charger_json_securise(chemin):
    try:
        if not os.path.exists(chemin):
            raise FileNotFoundError
        
        if os.path.getsize(chemin) == 0:
            print(f"Erreur : le fichier '{chemin}' est vide.")
            return None
        
        with open(chemin, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        return data

    except FileNotFoundError:
        print(f"Erreur : le fichier '{chemin}' n'existe pas.")
        return None
# Gestion de l'erreur si le fichier contient un JSON invalide
    except json.JSONDecodeError:
        print(f"Erreur : le fichier '{chemin}' est mal formé (JSON invalide).")
        return None

    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None


# Chemin complet vers le fichier JSON
chemin_d_acces_mission_data = r"C:\Users\DELL\Downloads\mission_data\corps_celestes.json"
data = charger_json_securise(chemin_d_acces_mission_data)

print(data)


## 🟡 Tâche 5 — `os` avancé : Commandes système et gestion de fichiers 



# Dossier principal mission_data
base_path = r"C:\Users\DELL\Downloads\mission_data"

# Dossier rapports
rapports_path = os.path.join(base_path, "rapports")

# Fichier rapport
rapport_path = os.path.join(rapports_path, "rapport_systeme.txt")

# Vérifie que le dossier rapports existe
if not os.path.exists(rapports_path):
    os.makedirs(rapports_path)

# Création du rapport système
with open(rapport_path, "w", encoding="utf-8") as rapport:

    # Répertoire courant
    rapport.write("=== RÉPERTOIRE COURANT ===\n")
    rapport.write(os.getcwd() + "\n\n")

    # Variables d’environnement PYTHON / PATH
    rapport.write("=== VARIABLES D'ENVIRONNEMENT (PYTHON / PATH) ===\n")
    for cle, valeur in os.environ.items():
        if "PYTHON" in cle.upper() or "PATH" in cle.upper():
            rapport.write(f"{cle} = {valeur}\n")

    # Espace disque disponible
    rapport.write("\n=== ESPACE DISQUE ===\n")
    total, used, free = shutil.disk_usage(base_path)
    rapport.write(f"Espace total : {total // (1024**3)} Go\n")
    rapport.write(f"Espace utilisé : {used // (1024**3)} Go\n")
    rapport.write(f"Espace libre : {free // (1024**3)} Go\n")

print("Rapport système créé avec succès")
print(" Emplacement :", rapport_path)



    
    
    