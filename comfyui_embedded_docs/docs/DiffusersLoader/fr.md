# Chargeur de diffuseurs

Le nœud DiffusersLoader charge des modèles pré-entraînés enregistrés au format diffusers. Il recherche dans les dossiers `diffusers` configurés des répertoires contenant un fichier `model_index.json`, vous permet d'en sélectionner un, et le charge en tant que composants MODEL, CLIP et VAE utilisés dans le pipeline. Ce nœud est obsolète, mais reste disponible pour la compatibilité avec les modèles diffusers de Hugging Face.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `chemin_modèle` | Le chemin vers le répertoire du modèle diffusers à charger. Le nœud analyse automatiquement les dossiers diffusers configurés pour trouver les modèles valides et liste les options disponibles. | COMBO | Oui | Plusieurs options disponibles<br>(remplie automatiquement à partir des dossiers diffusers) |

## Sorties

| Nom de sortie | Description | Type de données |
|-----------|-------------|-----------------|
| `MODEL` | Le composant modèle chargé à partir du format diffusers. | MODEL |
| `CLIP` | Le composant modèle CLIP chargé à partir du format diffusers. | CLIP |
| `VAE` | Le composant VAE (autoencodeur variationnel) chargé à partir du format diffusers. | VAE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/fr.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
