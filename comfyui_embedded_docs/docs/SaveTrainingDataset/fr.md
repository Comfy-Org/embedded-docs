# Enregistrer l'ensemble d'entraînement

---

Ce nœud enregistre un jeu de données d'entraînement préparé sur le disque dur de votre ordinateur. Il prend des données encodées, comprenant les latents d'image et leur conditionnement textuel correspondant, et les organise dans plusieurs fichiers plus petits appelés shards pour une gestion plus facile. Le nœud crée automatiquement un dossier dans le répertoire datasets et enregistre à la fois les fichiers de données shard et un fichier de métadonnées décrivant le jeu de données.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latents` | Liste de dictionnaires latents provenant de MakeTrainingDataset. | LATENT | Oui | N/A |
| `conditioning` | Liste de listes de conditionnement provenant de MakeTrainingDataset. | CONDITIONING | Oui | N/A |
| `folder_name` | Nom du dossier dans lequel enregistrer le jeu de données, dans le répertoire datasets. Les sous-dossiers comme 'project/run1' sont autorisés. (défaut : "training_dataset") | STRING | Oui | N/A |
| `shard_size` | Nombre d'échantillons par fichier shard. (défaut : 1000) | INT | Oui | 1 à 100000 |

**Remarque :** Le nombre d'éléments dans la liste `latents` doit correspondre exactement au nombre d'éléments dans la liste `conditioning`. Le nœud génère une erreur si ces comptages ne correspondent pas. Le `folder_name` doit désigner un sous-dossier du répertoire datasets : le dossier datasets racine lui-même, ainsi que tout chemin qui en sort (comme '..' ou un chemin absolu), est rejeté.

## Sorties

Ce nœud ne produit aucune donnée de sortie. Il enregistre le jeu de données sous forme de fichiers shard numérotés (par exemple `shard_0000.pkl`) et d'un fichier `metadata.json` dans le dossier choisi du répertoire datasets.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/fr.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
