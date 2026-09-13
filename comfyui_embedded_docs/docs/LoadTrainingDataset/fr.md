# Charger le jeu de données d'entraînement

Ce nœud charge un jeu de données d'entraînement encodé (latents et conditionnement) précédemment enregistré sur le disque. Il lit tous les fichiers de données shard `shard_*.pkl` depuis un dossier de jeu de données sélectionné dans le répertoire des jeux de données et renvoie les vecteurs latents et les données de conditionnement combinés pour utilisation dans les workflows d'entraînement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `folder_name` | Jeu de données enregistré à charger, depuis le répertoire des jeux de données. | COMBO | Oui | Une option par dossier de jeu de données trouvé dans le répertoire des jeux de données |

Remarque : les options de `folder_name` sont générées automatiquement en parcourant le répertoire des jeux de données. Un sous-dossier est répertorié comme jeu de données lorsqu'il contient un fichier `metadata.json` ou au moins un fichier `.safetensors` (le parcours ne descend pas dans un dossier correspondant). Le dossier de jeu de données sélectionné est recherché dans tous les répertoires racine de jeux de données configurés, et le nom du dossier doit correspondre à un sous-dossier dans l'un de ces répertoires racine. Le nœud lit tous les fichiers nommés `shard_*.pkl` dans le dossier sélectionné, par ordre trié, et génère une erreur si aucun fichier shard n'est trouvé ou si le dossier est introuvable.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latents` | Liste de dictionnaires latents (liste de sortie), où chaque dictionnaire contient une clé `"samples"` avec un tenseur. | LATENT |
| `conditioning` | Liste de listes de conditionnement (liste de sortie), où chaque liste interne contient les données de conditionnement pour l'échantillon correspondant. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/fr.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
