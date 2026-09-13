# ImageRGBToYUV

Le nœud ImageRGBToYUV convertit une image RGB en composantes colorimétriques de style YUV à l’aide d’une conversion de couleur RGB vers YCbCr. Il sépare le résultat en trois images distinctes — Y (luminance, ou luminosité), U (chrominance de différence bleue) et V (chrominance de différence rouge) — et renvoie chaque composante avec la même largeur et la même hauteur que l’entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Image RGB d’entrée à convertir en composantes Y, U et V. Si l’image contient un canal alpha, seuls les trois premiers canaux (RGB) sont utilisés. | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `Y` | Composante de luminance (luminosité) de l’espace colorimétrique YUV, renvoyée sous forme d’image à trois canaux | IMAGE |
| `U` | Composante de chrominance de différence bleue de l’espace colorimétrique YUV, renvoyée sous forme d’image à trois canaux | IMAGE |
| `V` | Composante de chrominance de différence rouge de l’espace colorimétrique YUV, renvoyée sous forme d’image à trois canaux | IMAGE |

Chaque sortie possède la même largeur et la même hauteur que l’image d’entrée. La composante Y, U ou V correspondante est répétée sur les trois canaux, de sorte que chaque sortie soit renvoyée sous forme d’image standard à trois canaux.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/fr.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
