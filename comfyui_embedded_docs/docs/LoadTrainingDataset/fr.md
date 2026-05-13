> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/fr.md)

Ce nœud charge un ensemble de données d'entraînement encodé préalablement sauvegardé sur le disque. Il recherche et lit tous les fichiers de fragments de données d'un dossier spécifié dans le répertoire de sortie de ComfyUI, puis renvoie les vecteurs latents combinés et les données de conditionnement pour une utilisation dans les workflows d'entraînement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `folder_name` | STRING | Oui | N/A | Nom du dossier contenant l'ensemble de données sauvegardé, situé dans le répertoire de sortie de ComfyUI (par défaut : "training_dataset"). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `latents` | LATENT | Une liste de dictionnaires latents, où chaque dictionnaire contient une clé `"samples"` avec un tenseur. |
| `conditioning` | CONDITIONING | Une liste de listes de conditionnement, où chaque liste interne contient les données de conditionnement pour un échantillon correspondant. |

---
**Source fingerprint (SHA-256):** `0a07c97e2c6a32f77cd21ea7dbdd33e06fad82285696b88122fef369307e133d`
