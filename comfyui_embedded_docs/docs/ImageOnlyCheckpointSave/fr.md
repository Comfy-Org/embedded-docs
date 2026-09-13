# ImageOnlyCheckpointSave

Ce nœud enregistre un fichier checkpoint qui regroupe un modèle avec son encodeur visuel CLIP et son VAE. Le fichier est écrit au format safetensors dans le répertoire de sortie, en utilisant le préfixe de nom de fichier fourni, afin que les composants liés à l'image d'un modèle puissent être stockés sous forme d'un seul checkpoint.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle à enregistrer dans le checkpoint | MODEL | Oui | - |
| `clip_vision` | L'encodeur visuel CLIP à enregistrer dans le checkpoint | CLIP_VISION | Oui | - |
| `vae` | Le VAE (autoencodeur variationnel) à enregistrer dans le checkpoint | VAE | Oui | - |
| `filename_prefix` | Le préfixe du nom de fichier de sortie (par défaut : "checkpoints/ComfyUI") | STRING | Oui | - |
| `prompt` | Paramètre masqué qui reçoit les données de prompt du workflow | PROMPT | Non | - |
| `extra_pnginfo` | Paramètre masqué qui reçoit des métadonnées PNG supplémentaires | EXTRA_PNGINFO | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| - | Ce nœud ne renvoie aucune sortie | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/fr.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
