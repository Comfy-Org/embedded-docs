# Charger le jeu de données d'entraînement

Ce nœud charge un jeu de données d’entraînement encodé (latents et conditionnement) précédemment enregistré sur le disque. Il lit tous les fichiers de fragments de données d’un dossier de jeu de données sélectionné dans le répertoire `datasets` et renvoie les vecteurs latents combinés ainsi que les données de conditionnement pour une utilisation dans les flux de travail d’entraînement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `folder_name` | Jeu de données sauvegardé à charger, depuis le répertoire `datasets`. | COMBO | Oui | Une option par dossier de jeu de données trouvé dans le répertoire `datasets` |

Remarque : Les options de `folder_name` sont construites automatiquement en analysant le répertoire `datasets`. Un sous-dossier est répertorié comme jeu de données lorsqu’il contient un fichier `metadata.json` ou au moins un fichier `.safetensors`. Le dossier de jeu de données sélectionné est recherché dans tous les répertoires racine de jeux de données configurés. Le nœud lit tous les fichiers nommés `shard_*.pkl` dans le dossier sélectionné et lève une erreur si aucun fichier de fragment n’est trouvé.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latents` | Liste de dictionnaires latents, où chaque dictionnaire contient une clé `"samples"` avec un tenseur. | LATENT |
| `conditioning` | Liste de listes de conditionnement, où chaque liste interne contient les données de conditionnement pour l’échantillon correspondant. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/fr.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
