import csv
import sys

# Créez un lecteur CSV pour gérer les données
csv_reader = csv.DictReader(sys.stdin)

# Parcourez les lignes du CSV
for line in csv_reader:
    
    # Extraire les champs du CSV
    released_year = line.get("released_year")
    streams = line.get("streams")
    
    print("%s;%s" % (released_year, streams)
)