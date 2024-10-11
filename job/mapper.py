# imports
import sys

# lire l'entrée standard: sys.stdin
lignes = sys.stdin

# boucler les les données
for ligne in lignes:

    # enlever les espaces
    ligne = ligne.strip()
    # diviser la ligne en parties (split ,)
    parties = ligne.split(',') # tableau
    
    # stocker les données dans des variables
    # released_year
    released_year = parties[3]
    # streams
    streams = parties[8]
    
    try:
        released_year: int = int(released_year)
    except Exception:
        continue
    
    # OPTIONAL : filtre les données
    if released_year < 2000:
        continue
    
    # afficher les données
    print("%s\t%s" % (released_year, streams))