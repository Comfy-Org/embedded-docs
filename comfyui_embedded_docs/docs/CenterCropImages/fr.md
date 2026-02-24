> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/fr.md)

Le nœud Center Crop Images recadre une image depuis son centre selon une largeur et une hauteur spécifiées. Il calcule la région centrale de l'image d'entrée et en extrait une zone rectangulaire aux dimensions définies. Si la taille de recadrage demandée est plus grande que l'image, le recadrage sera limité aux bords de l'image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à recadrer. |
| `width` | INT | Non | 1 à 8192 | La largeur de la zone de recadrage (par défaut : 512). |
| `height` | INT | Non | 1 à 8192 | La hauteur de la zone de recadrage (par défaut : 512). |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image résultante après l'opération de recadrage central. |
