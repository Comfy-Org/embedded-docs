> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomCropImages/fr.md)

Le nœud Random Crop Images sélectionne aléatoirement une section rectangulaire dans chaque image d'entrée et la recadre aux dimensions spécifiées. Cette opération est couramment utilisée pour l'augmentation de données afin de créer des variations d'images d'entraînement. La position aléatoire du recadrage est déterminée par une valeur de `seed`, garantissant la reproductibilité du même recadrage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image à recadrer. |
| `width` | INT | Non | 1 - 8192 | La largeur de la zone de recadrage (par défaut : 512). |
| `height` | INT | Non | 1 - 8192 | La hauteur de la zone de recadrage (par défaut : 512). |
| `seed` | INT | Non | 0 - 18446744073709551615 | Nombre utilisé pour contrôler la position aléatoire du recadrage (par défaut : 0). |

**Remarque :** Les paramètres `width` et `height` doivent être inférieurs ou égaux aux dimensions de l'image d'entrée. Si une dimension spécifiée est plus grande que l'image, le recadrage sera limité aux bords de l'image.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `image` | IMAGE | L'image résultante après application du recadrage aléatoire. |

---
**Source fingerprint (SHA-256):** `bc4aca8cc63bde28fee906a92463b73436ba48ba69d7c1ff13881ac900e252a8`
