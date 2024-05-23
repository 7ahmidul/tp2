import csv
def pokemon_csv(fichier):
    pokemons = {}

    with open(fichier,newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            nom = row[0]
            stats = list(map(int,row[1:]))
            pokemons[nom]=stats
    return pokemons

pkmn = pokemon_csv("pokemon.csv")
for nom, stats in pkmn.items():
    print(nom ,stats)

print(isinstance(pkmn,dict))
print(isinstance(pkmn["Pikachu"],list))
print(isinstance(pkmn["Pikachu"][0],int))
