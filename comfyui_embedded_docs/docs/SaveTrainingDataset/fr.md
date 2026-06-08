Ce nœud enregistre un ensemble de données d'entraînement préparé sur le disque dur de votre ordinateur. Il prend des données encodées, comprenant des latentes d'image et leur conditionnement textuel correspondant, et les organise en plusieurs fichiers plus petits appelés *shards* pour une gestion plus facile. Le nœud crée automatiquement un dossier dans votre répertoire de sortie et enregistre à la fois les fichiers de données et un fichier de métadonnées décrivant l'ensemble de données.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latents` | Liste de dictionnaires latents provenant de MakeTrainingDataset. | LATENT | Oui | N/A |
| `conditioning` | Liste de listes de conditionnement provenant de MakeTrainingDataset. | CONDITIONING | Oui | N/A |
| `folder_name` | Nom du dossier pour enregistrer l'ensemble de données (dans le répertoire de sortie). (par défaut : "training_dataset") | STRING | Non | N/A |
| `shard_size` | Nombre d'échantillons par fichier *shard*. (par défaut : 1000) | INT | Non | 1 à 100000 |

**Remarque :** Le nombre d'éléments dans la liste `latents` doit correspondre exactement au nombre d'éléments dans la liste `conditioning`. Le nœud générera une erreur si ces comptes ne correspondent pas.

## Sorties

Ce nœud ne produit aucune donnée de sortie. Sa fonction est d'enregistrer des fichiers sur votre disque.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/fr.md)

---
**Source fingerprint (SHA-256):** `1b0108be7362c0cb8ba16ffbf94cf42be2d04159aacbabe1ff0890083d1733b3`
