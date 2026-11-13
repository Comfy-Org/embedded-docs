# LTX Video AlphaGen

Extrait un masque alpha en niveaux de gris, blanc pour le premier plan, qui correspond à la trame vidéo d’entrée, image par image. Envoyez le masque à Get Video Components et Image To Mask pour le transformer en masque. L’audio n’est pas conservé.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `video` | Vidéo à convertir en masque, jusqu’à 10 secondes et 3840x2160 dans l’une ou l’autre orientation. | VIDEO | Oui | - |
| `seed` | Contrôle si le nœud est réexécuté ; les résultats ne sont pas déterministes quelle que soit la valeur de `seed`. Par défaut : 42. | INT | Non | 0 à 4294967295 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `matte` | Le masque alpha sous forme de vidéo, avec une image pour chaque image d’entrée et sans audio. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoAlphaGen/fr.md)

---
**Source fingerprint (SHA-256):** `54a8304c2d092a736ad7fb86c8497aceda6340886beb81b6068a3de5a387a746`
