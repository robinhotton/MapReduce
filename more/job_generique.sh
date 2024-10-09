#!/bin/bash

# /!\ Il faut que le Thrift soit lancé dans les slaves /!\
# Lancer le script: ./lance_srv_slaves.sh depuis la VM, pas hadoop-master

# Il faut que les services dfs, Yarn, HBase et Thrift soient lancés dans hadoop-master
start-dfs.sh                 # contenu dans ./start-hadoop.sh
start-yarn.sh                # contenu dans ./start-hadoop.sh
start-hbase.sh               # contenu dans ./services_hbase_thrift.sh
hbase-daemon.sh start thrift # contenu dans ./services_hbase_thrift.sh

# creation des variables
file_input=""
dir_output=""
mapper=""
reducer=""

# Créer le répertoire input et copier les données dedans
hdfs dfs -mkdir -p input
hdfs dfs -put $file_input input

# Supprimer le répertoire s'il existe
hdfs dfs -rm -r output/$dir_output

# Lancer le job MapReduce
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-file $mapper -mapper "python3 $mapper" \
-file $reducer -reducer "python3 $reducer" \
-input input/$file_input \
-output output/$dir_output