# EnregistrerWEBM

Le nœud SaveWEBM enregistre une séquence d'images sous forme de fichier vidéo WEBM. Il encode les images d'entrée en une vidéo à l'aide du codec VP9 ou AV1 avec des paramètres configurables de taux d'images par seconde et de qualité, puis enregistre le fichier dans le répertoire de sortie. Les métadonnées du prompt et du workflow sont intégrées dans le fichier vidéo lorsqu'elles sont disponibles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | La séquence d'images à encoder dans la vidéo. Les images RGBA sont enregistrées avec leur canal alpha en tant que transparence (codec vp9 uniquement). | IMAGE | Oui | - |
| `filename_prefix` | Préfixe du nom de fichier de sortie ; un compteur et l'extension .webm sont ajoutés automatiquement (défaut : "ComfyUI") | STRING | Non | - |
| `codec` | Codec vidéo utilisé pour l'encodage | COMBO | Oui | "vp9"<br>"av1" |
| `fps` | Taux d'images par seconde pour la vidéo de sortie (défaut : 24.0) | FLOAT | Non | 0.01-1000.0 |
| `crf` | Un crf plus élevé signifie une qualité inférieure avec une taille de fichier plus petite, un crf plus faible signifie une qualité supérieure avec une taille de fichier plus élevée (défaut : 32.0) | FLOAT | Non | 0-63.0 |

**Note sur le canal alpha :** Le canal alpha des images RGBA n'est préservé qu'avec le codec vp9. Avec le codec av1, le canal alpha est ignoré et seules les données RVB sont encodées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | La séquence d'images d'entrée, transmise telle quelle | IMAGE |
| `ui` | Aperçu vidéo montrant le fichier WEBM enregistré | PREVIEW |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/fr.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
