# LTX Video Reframe

Recadre une vidéo vers une nouvelle résolution et un nouveau rapport d’aspect. La zone située à l’extérieur de la vidéo d’origine est générée pour correspondre à son contenu, de sorte qu’un clip portrait peut devenir paysage, ou inversement.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `video` | Vidéo à recadrer, jusqu’à 60 secondes et 1800 images, chaque côté mesurant entre 64 et 4096 pixels. | VIDEO | Oui | - |
| `resolution` | Taille et rapport d’aspect de sortie, en 720p ou 1080p. Par défaut : `"(1080p) 1080x1920 (9:16)"`. | COMBO | Oui | `"(720p) 720x720 (1:1)"`<br>`"(720p) 720x900 (4:5)"`<br>`"(720p) 900x720 (5:4)"`<br>`"(720p) 720x1280 (9:16)"`<br>`"(720p) 1280x720 (16:9)"`<br>`"(1080p) 1080x1080 (1:1)"`<br>`"(1080p) 1080x1350 (4:5)"`<br>`"(1080p) 1350x1080 (5:4)"`<br>`"(1080p) 1080x1920 (9:16)"`<br>`"(1080p) 1920x1080 (16:9)"` |
| `placement` | Emplacement de la vidéo d’origine dans le nouveau cadre. La vidéo remplit toujours un côté du cadre ; le point d’ancrage ne la déplace donc que le long de l’autre côté. Par défaut : `"center"`. | DYNAMIC_COMBO | Oui | `"center"`<br>`"top"`<br>`"bottom"`<br>`"left"`<br>`"right"`<br>`"custom"` |
| `seed` | Contrôle si le nœud est réexécuté ; les résultats ne sont pas déterministes, quelle que soit la graine. Par défaut : 42. | INT | Non | 0 à 4294967295 |

### Entrées de placement « custom »

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `x` | Bord gauche de la vidéo, exprimé en fraction de la largeur de sortie. Par défaut : 0.25. | FLOAT | Non | 0.0 à 0.99 (pas : 0.01) |
| `y` | Bord supérieur de la vidéo, exprimé en fraction de la hauteur de sortie. Par défaut : 0.25. | FLOAT | Non | 0.0 à 0.99 (pas : 0.01) |
| `width` | Largeur de la vidéo, exprimée en fraction de la largeur de sortie ; la hauteur suit le rapport d’aspect de la vidéo. La vidéo doit rester à l’intérieur du cadre et peut être agrandie au maximum de 2x. Par défaut : 0.5. | FLOAT | Non | 0.01 à 1.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo recadrée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoReframe/fr.md)

---
**Source fingerprint (SHA-256):** `85fcce4a8054fa8faf0085a55510ee09bce89afd1cf9f19d6ea45105549f2656`
