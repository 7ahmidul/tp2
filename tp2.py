import json
import csv

def read_json_and_write_csv(fichier_json, fichier_csv):
    with open(fichier_json, 'r') as f_json:
        data = json.load(f_json)

    with open(fichier_csv, 'w', newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerows(['reel', 'imaginaire'])

        for nb_complexes in data:
            writer.writerows(nb_complexes)


read_json_and_write_csv('data.json', 'output.csv')
