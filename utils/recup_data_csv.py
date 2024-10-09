import sys
import csv

# Créez un lecteur CSV pour gérer les données
csv_reader = csv.DictReader(sys.stdin) # ligne 131 csv

# Parcourez les lignes du CSV
for index, line in enumerate(csv_reader):
    
    # Extraire les champs du CSV
    track_name = line.get("track_name")
    artist_name = line.get("artist(s)_name")
    artist_count = line.get("artist_count")
    
    print("%i;%s;%s;%s" % (index, track_name, artist_name, artist_count)
)