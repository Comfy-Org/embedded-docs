> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/fr.md)

Le nœud PrimitiveBoundingBox crée une zone rectangulaire simple définie par sa position et sa taille. Il prend les coordonnées X et Y pour le coin supérieur gauche, ainsi que les valeurs de largeur et de hauteur, et produit une structure de données de boîte englobante qui peut être utilisée par d'autres nœuds dans un flux de travail.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `x` | INT | Non | 0 à 8192 | La coordonnée X du coin supérieur gauche de la boîte englobante (par défaut : 0). |
| `y` | INT | Non | 0 à 8192 | La coordonnée Y du coin supérieur gauche de la boîte englobante (par défaut : 0). |
| `width` | INT | Non | 1 à 8192 | La largeur de la boîte englobante (par défaut : 512). |
| `height` | INT | Non | 1 à 8192 | La hauteur de la boîte englobante (par défaut : 512). |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `bounding_box` | BOUNDING_BOX | Une structure de données contenant les propriétés `x`, `y`, `width` et `height` du rectangle défini. |
