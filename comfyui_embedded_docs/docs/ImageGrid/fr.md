> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/fr.md)

Voici la traduction de la documentation du nœud ImageGrid :

Le nœud Grille d'Images combine plusieurs images en une seule grille ou collage organisé. Il prend une liste d'images et les dispose en un nombre spécifié de colonnes, en redimensionnant chaque image pour s'adapter à une taille de cellule définie et en ajoutant un espacement optionnel entre elles. Le résultat est une seule nouvelle image contenant toutes les images d'entrée dans une disposition en grille.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | - | Une liste d'images à disposer dans la grille. Le nœud nécessite au moins une image pour fonctionner. |
| `columns` | INT | Non | 1 - 20 | Le nombre de colonnes dans la grille (par défaut : 4). |
| `cell_width` | INT | Non | 32 - 2048 | La largeur, en pixels, de chaque cellule de la grille (par défaut : 256). |
| `cell_height` | INT | Non | 32 - 2048 | La hauteur, en pixels, de chaque cellule de la grille (par défaut : 256). |
| `padding` | INT | Non | 0 - 50 | La quantité d'espacement, en pixels, à placer entre les images dans la grille (par défaut : 4). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `image` | IMAGE | L'image de sortie unique contenant toutes les images d'entrée disposées en grille. |

---
**Source fingerprint (SHA-256):** `79d0942c79d3966d06fe804f839c1d677764cef90265bd621bf915fe6de0ad46`
