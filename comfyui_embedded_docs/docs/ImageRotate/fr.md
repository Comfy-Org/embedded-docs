> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/fr.md)

Le nœud ImageRotate fait pivoter une image d'entrée selon des angles spécifiés. Il prend en charge quatre options de rotation : aucune rotation, 90 degrés dans le sens horaire, 180 degrés et 270 degrés dans le sens horaire. La rotation est effectuée à l'aide d'opérations tensorielle efficaces qui préservent l'intégrité des données de l'image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à faire pivoter |
| `rotation` | STRING | Oui | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" | L'angle de rotation à appliquer à l'image |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image de sortie après rotation |
