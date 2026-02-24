> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomCropImages/fr.md)

Le nœud Random Crop Images sélectionne aléatoirement une section rectangulaire de chaque image d'entrée et la recadre à une largeur et une hauteur spécifiées. Cette opération est couramment utilisée pour l'augmentation de données afin de créer des variations d'images d'entrée pour l'entraînement. La position aléatoire du recadrage est déterminée par une valeur de `seed`, garantissant que le même recadrage puisse être reproduit.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image à recadrer. |
| `width` | INT | Non | 1 - 8192 | La largeur de la zone de recadrage (par défaut : 512). |
| `height` | INT | Non | 1 - 8192 | La hauteur de la zone de recadrage (par défaut : 512). |
| `seed` | INT | Non | 0 - 18446744073709551615 | Un nombre utilisé pour contrôler la position aléatoire du recadrage (par défaut : 0). |

**Note :** Les paramètres `width` et `height` doivent être inférieurs ou égaux aux dimensions de l'image d'entrée. Si une dimension spécifiée est plus grande que l'image, le recadrage sera limité aux bords de l'image.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image résultante après l'application du recadrage aléatoire. |
