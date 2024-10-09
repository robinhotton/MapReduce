import sys
import happybase


# Configurer la connexion à HBase
IP = ''
PORT = 0 # Port public couplé au port privé 9090 de HBase
connection = happybase.Connection(IP, PORT) 
connection.open()


hbase_table_name = ''
try:
    # Supprimer la table HBase si elle existe déjà
    connection.disable_table(hbase_table_name)
    connection.delete_table(hbase_table_name)
except Exception:
    pass


# Créer une table HBase avec des column families
column_families = {
    'cf1': dict(),
    'cf2': dict()
}
connection.create_table(hbase_table_name, column_families)
table = connection.table(hbase_table_name)


# boucler sur les données
for index, line in enumerate(sys.stdin):
    line = line.strip()
    line = line.split(',')
    
    # Extraire et convertir les champs en bytes
    index = b'%i' % index
    data = {
        b'cf1:track_name': b'%s' % line[0],
        b'cf2:artist_name':  b'%s' % line[1],
        b'cf2:artist_count':  b'%s' % line[2]
    }
    
    # Insérer les données dans HBase
    table.put(index, data)