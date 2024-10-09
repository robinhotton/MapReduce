# Exercices MapReduce

<br>

## Données

---

Le [Dataset Spotify_Most_Streamed_Songs.csv](https://www.kaggle.com/datasets/abdulszz/spotify-most-streamed-songs) provient de [kaggle](https://www.kaggle.com/). Un site d'entrainement de cours et de défis pour le Big Data et IA comportant des datasets divers et variés.

Plus d'information sur les données sur le site : https://www.kaggle.com/datasets/abdulszz/spotify-most-streamed-songs

<br>

## Questions

---

Pour réaliser ces différentes questions, vous devrez utiliser le comportement MapReduce de Hadoop grâce à ces deux fichiers :

- le mapper, pour filtrer les données
- le reducer, pour aggréger et exporter les données

Pour simuler le comportement du MapReduce en local avec python, vous pouvez utiliser cette commande :

```bash
cat fichier.txt | python mapper.py | sort | python reducer.py
```

<br>

### <u>Question 1 : Nombre total de streams par année</u>

Écrivez un job MapReduce qui calcule le nombre total de streams par année. Le **mapper** doit lire le fichier CSV, extraire l'année de sortie (`released_year`) et le nombre de streams (`streams`), puis émettre l'année en tant que clé et le nombre de streams en tant que valeur. Le **reducer** doit agréger le nombre total de streams par année.

**Mapper Output:**

- Clé : `released_year`
- Valeur : `streams`

**Reducer Output:**

- Clé : `released_year`
- Valeur : Total des streams pour cette année

<br>

### <u>Question 2 : Classement des artistes selon le nombre de streams</u>

Écrivez un job MapReduce qui calcule le nombre total de streams pour chaque artiste. Le **mapper** doit extraire le nom de l'artiste (`artist(s)_name`) et le nombre de streams, et émettre le nom de l'artiste en tant que clé et le nombre de streams en tant que valeur. Le **reducer** doit agréger le nombre total de streams par artiste.

**Mapper Output:**

- Clé : `artist(s)_name`
- Valeur : `streams`

**Reducer Output:**

- Clé : `artist(s)_name`
- Valeur : Total des streams de cet artiste

<br>

### <u>Question 3 : Nombre moyen de playlists contenant une chanson selon l'année de sortie</u>

Écrivez un job MapReduce qui calcule la moyenne du nombre de playlists contenant des chansons, regroupées par année de sortie. Le **mapper** doit extraire l'année de sortie (`released_year`) et le nombre de playlists Spotify (`in_spotify_playlists`), puis émettre l'année en tant que clé et le nombre de playlists en tant que valeur. Le **reducer** doit calculer la moyenne du nombre de playlists par année.

**Mapper Output:**

- Clé : `released_year`
- Valeur : `in_spotify_playlists`

**Reducer Output:**

- Clé : `released_year`
- Valeur : Moyenne des playlists pour cette année

<br>

### <u>Question 4 : Classement des chansons selon leur « danceability »</u>

Écrivez un job MapReduce qui classe les chansons selon leur pourcentage de **danceability** (`danceability_%`). Le **mapper** doit extraire le nom de la chanson (`track_name`) et la danceability, puis émettre le nom de la chanson en tant que clé et son score de danceability en tant que valeur. Le **reducer** n'est pas nécessaire si l'on se limite à une simple sortie triée en fonction de la valeur.

**Mapper Output:**

- Clé : `track_name`
- Valeur : `danceability_%`

**Reducer Output (facultatif)**:

- Clé : `track_name`
- Valeur : `danceability_%`, trié par ordre décroissant

<br>

### <u>Question 5 : Corrélation entre l'énergie musicale et la popularité</u>

Écrivez un job MapReduce qui examine la corrélation entre l'énergie d'une chanson (`energy_%`) et son rang dans les classements Spotify (`in_spotify_charts`). Le **mapper** doit extraire le pourcentage d'énergie (`energy_%`) et le rang dans les charts Spotify (`in_spotify_charts`), puis émettre le pourcentage d'énergie en tant que clé et le rang en tant que valeur. Le **reducer** pourrait calculer des statistiques basiques pour chaque niveau d'énergie.

**Mapper Output:**

- Clé : `energy_%`
- Valeur : `in_spotify_charts`

**Reducer Output:**

- Clé : `energy_%`
- Valeur : Statistiques sur les rangs des charts pour ce niveau d'énergie (par exemple, moyenne, médiane)

<br>

### <u>Question 6 : Identification des chansons « à succès » multi-plateformes</u>

Écrivez un job MapReduce qui identifie les chansons présentes dans au moins trois plateformes (Spotify, Apple Music, Deezer, Shazam) et ayant atteint un classement dans les charts (non nul dans au moins trois des colonnes `in_spotify_charts`, `in_apple_charts`, `in_deezer_charts`, `in_shazam_charts`). Le **mapper** doit extraire les informations pertinentes sur les classements des chansons, puis émettre le nom de la chanson en tant que clé et un indicateur binaire pour chaque plateforme. Le **reducer** doit vérifier si la chanson est présente sur au moins trois plateformes et, si oui, la considérer comme un succès multi-plateformes.

**Mapper Output:**

- Clé : `track_name`
- Valeur : Indicateurs binaires pour chaque plateforme (1 si présent dans les charts, 0 sinon)

**Reducer Output:**

- Clé : `track_name`
- Valeur : 1 si la chanson est présente dans au moins trois plateformes, sinon 0