import sys

# Initialiser les variables
current_year = None
current_streams = 0

# lire le flux d'entrée
for line in sys.stdin:
    line = line.strip()
    year, streams = line.split(";")
    
    try:
        year = int(year)
        streams = int(streams)
    except ValueError:
        continue
    
    # Si nous changeons d'année, afficher les résultats de l'année précédente
    if current_year is not None and year != current_year:
        print(f"{current_year};{current_streams}")
        current_streams = 0
    
    # Mettre à jour l'année courante et les streams
    current_year = year
    current_streams += streams

# Afficher la dernière année
if current_year is not None:
    print(f"{current_year};{current_streams}")
