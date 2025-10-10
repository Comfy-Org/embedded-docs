> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée depuis laquelle extraire les informations de taille |
| `unique_id` | UNIQUE_ID | Non | - | Identifiant interne utilisé pour afficher les informations de progression |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `width` | INT | La largeur de l'image d'entrée en pixels |
| `height` | INT | La hauteur de l'image d'entrée en pixels |
| `batch_size` | INT | Le nombre d'images dans le lot |