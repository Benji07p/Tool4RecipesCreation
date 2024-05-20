def create_dictionaries_from_list(values):
    # Liste pour stocker les dictionnaires
    dictionaries = []
    
    # Parcourir chaque valeur dans le tableau fourni par l'utilisateur
    for value in values:
        # Créer un dictionnaire formaté selon vos spécifications
        dictionary = {
            "output": "atum:coin_gold",
            "payment": {
                "item": value,
                "count": 1
            }
        }
        # Ajouter le dictionnaire à la liste
        dictionaries.append(dictionary)
    
    return dictionaries

def write_dictionaries_to_file(dictionaries, filename):
    # Ouvrir le fichier en mode écriture
    with open(filename, 'w') as file:
        # Parcourir chaque dictionnaire dans la liste
        for dictionary in dictionaries:
            # Écrire le dictionnaire sous forme de chaîne JSON dans le fichier
            file.write(f"{dictionary}\n")

def process_values(values):
    # Créer les dictionnaires à partir de la liste de valeurs
    dictionaries = create_dictionaries_from_list(values)
    
    # Nom du fichier à créer
    filename = 'output.txt'
    
    # Écrire les dictionnaires dans le fichier
    write_dictionaries_to_file(dictionaries, filename)
    
    print(f"Les dictionnaires ont été écrits dans le fichier {filename}")