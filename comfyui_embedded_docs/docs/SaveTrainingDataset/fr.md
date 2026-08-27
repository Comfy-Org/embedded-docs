# Enregistrer l'ensemble d'entraînement

Ce nœud enregistre un jeu de données d’entraînement encodé sur le disque pour un chargement efficace pendant l’entraînement. Il prend les latents d’image et leur conditionnement textuel correspondant, les divise en fichiers plus petits appelés shards, puis les stocke dans un dossier à l’intérieur du répertoire datasets. Il écrit également un fichier de métadonnées décrivant le jeu de données.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latents` | Liste de dictionnaires de latents provenant de MakeTrainingDataset. | LATENT | Oui | N/A |
| `conditioning` | Liste de listes de conditionnement provenant de MakeTrainingDataset. | CONDITIONING | Oui | N/A |
| `folder_name` | Nom du dossier dans lequel enregistrer le jeu de données, à l’intérieur du répertoire datasets. Les sous-dossiers comme `project/run1` sont autorisés. (par défaut : `"training_dataset"`) | STRING | Oui | N/A |
| `shard_size` | Nombre d’échantillons par fichier shard. (par défaut : 1000) | INT | Oui | 1 à 100000 |

**Remarque :** Le nombre d’éléments dans `latents` doit correspondre exactement au nombre d’éléments dans `conditioning` ; le nœud lève une erreur si ces nombres ne correspondent pas. Le `folder_name` doit désigner un sous-dossier du répertoire datasets (par exemple `my_dataset`) — il ne peut pas être le répertoire datasets lui-même, et les noms de dossier qui résoudraient en dehors du répertoire datasets sont rejetés.

## Sorties

Ce nœud ne produit aucune donnée de sortie. Sa fonction est d’enregistrer des fichiers sur votre disque. Chaque shard est enregistré sous la forme d’un fichier `shard_XXXX.pkl` dans le dossier choisi, et un fichier `metadata.json` enregistre le nombre total d’échantillons, le nombre de shards et la taille des shards.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/fr.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
