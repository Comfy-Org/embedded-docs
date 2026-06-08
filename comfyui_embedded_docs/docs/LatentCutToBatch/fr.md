Voici la traduction en français de la documentation du nœud **LatentCutToBatch** :

Le nœud **LatentCutToBatch** divise une représentation latente le long d'une dimension choisie en plusieurs tranches et les empile dans un nouveau lot. Cela permet de traiter indépendamment différentes parties d'un échantillon latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | La représentation latente à diviser et à mettre en lot. | LATENT | Oui | - |
| `dim` | La dimension selon laquelle couper les échantillons latents. `"t"` fait référence à la dimension temporelle, `"x"` à la largeur et `"y"` à la hauteur. | COMBO | Oui | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | La taille de chaque tranche à découper dans la dimension spécifiée. Si la taille de la dimension n'est pas parfaitement divisible par cette valeur, le reste est ignoré. (par défaut : 1) | INT | Oui | 1 à 16384 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Le lot latent résultant, contenant les échantillons découpés et empilés. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/fr.md)

---
**Source fingerprint (SHA-256):** `38d0ace3ef91e47e3f047aa7057c61e09b6534702526b34691b4bc239c933cd3`
