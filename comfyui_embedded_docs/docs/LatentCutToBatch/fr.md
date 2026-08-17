# LatentCutToBatch

Le nœud LatentCutToBatch découpe une représentation latente le long d'une dimension choisie en plusieurs tranches, puis les empile dans un nouveau lot. Cela permet de traiter indépendamment différentes parties d'un échantillon latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | La représentation latente à découper et à regrouper en lot. | LATENT | Oui | - |
| `dim` | La dimension le long de laquelle découper les échantillons latents. `"t"` fait référence à la dimension temporelle, `"x"` à la largeur et `"y"` à la hauteur. | COMBO | Oui | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | La taille de chaque tranche à découper selon la dimension spécifiée. Si la taille de la dimension n'est pas parfaitement divisible par cette valeur, le reste est ignoré. (par défaut : 1) | INT | Oui | 1 à 16384 (résolution maximale) |

Remarque : Si la dimension sélectionnée est l'axe du lot ou des canaux, l'entrée est renvoyée telle quelle. Si `slice_size` est plus grand que la taille de la dimension, la dimension entière est utilisée comme une seule tranche.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Le lot latent résultant, contenant les échantillons découpés et empilés. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/fr.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
