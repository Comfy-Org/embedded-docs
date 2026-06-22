# ImageOnlyCheckpointSave

Le nœud ImageOnlyCheckpointSave enregistre un fichier de point de contrôle contenant un modèle, un encodeur de vision CLIP et un VAE. Il crée un fichier safetensors avec le préfixe de nom de fichier spécifié et le stocke dans le répertoire de sortie. Ce nœud est spécialement conçu pour sauvegarder ensemble les composants du modèle liés à l'image dans un seul fichier de point de contrôle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à enregistrer dans le point de contrôle | MODEL | Oui | - |
| `clip_vision` | L'encodeur de vision CLIP à enregistrer dans le point de contrôle | CLIP_VISION | Oui | - |
| `vae` | Le VAE (Autoencodeur Variationnel) à enregistrer dans le point de contrôle | VAE | Oui | - |
| `préfixe_de_nom_de_fichier` | Le préfixe pour le nom du fichier de sortie (par défaut : "checkpoints/ComfyUI") | STRING | Oui | - |
| `prompt` | Paramètre caché pour les données d'invite du workflow | PROMPT | Non | - |
| `extra_pnginfo` | Paramètre caché pour les métadonnées PNG supplémentaires | EXTRA_PNGINFO | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| - | Ce nœud ne renvoie aucune sortie | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/fr.md)

---
**Source fingerprint (SHA-256):** `d2a26933f0e2fcccf3c57f50038fb40ef5b23d00ccdd2e1d215b3cb78203b9fd`
