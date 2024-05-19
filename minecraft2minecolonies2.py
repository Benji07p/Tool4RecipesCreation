import json
from collections import Counter

# Dictionnaire de mappage des tags aux items
tag_to_item_map = {
    "forge:ingots/bronze": "electrodynamics:ingotbronze",
    "minecraft:planks": "minecraft:oak_planks",
    "forge:cobblestone": "minecraft:cobblestone",
    'forge:ingots/iron': 'minecraft:iron_ingot',
    'forge:ingots/gold': 'minecraft:gold_ingot',
    'forge:gems/diamond': 'minecraft:diamond',
    'forge:ingots/copper': 'minecraft:copper_ingot',
    'forge:ingots/steel': 'electrodynamics:ingotsteel',
    'forge:ingots/silver': 'electrodynamics:ingotsilver',
    'forge:ingots/tin': 'electrodynamics:ingottin',
    'forge:plates/iron': 'electrodynamics:plateiron',
    'forge:rods/wooden': 'minecraft:stick',
    'forge:nuggets/iron': 'minecraft:iron_nugget',
    'forge:nuggets/gold': 'minecraft:gold_nugget',
    'forge:feathers': 'minecraft:feather',
    'magistuarmory:plume_decorations': 'magistuarmory:plume_middle_decoration'
}

def transform_json(input_file, output_file):
    # Lire le fichier JSON d'entrée
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Extraire les informations nécessaires
    pattern = data["pattern"]
    key = data["key"]
    result_item = data["result"]["item"]
    if "count" in data["result"]:
        count_item_final = data["result"]["count"]
    else:
        count_item_final = 1

    # Compter les occurrences de chaque élément dans le pattern
    element_counts = Counter()
    for row in pattern:
        for char in row:
            if char in key:
                element_data = key[char]
                # Vérifier si c'est un item ou un tag et l'ajouter au compteur
                if "item" in element_data:
                    element_counts[element_data["item"]] += 1
                elif "tag" in element_data:
                    tag = element_data["tag"]
                    if tag in tag_to_item_map:
                        element_counts[tag_to_item_map[tag]] += 1
                    else:
                        print(f"Warning: No item mapping found for tag {tag}")

    # Créer la liste des inputs
    inputs = [{"item": item, "count": count} for item, count in element_counts.items()]
    
    # Créer la nouvelle structure JSON
    transformed_data = {
        "type": "recipe",
        "crafter": "blacksmith_crafting",
        "inputs": inputs,
        "result": result_item,
        "count": count_item_final,
        "intermediate": "minecraft:air",
        "min-building-level": 1,
        "show-tooltip": True
    }
    
    # Écrire le fichier JSON de sortie
    with open(output_file, 'w') as file:
        json.dump(transformed_data, file, indent=4)

# Nom des fichiers d'entrée et de sortie
input_file = 'wood_ellipticalshield.json'
output_file = 'wood_ellipticalshield1.json'

# Appeler la fonction de transformation
transform_json(input_file, output_file)
