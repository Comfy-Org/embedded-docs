# LTX Video Upscale

Agrandit une vidéo à 1080p, 4K ou 8K, en conservant son rapport d'aspect, sa fréquence d'images et son audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video` | Vidéo à agrandir, avec un petit côté d'au moins 480 pixels et au plus 7680x4320 dans les deux orientations. Jusqu'à 2401 images pour 1080p, 601 images pour 4K et 241 images pour 8K. | VIDEO | Oui | - |
| `resolution` | Taille de sortie, aussi grande que possible dans 1920x1080, 3840x2160 ou 7680x4320 et orientée pour les vidéos portrait. Par défaut : `"4k"`. | COMBO | Oui | `"1080p"`<br>`"4k"`<br>`"8k"` |
| `seed` | Contrôle si le nœud est réexécuté ; les résultats sont non déterministes quel que soit le seed. Par défaut : 42. | INT | Non | 0 à 4294967295 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo agrandie, avec son audio conservé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoUpscale/fr.md)

---
**Source fingerprint (SHA-256):** `e9b3b760365568ab2f6572c5f4f28758d67c4f5795fc39716ed4f648aafef80e`
