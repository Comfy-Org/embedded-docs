> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/fr.md)

Le nœud ImageYUVToRGB convertit les images de l'espace colorimétrique YUV vers l'espace colorimétrique RGB. Il prend trois images d'entrée distinctes représentant les canaux Y (luma), U (projection bleue) et V (projection rouge) et les combine en une seule image RGB en utilisant la conversion d'espace colorimétrique.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `Y` | IMAGE | Oui | - | L'image d'entrée du canal Y (luminance) |
| `U` | IMAGE | Oui | - | L'image d'entrée du canal U (projection bleue) |
| `V` | IMAGE | Oui | - | L'image d'entrée du canal V (projection rouge) |

**Note :** Les trois images d'entrée (Y, U et V) doivent être fournies ensemble et doivent avoir des dimensions compatibles pour une conversion correcte.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image RGB convertie |
