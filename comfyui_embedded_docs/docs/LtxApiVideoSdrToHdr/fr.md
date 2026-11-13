# LTX Video SDR to HDR

Convertit une vidéo SDR en une vidéo HDR 10 bits en BT.2020 avec la fonction de transfert HLG, à la même résolution. L’audio n’est pas conservé.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `video` | Vidéo SDR à convertir, au maximum 3840x2160 quelle que soit l’orientation. Jusqu’à 273 images en 1080p, 193 images en 1440p et 65 images en 4K. | VIDEO | Oui | - |
| `seed` | Contrôle si le nœud se réexécute ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 42. | INT | Non | 0 à 4294967295 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo HDR 10 bits convertie, sans audio. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoSdrToHdr/fr.md)

---
**Source fingerprint (SHA-256):** `e5c0ef901f504a9477f042b4aef24935f4b85da52ccfaddfc764e9efec490915`
