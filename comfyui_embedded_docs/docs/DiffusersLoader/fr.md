> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/fr.md)

Le nœud DiffusersLoader charge des modèles pré-entraînés au format diffusers. Il recherche les répertoires de modèles diffusers valides contenant un fichier `model_index.json` et les charge en tant que composants MODEL, CLIP et VAE pour une utilisation dans le pipeline. Ce nœud fait partie de la catégorie des chargeurs obsolètes et assure la compatibilité avec les modèles diffusers de Hugging Face.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `chemin_modèle` | STRING | Oui | Plusieurs options disponibles<br>(remplissage automatique à partir des dossiers diffusers) | Le chemin vers le répertoire du modèle diffusers à charger. Le nœud analyse automatiquement les modèles diffusers valides dans les dossiers diffusers configurés et liste les options disponibles. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `MODEL` | MODEL | Le composant modèle chargé à partir du format diffusers |
| `CLIP` | CLIP | Le composant modèle CLIP chargé à partir du format diffusers |
| `VAE` | VAE | Le composant VAE (autoencodeur variationnel) chargé à partir du format diffusers |

---
**Source fingerprint (SHA-256):** `59be9923ed76d4859d5f7217a802c43297cb5af3d895eb6713edea97a32c3db2`
