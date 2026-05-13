> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/fr.md)

Le nœud ImageOnlyCheckpointSave enregistre un fichier de point de contrôle contenant un modèle, un encodeur de vision CLIP et un VAE. Il crée un fichier safetensors avec le préfixe de nom de fichier spécifié et le stocke dans le répertoire de sortie. Ce nœud est spécialement conçu pour sauvegarder ensemble les composants du modèle liés à l'image dans un seul fichier de point de contrôle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle à enregistrer dans le point de contrôle |
| `clip_vision` | CLIP_VISION | Oui | - | L'encodeur de vision CLIP à enregistrer dans le point de contrôle |
| `vae` | VAE | Oui | - | Le VAE (Autoencodeur Variationnel) à enregistrer dans le point de contrôle |
| `filename_prefix` | STRING | Oui | - | Le préfixe pour le nom du fichier de sortie (par défaut : "checkpoints/ComfyUI") |
| `prompt` | PROMPT | Non | - | Paramètre caché pour les données d'invite du workflow |
| `extra_pnginfo` | EXTRA_PNGINFO | Non | - | Paramètre caché pour les métadonnées PNG supplémentaires |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| - | - | Ce nœud ne renvoie aucune sortie |

---
**Source fingerprint (SHA-256):** `d2a26933f0e2fcccf3c57f50038fb40ef5b23d00ccdd2e1d215b3cb78203b9fd`
