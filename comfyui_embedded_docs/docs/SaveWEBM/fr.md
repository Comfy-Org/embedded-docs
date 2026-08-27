# EnregistrerWEBM

Le nœud SaveWEBM enregistre une séquence d'images sous forme de fichier vidéo WEBM. Il prend plusieurs images en entrée et les encode en une vidéo en utilisant le codec VP9 ou AV1, avec des paramètres de qualité et une fréquence d'images configurables. Le fichier vidéo résultant est enregistré dans le répertoire de sortie avec des métadonnées incluant les informations du prompt.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Les images RGBA sont enregistrées avec leur canal alpha comme transparence (codec vp9 uniquement). | IMAGE | Oui | - |
| `préfixe_de_nom_de_fichier` | Préfixe pour le nom du fichier de sortie (par défaut : "ComfyUI"). | STRING | Non | - |
| `codec` | Codec vidéo à utiliser pour l'encodage. | COMBO | Oui | "vp9"<br>"av1" |
| `fps` | Fréquence d'images pour la vidéo de sortie (par défaut : 24.0). | FLOAT | Non | 0.01-1000.0 |
| `crf` | Un crf plus élevé signifie une qualité inférieure avec un fichier plus petit ; un crf plus faible signifie une qualité supérieure avec un fichier plus volumineux (par défaut : 32.0). | FLOAT | Non | 0-63.0 |

**Remarque sur le canal alpha :** Le canal alpha des images RGBA n'est préservé qu'avec le codec VP9. Avec le codec AV1, le canal alpha est ignoré et seules les données RVB sont encodées.

**Remarque sur le nommage des fichiers :** Les vidéos sont enregistrées dans le répertoire de sortie sous la forme `{filename_prefix}_{counter:05}_.webm`, où le compteur s'incrémente automatiquement pour éviter d'écraser les fichiers existants.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | Les images d'entrée, transmises telles quelles après l'enregistrement de la vidéo. | IMAGE |
| UI preview | Aperçu vidéo montrant le fichier WEBM enregistré. | PREVIEW |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/fr.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
