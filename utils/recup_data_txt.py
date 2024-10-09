import sys

# Parcourez les lignes du CSV
for index, line in enumerate(sys.stdin):
    line = line.strip()
    line = line.split(",")
    
    # Extraire les champs du CSV
    track_name = line[0]
    artist_name = line[1]
    artist_count = line[2]
    
    print("%i;%s;%s;%s" % (index, track_name, artist_name, artist_count)
)