# EnregistrerWEBM

Le nœud SaveWEBM enregistre une séquence d’images dans un fichier vidéo WEBM. Il prend plusieurs images d’entrée et les encode dans une vidéo à l’aide du codec VP9 ou AV1 avec des paramètres de qualité et une fréquence d’images configurables. Le fichier vidéo résultant est enregistré dans le répertoire de sortie avec des métadonnées incluant les informations de prompt.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Les images RGBA sont enregistrées avec leur canal alpha comme transparence (codec VP9 uniquement). | IMAGE | Oui | - |
| `préfixe_de_nom_de_fichier` | Préfixe du nom de fichier de sortie (par défaut : "ComfyUI"). | STRING | Non | - |
| `codec` | Codec vidéo à utiliser pour l’encodage. | COMBO | Oui | "vp9"<br>"av1" |
| `fps` | Fréquence d’images de la vidéo de sortie (par défaut : 24.0). | FLOAT | Non | 0.01-1000.0 |
| `crf` | Un crf plus élevé signifie une qualité inférieure avec une taille de fichier plus petite ; un crf plus faible signifie une qualité supérieure avec une taille de fichier plus grande (par défaut : 32.0). | FLOAT | Non | 0-63.0 |

**Note sur le canal alpha :** Le canal alpha des images RGBA n’est préservé que lors de l’utilisation du codec VP9. Avec le codec AV1, le canal alpha est ignoré et seules les données RVB sont encodées.

**Note sur le nommage des fichiers :** Les vidéos sont enregistrées dans le répertoire de sortie sous la forme `{filename_prefix}_{counter:05}_.webm`, où le compteur s’incrémente automatiquement pour éviter d’écraser les fichiers existants.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | Les images d’entrée, transmises sans modification après l’enregistrement de la vidéo. | IMAGE |
| UI preview | Aperçu vidéo montrant le fichier WEBM enregistré. | PREVIEW |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/fr.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
