Voici la traduction de la documentation technique du nœud ComfyUI, en respectant les règles établies :

## Aperçu

Ce nœud prépare une séquence d'images clés pour un segment spécifique d'un processus de génération vidéo plus long. Il prend un lot d'images d'entrée et une piste audio, calcule le nombre total d'images que la vidéo complète doit avoir en fonction de la durée audio, puis distribue les images d'entrée comme images clés sur le segment choisi, en complétant le reste avec des images vides. Il extrait également la portion correspondante de l'audio pour ce segment.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Les images d'entrée à distribuer comme images clés. | IMAGE | Oui | Lot d'images |
| `segment_length` | Longueur de ce segment en images (par défaut : 149). | INT | Oui | 1 à 10000 |
| `segment_index` | Index de ce segment (0 pour le premier, 1 pour le second, etc., par défaut : 0). | INT | Oui | 0 à 100 |
| `audio` | Audio utilisé pour calculer le nombre total d'images de sortie et extraire l'audio du segment. | AUDIO | Oui | Données audio |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `keyframes_sequence` | Séquence d'images clés complétée pour le segment spécifié. | IMAGE |
| `keyframes_mask` | Masque indiquant les images valides (1 pour les positions d'images clés, 0 pour les positions complétées). | MASK |
| `audio_segment` | Segment audio pour ce segment vidéo. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/fr.md)

---
**Source fingerprint (SHA-256):** `5a104b45faaa870727d4c45e6327e7233110b40dc5a13515a29e5f14de2050e0`
