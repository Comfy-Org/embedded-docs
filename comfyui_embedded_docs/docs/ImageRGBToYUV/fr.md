Le nœud ImageRGBToYUV convertit des images couleur RVB vers l'espace colorimétrique YUV. Il prend une image RVB en entrée et la sépare en trois canaux distincts : Y (luminance), U (projection bleue) et V (projection rouge). Chaque canal de sortie est renvoyé sous forme d'image en niveaux de gris représentant le composant YUV correspondant.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image RVB d'entrée à convertir vers l'espace colorimétrique YUV | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `U` | Le composant de luminance (luminosité) de l'espace colorimétrique YUV | IMAGE |
| `V` | Le composant de projection bleue de l'espace colorimétrique YUV | IMAGE |
| `V` | Le composant de projection rouge de l'espace colorimétrique YUV | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/fr.md)

---
**Source fingerprint (SHA-256):** `119cba119b62c7b46ffdd2c0feca932a9af1ec41c338fead23c21fdf76a6abb2`
