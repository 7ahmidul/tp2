import json
import csv

def read_json_et_write_csv(fichier_json, fichier_csv):
    with open(fichier_json, 'r') as f_json:
        data = json.load(f_json)

    with open(fichier_csv, 'w', newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(['reel', 'imaginaire'])

        for nb_complexes in data:
            writer.writerow(nb_complexes)


read_json_et_write_csv('data.json', 'resultat.csv')
print("Le fichier resultat.csv est crée avec succès")