> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageToTileList/fr.md)

Le nœud Split Image into List of Tiles (Diviser l'image en liste de tuiles) divise une image d'entrée unique en une série de sections rectangulaires plus petites et se chevauchant, appelées tuiles. Il crée une liste groupée de ces tuiles, qui peuvent ensuite être traitées individuellement par d'autres nœuds. La taille de chaque tuile ainsi que le degré de chevauchement entre elles peuvent être spécifiés.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à diviser en tuiles. |
| `tile_width` | INT | Non | 64 à 1048576 | La largeur de chaque tuile de sortie en pixels (par défaut : 1024). |
| `tile_height` | INT | Non | 64 à 1048576 | La hauteur de chaque tuile de sortie en pixels (par défaut : 1024). |
| `overlap` | INT | Non | 0 à 4096 | Le nombre de pixels de chevauchement entre les tuiles adjacentes (par défaut : 128). |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | Une liste groupée contenant toutes les tuiles d'image individuelles. |