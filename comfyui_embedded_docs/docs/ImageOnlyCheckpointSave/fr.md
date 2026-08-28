# ImageOnlyCheckpointSave

Le nœud ImageOnlyCheckpointSave enregistre un fichier checkpoint contenant un modèle, un encodeur de vision CLIP et un VAE. Il crée un fichier safetensors avec le préfixe de nom de fichier spécifié et le stocke dans le répertoire de sortie. Ce nœud est spécifiquement conçu pour enregistrer ensemble les composants de modèle liés aux images dans un seul fichier checkpoint.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à enregistrer dans le checkpoint | MODEL | Oui | - |
| `clip_vision` | L'encodeur de vision CLIP à enregistrer dans le checkpoint | CLIP_VISION | Oui | - |
| `vae` | Le VAE (auto-encodeur variationnel) à enregistrer dans le checkpoint | VAE | Oui | - |
| `préfixe_de_nom_de_fichier` | Le préfixe du nom de fichier de sortie (défaut : "checkpoints/ComfyUI") | STRING | Oui | - |
| `prompt` | Paramètre caché pour les données de prompt du workflow | PROMPT | Non | - |
| `extra_pnginfo` | Métadonnées PNG supplémentaires | EXTRA_PNGINFO | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| - | Ce nœud ne retourne aucune sortie | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/fr.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
