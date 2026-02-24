> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/fr.md)

Ce nœud enregistre un jeu de données d'entraînement préparé sur le disque dur de votre ordinateur. Il prend des données encodées, qui incluent des latents d'image et leur conditionnement texte correspondant, et les organise en plusieurs fichiers plus petits appelés *shards* pour une gestion plus facile. Le nœud crée automatiquement un dossier dans votre répertoire de sortie et y enregistre à la fois les fichiers de données et un fichier de métadonnées décrivant le jeu de données.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Oui | N/A | Liste de dictionnaires de latents provenant de MakeTrainingDataset. |
| `conditioning` | CONDITIONING | Oui | N/A | Liste de listes de conditionnement provenant de MakeTrainingDataset. |
| `folder_name` | STRING | Non | N/A | Nom du dossier pour enregistrer le jeu de données (à l'intérieur du répertoire de sortie). (par défaut : "training_dataset") |
| `shard_size` | INT | Non | 1 à 100000 | Nombre d'échantillons par fichier *shard*. (par défaut : 1000) |

**Note :** Le nombre d'éléments dans la liste `latents` doit correspondre exactement au nombre d'éléments dans la liste `conditioning`. Le nœud générera une erreur si ces nombres ne correspondent pas.

## Sorties

Ce nœud ne produit aucune donnée en sortie. Sa fonction est d'enregistrer des fichiers sur votre disque.
