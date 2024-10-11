# imports
import sys
import happybase

IP="node183679-env-1839015-etudiant-amina-marie.sh1.hidora.com"
PORT=11904
connexion = happybase.Connection(IP, PORT)
connexion.open()

nom_table = "streams"
colonne_familles = {
    'cf': dict
}

try:
    connexion.disable_table(nom_table)
    connexion.delete_table(nom_table)
except:
    pass

connexion.create_table(nom_table, colonne_familles)
table = connexion.table(nom_table)


# lire l'entrée standard: sys.stdin
lignes = sys.stdin

# variables pour les cumuls
current_year = None
current_stream = None

# boucler les les données
for ligne in lignes:

    # enlever les espaces
    ligne = ligne.strip()
    # diviser la ligne en parties (split ,)
    parties = ligne.split('\t') # tableau
    
    # stocker les données dans des variables
    # released_year
    released_year = parties[0]
    # streams
    streams = parties[1]

    # assembler
    try:
        streams = int(streams)
    except:
        continue
    
    # si regarder si notre current_year == year de la boucle // s'il existe
    if current_year and current_year == released_year:
        # incrementer le cumul
        current_stream += streams
        
    # sinon
    else:
        dic = {
            'cf:somme': current_stream
        }
        table.put(current_year, dic)
        # print()
        # réaffecter les nouvelles valeurs de la boucle
        current_stream = streams
        current_year = released_year
        
# affiche le dernier element
dic = {
    'cf:somme': current_stream
}

table.put(current_year, dic)
connexion.close()
