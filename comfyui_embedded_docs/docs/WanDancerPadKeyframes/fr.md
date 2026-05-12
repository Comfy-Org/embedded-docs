> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI :

## Aperçu

Ce nœud prépare une séquence d'images clés pour un segment spécifique d'un processus de génération vidéo plus long. Il prend un lot d'images d'entrée et une piste audio, calcule le nombre total d'images que la vidéo complète doit avoir en fonction de la durée audio, puis distribue les images d'entrée comme images clés sur le segment choisi, en complétant le reste avec des images vides. Il extrait également la partie correspondante de l'audio pour ce segment.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | Lot d'images | Les images d'entrée à distribuer comme images clés. |
| `segment_length` | INT | Oui | 1 à 10000 | Longueur de ce segment en images (par défaut : 149). |
| `segment_index` | INT | Oui | 0 à 100 | Index de ce segment (0 pour le premier, 1 pour le second, etc., par défaut : 0). |
| `audio` | AUDIO | Oui | Données audio | Audio utilisé pour calculer le nombre total d'images de sortie et extraire l'audio du segment. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `keyframes_sequence` | IMAGE | Séquence d'images clés complétée pour le segment spécifié. |
| `keyframes_mask` | MASK | Masque indiquant les images valides (1 pour les positions d'images clés, 0 pour les positions complétées). |
| `audio_segment` | AUDIO | Segment audio correspondant à ce segment vidéo. |