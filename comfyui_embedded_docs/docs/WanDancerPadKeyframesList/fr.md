# WanDancerPadKeyframesList

Voici la traduction en français de la documentation, en respectant vos règles :

## Aperçu

Ce nœud prend une séquence d'images et une piste audio optionnelle, puis les divise en un nombre spécifié de segments rembourrés. Il est conçu pour préparer des séquences d'images clés pour la génération vidéo, où chaque segment est rembourré à une longueur uniforme et un masque correspondant est créé pour indiquer les images valides.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | La séquence d'images d'entrée à diviser en segments. | IMAGE | Oui | N/A |
| `segment_length` | Longueur de chaque segment en images (par défaut : 149). | INT | Oui | 1 à 10000 |
| `num_segments` | Nombre de segments rembourrés à émettre sous forme de listes (par défaut : 1). | INT | Oui | 1 à 100 |
| `audio` | Audio à découper pour chaque segment émis. | AUDIO | Non | N/A |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `keyframes_mask` | Une liste de séquences d'images clés rembourrées, une pour chaque segment. | IMAGE |
| `audio_segment` | Une liste de masques indiquant les images valides pour chaque segment. | MASK |
| `audio_segment` | Une liste de segments audio, un pour chaque segment vidéo. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframesList/fr.md)

---
**Source fingerprint (SHA-256):** `c6a3ddca3fd61fcdb287fecb6969796eebd65e70f1174abdab57912586d27d00`
