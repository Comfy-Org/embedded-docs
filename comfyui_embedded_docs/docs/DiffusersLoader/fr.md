# Chargeur de diffuseurs

Le nœud DiffusersLoader est obsolète. Il charge des modèles pré-entraînés enregistrés au format diffusers de Hugging Face et renvoie les trois composants standard nécessaires au pipeline : MODEL, CLIP et VAE. Le nœud analyse automatiquement les dossiers diffusers configurés à la recherche de répertoires de modèles valides (dossiers contenant un fichier `model_index.json`) et vous permet de choisir celui à charger.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_path` | Le chemin vers le répertoire du modèle diffusers à charger. Le nœud analyse les dossiers diffusers configurés et liste chaque répertoire contenant un fichier `model_index.json`. | COMBO | Oui | Rempli automatiquement à partir des dossiers diffusers configurés (chaque sous-répertoire contenant un fichier `model_index.json`) |

Remarque : le chemin sélectionné est validé par rapport à la liste des modèles découverts. Le chargement échoue avec une erreur si le chemin ne figure plus dans la liste ou si le répertoire du modèle est introuvable.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le composant modèle chargé à partir du format diffusers | MODEL |
| `CLIP` | Le composant CLIP d'encodage de texte chargé à partir du format diffusers | CLIP |
| `VAE` | Le composant VAE (auto-encodeur variationnel) chargé à partir du format diffusers | VAE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/fr.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
