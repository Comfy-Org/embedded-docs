> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/fr.md)

Le nœud SaveWEBM enregistre une séquence d'images sous forme de fichier vidéo WEBM. Il prend plusieurs images en entrée et les encode en une vidéo en utilisant le codec VP9 ou AV1, avec des paramètres de qualité et une fréquence d'images configurables. Le fichier vidéo résultant est sauvegardé dans le répertoire de sortie avec des métadonnées incluant les informations de l'invite.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | - | Séquence d'images d'entrée à encoder sous forme d'images vidéo |
| `filename_prefix` | STRING | Non | - | Préfixe pour le nom du fichier de sortie (par défaut : "ComfyUI") |
| `codec` | COMBO | Oui | "vp9"<br>"av1" | Codec vidéo à utiliser pour l'encodage |
| `fps` | FLOAT | Non | 0,01-1000,0 | Fréquence d'images pour la vidéo de sortie (par défaut : 24,0) |
| `crf` | FLOAT | Non | 0-63,0 | Paramètre de qualité où un crf plus élevé signifie une qualité inférieure avec une taille de fichier plus petite, un crf plus bas signifie une qualité supérieure avec une taille de fichier plus grande (par défaut : 32,0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `ui` | PREVIEW | Aperçu vidéo affichant le fichier WEBM sauvegardé |

---
**Source fingerprint (SHA-256):** `761ce5148c273ffe3789be75c2a00268241d3ec7ecebd5b10efd1b1cc98d85ea`
