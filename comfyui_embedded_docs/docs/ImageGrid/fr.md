> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/fr.md)

Le nœud Image Grid combine plusieurs images en une seule image organisée sous forme de grille ou de collage. Il prend une liste d'images et les dispose en un nombre spécifié de colonnes, redimensionnant chaque image pour qu'elle s'adapte à une taille de cellule définie et en ajoutant un espacement optionnel entre elles. Le résultat est une seule nouvelle image contenant toutes les images d'entrée dans une disposition en grille.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | - | Une liste d'images à organiser dans la grille. Le nœud nécessite au moins une image pour fonctionner. |
| `columns` | INT | Non | 1 - 20 | Le nombre de colonnes dans la grille (par défaut : 4). |
| `cell_width` | INT | Non | 32 - 2048 | La largeur, en pixels, de chaque cellule de la grille (par défaut : 256). |
| `cell_height` | INT | Non | 32 - 2048 | La hauteur, en pixels, de chaque cellule de la grille (par défaut : 256). |
| `padding` | INT | Non | 0 - 50 | La quantité d'espacement, en pixels, à placer entre les images dans la grille (par défaut : 4). |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image de sortie unique contenant toutes les images d'entrée disposées en grille. |
